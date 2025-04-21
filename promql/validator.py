import requests
# Function to validate if the given URL is a valid Prometheus instance

def is_valid_prometheus(prom_url):
    try:
        response = requests.get(f"{prom_url}/api/v1/status/buildinfo")
        if response.status_code == 200:
            return True
        return False
    except requests.exceptions.RequestException:
        return False
    
    
 