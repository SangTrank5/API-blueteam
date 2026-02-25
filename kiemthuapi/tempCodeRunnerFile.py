client = APIRequester()

res = client.request(
    "GET",
    "https://jsonplaceholder.typicode.com/posts/1"
)

print("Status:", res.get("status_code"))