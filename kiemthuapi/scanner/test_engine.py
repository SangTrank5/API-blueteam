from core.engine import APIRequester
client = APIRequester()

res = client.request(
    "GET",
    "https://jsonplaceholder.typicode.com/posts/1"
)

import os
print("LOG PATH:", os.getcwd())