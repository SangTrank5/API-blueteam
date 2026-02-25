import json
import requests

class EndpointScanner:
    def __init__(self, swagger_url):
        self.swagger_url = swagger_url
        self.endpoints = []

    def fetch_swagger(self):
        r = requests.get(self.swagger_url, timeout=10)
        r.raise_for_status()
        return r.json()

    def parse(self, swagger_json):
        paths = swagger_json.get("paths", {})

        for path, methods in paths.items():
            for method in methods.keys():
                self.endpoints.append({
                    "method": method.upper(),
                    "path": path
                })

        return self.endpoints

    def save(self, filename="endpoints.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.endpoints, f, indent=2)

        return filename