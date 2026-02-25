import json
class AuthManager:
    def __init__(self, config_file="config.json"):
        with open(config_file, "r", encoding="utf-8") as f:
            self.config = json.load(f)

        self.auth_config = self.config.get("auth", {})

    def get_bearer_header(self, role="user"):
        token = None

        if role == "admin":
            token = self.auth_config.get("admin_token")
        else:
            token = self.auth_config.get("user_token")

        if not token:
            return {}

        return {
            "Authorization": f"Bearer {token}"
        }

    def get_apikey_header(self):
        api_key = self.auth_config.get("api_key")
        header_name = self.auth_config.get("api_key_header", "X-API-Key")

        if not api_key:
            return {}

        return {
            header_name: api_key
        }