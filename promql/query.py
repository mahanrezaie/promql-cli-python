import requests

def query_execute(prom_url, promql = "up"):
    # check if the response is not empty
    if not promql or not prom_url:
        return "Error: Prometheus URL or query is empty"
    
    response = requests.get(f"{prom_url}/api/v1/query", params={'query': promql})
    
    if response.status_code != 200:
        raise Exception(f"Error {response.status_code}: {response.text}")
    json_response = response.json()

    return json_response["data"]["result"]


