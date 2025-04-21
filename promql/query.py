import requests

def query_prometheus(prom_url, promql = "up"):
    # check if the response is not empty
    if not promql or not prom_url:
        return "Error: Prometheus URL or query is empty"
    
    response = requests.get(f"{prom_url}/api/v1/query", params={'query': promql})
    
    if response.status_code != 200:
        raise Exception(f"Error {response.status_code}: {response.text}")
    json_response = response.json()

    # check if the response is valid
    if len(json_response["data"]["result"]) == 0:
       return f"Error: No data found for query '{promql}'"
    return json_response["data"]["result"]


