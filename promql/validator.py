import requests

def is_valid_prometheus(prom_url):
    try:
        response = requests.get(f"{prom_url}/api/v1/status/buildinfo")
        if response.status_code == 200:
            return True
        return False
    except requests.exceptions.RequestException:
        return False


    
