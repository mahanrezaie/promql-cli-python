from tabulate import tabulate
from datetime import datetime

def format_timestamp(timestamp):
    # Convert the Unix timestamp to a human-readable format
    return datetime.fromtimestamp(float(timestamp)).strftime('%Y-%m-%d %H:%M:%S')

def orgranize_data(results):
    if not results:
        return "No data found"

    # create a list to store multiple metrics
    metric_names = []
    instances = []
    jobs = []
    values = []

    for item in results:
        metric_name = item["metric"]["__name__"]
        instance = item["metric"]["instance"]
        job = item["metric"]["job"]

        # if multiple or on value
        raw = item.get("values") or [item.get("value")]
        
        for timestamp, val in raw:
            metric_names.append(metric_name)
            instances.append(instance)
            jobs.append(job)
            values.append([format_timestamp(timestamp), val])
        
    return metric_names, instances, jobs, values

def human_readable(results):
    metric_names, instances, jobs, values = orgranize_data(results)
    table = []
    for i in range(len(metric_names)):
        table.append([metric_names[i], instances[i], jobs[i], values[i][0], values[i][1]])

    headers = ["Metric Name", "Instance", "Job", "Timestamp", "Value"]
    table = tabulate(table, headers=headers, tablefmt="grid")
    return table
    
def raw(results):
    # This function will return the raw JSON response
    return results