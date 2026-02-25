import requests 
import json
from core.logger import Logger
class APIRequester:
    def __init__(self, timeout=10): 
        self.timeout = timeout #tránh việc tool bị đứng hình vĩnh viễn
        self.logger = Logger()
        self.headers = {
            "Content-Type": "application/json",
            "User-Agent": "MyHackerTool/1.0"  
        }
    #method truyen phuong thuc
    def request(self, method, url, data=None, params=None, headers=None):
        """Hàm gốc để xử lý mọi loại request"""
        final_headers = self.headers.copy()
        if headers:
            final_headers.update(headers)
         # 🔹 LOG REQUEST
        self.logger.log_request(
            method=method,
            url=url,
            headers=final_headers,
            data=data,
            params=params
        )
        try:
            response = requests.request( # hàm tổng quát của thư viện py thực thi dựa trên biến method truyền vào
                method=method,
                url=url,
                json=data,        # Tự động chuyển dict sang JSON body
                params=params,    # Query parameters cho GET
                headers=final_headers, #gửi kèm thông tin này để server biết chúng ta đang gửi dữ liệu dạng JSON.
                timeout=self.timeout
            )
               # 🔹 LOG RESPONSE
            self.logger.log_response(response.status_code, response.text)
            # Kiểm tra status code, nếu >= 400 sẽ văng ra lỗi
            response.raise_for_status() 
            
            return {
                "status_code": response.status_code,
                "data": response.json(),
                "url": response.url
            }
            
        except requests.exceptions.HTTPError as errh:
            return {"error": f"HTTP Error: {errh}", "status": response.status_code}
        except requests.exceptions.ConnectionError as errc:#URL hoặc mất mạng
            return {"error": f"Error Connecting: {errc}"}
        except requests.exceptions.Timeout as errt:#phản hồi lâu
            return {"error": f"Timeout Error: {errt}"}
        except Exception as err:
            return {"error": f"Ops: {err}"}
# --- TEST CODE (Chạy thử ngay để hoàn thành nhiệm vụ) ---
if __name__ == "__main__":
    client = APIRequester()
    
    print("--- Testing GET ---")
    get_res = client.request("GET", "https://jsonplaceholder.typicode.com/posts/1")
    print(f"Status: {get_res.get('status_code')} | Data: {get_res.get('data')}")

    print("\n--- Testing POST ---")
    payload = {"title": "Hello Admin", "body": "Nhiệm vụ hoàn thành", "userId": 99}
    post_res = client.request("POST", "https://jsonplaceholder.typicode.com/posts", data=payload)
    print(f"Status: {post_res.get('status_code')} | Response: {post_res.get('data')}")
# if __name__ == "__main__":
#     client = APIRequester(timeout=5) # Đặt timeout ngắn để test cho nhanh

#     # --- CASE 1: Lỗi 404 (Not Found) ---
#     print("\n[Test 404] Truy cập đường dẫn không tồn tại:")
#     res_404 = client.request("GET", "https://httpbin.org/status/404")
#     print(res_404)

#     # --- CASE 2: Lỗi 500 (Server Error) ---
#     # Rất quan trọng để test SQL Injection sau này
#     print("\n[Test 500] Giả lập lỗi Server:")
#     res_500 = client.request("GET", "https://httpbin.org/status/500")
#     print(res_500)

#     # --- CASE 3: Lỗi Timeout (Hết thời gian chờ) ---
#     # Giả lập server xử lý quá lâu (8 giây) trong khi timeout của ta là 5 giây
#     print("\n[Test Timeout] Server phản hồi chậm:")
#     res_timeout = client.request("GET", "https://httpbin.org/delay/8")
#     print(res_timeout)

#     # --- CASE 4: Chuyển hướng (302 Redirect) ---
#     print("\n[Test 302] Chuyển hướng trang:")
#     res_302 = client.request("GET", "https://httpbin.org/status/302")
#     print(f"Status: {res_302.get('status_code')} | Cuối cùng dừng ở: {res_302.get('url')}")