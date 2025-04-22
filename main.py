import sys
import argparse
# Local imports
from promql import formatters, query, validator

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="PromQL CLI Tool")
    parser.add_argument("host", help="The Prometheus server URL (e.g., http://localhost:9090)")
    parser.add_argument("promql", help="The PromQL query to execute")
    args = parser.parse_args()

    # Validate the Prometheus server
    if not validator.is_valid_prometheus(args.host):
        print("Error: Invalid Prometheus server URL.")
        sys.exit(1)

    # Validate the PromQL query
    if not validator.is_valid_promql(args.host, args.promql):
        print("Error: Invalid PromQL query.")
        sys.exit(1)

    # Execute the query and format the results
    results = query.execute(args.host, args.promql)
    if not results:
        print("No data returned.")
        sys.exit(0)

    # Format and display the results
    formatted_table = formatters.human_readable(results)
    print(formatted_table)

# Entry point
if __name__ == "__main__":
    main()




