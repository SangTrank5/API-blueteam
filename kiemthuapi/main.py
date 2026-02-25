from core.engine import APIRequester
from core.auth import AuthManager
import json
req = APIRequester()
auth = AuthManager()
# Load config
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

base_url = config["target"]
endpoint = config["endpoints"]["posts"]
url = base_url + endpoint

# No Auth
r = req.request("GET",url, headers={})
print("No Auth:", r["status_code"])

# User Auth
headers_user = auth.get_bearer_header(role="user")
r = req.request("GET", url, headers=headers_user)
print("User Auth:", r["status_code"])

# Admin Auth
headers_admin = auth.get_bearer_header(role="admin")
r = req.request("GET", url, headers=headers_admin)
print("Admin Auth:", r["status_code"])

# Test apikey
headers_apikey = auth.get_apikey_header()
r = req.request("GET", url, headers=headers_apikey)
print("API Key:", r["status_code"])

base_url = "https://petstore.swagger.io/v2"
req = APIRequester()

with open("endpoints.json", "r", encoding="utf-8") as f:
    endpoints = json.load(f)

for ep in endpoints:
    url = base_url + ep["path"].replace("{petId}", "1")
    print(f"[SCAN] {ep['method']} {url}")

    res = req.request(ep["method"], url)

