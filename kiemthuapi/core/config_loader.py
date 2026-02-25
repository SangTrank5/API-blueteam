import json

class ConfigLoader:
    def __init__(self, path="config.json"):
        self.path = path
        self.data = self._load()

    def _load(self):
        with open(self.path, "r", encoding="utf-8") as f:
            return json.load(f)

    def get_base_url(self):
        return self.data["target"]["base_url"]

    def get_token(self, role):
        return self.data["tokens"].get(role)

    def get_api_key(self):
        return self.data["api_keys"]["default"]

    def get_endpoint(self, name):
        return self.data["endpoints"].get(name)

    def get_all_endpoints(self):
        return self.data["endpoints"]