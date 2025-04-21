import requests

def query_prometheus(prom_url, promql):
    response = requests.get(f"{prom_url}/api/v1/query", params={'query': promql})
    if response.status_code != 200:
        raise Exception(f"Error {response.status_code}: {response.text}")
    json_response = response.json()
    return json_response["data"]["result"]


