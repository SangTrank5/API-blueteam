# test_scanner.py
from scanner.endpoint_scanner import EndpointScanner

swagger_url = "https://petstore.swagger.io/v2/swagger.json"

scanner = EndpointScanner(swagger_url)
swagger_json = scanner.fetch_swagger()
endpoints = scanner.parse(swagger_json)
scanner.save()

print(f"Found {len(endpoints)} endpoints")