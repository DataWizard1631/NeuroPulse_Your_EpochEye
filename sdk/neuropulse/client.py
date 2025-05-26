import requests

def log(api_key, project_id, metric, value):
    payload = {
        "project_id": project_id,
        "metric": metric,
        "value": value
    }
    headers = {"Authorization": f"Bearer {api_key}"}
    requests.post("http://localhost:8000/log", json=payload, headers=headers)
