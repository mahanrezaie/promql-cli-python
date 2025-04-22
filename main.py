import sys
import argparse
import json
import os
# Local imports
from promql import formatters, query, validator

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.json")

def load_host_from_config():
    try:
        with open(CONFIG_PATH, "r") as f:
            config = json.load(f)
            return config.get("host")
    except Exception as e:
        print(f"Error loading config: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="PromQL CLI Tool")
    parser.add_argument("promql", help="The PromQL query to execute")
    parser.add_argument("-i", "--host", help="The Prometheus server URL (overrides config.json)")
    parser.add_argument("-H", "--human", action="store_true", help="Format output as human-readable table")
    args = parser.parse_args()

    # Use host from flag if provided, otherwise from config
    host = args.host if args.host else load_host_from_config()
    if not host:
        print("Error: No host provided and none found in config.json.")
        sys.exit(1)

    # Validate the Prometheus server
    if not validator.is_valid_prometheus(host):
        print("Error: Invalid Prometheus server URL.")
        sys.exit(1)

    # Validate the PromQL query
    if not validator.is_valid_promql(host, args.promql):
        print("Error: Invalid PromQL query.")
        sys.exit(1)

    # Execute the query 
    results = query.execute(host, args.promql)
    if not results:
        print("No data returned.")
        sys.exit(0)

    # Format and display the results
    if args.human:
        formatted_output = formatters.human_readable(results)
    else:
        formatted_output = formatters.raw(results)

    print(formatted_output)

if __name__ == "__main__":
    main()




