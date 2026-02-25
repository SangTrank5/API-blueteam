import os
from datetime import datetime

class Logger:
    def __init__(self, logfile="log/log.txt"):
        # Ghi log tại ROOT PROJECT (kiemthuapi/)
        os.makedirs("log", exist_ok=True)
        self.logfile = logfile
        self.logfile = os.path.join(os.getcwd(), logfile)

    def log_request(self, method, url, headers=None, data=None, params=None):
        with open(self.logfile, "a", encoding="utf-8") as f:
            f.write("\n" + "="*50 + "\n")
            f.write(f"[REQUEST] {datetime.now()}\n")
            f.write(f"{method} {url}\n")
            if params:
                f.write(f"Params: {params}\n")
            if headers:
                f.write(f"Headers: {headers}\n")
            if data:
                f.write(f"Body: {data}\n")

    def log_response(self, status_code, body):
        with open(self.logfile, "a", encoding="utf-8") as f:
            f.write(f"[RESPONSE] {datetime.now()}\n")
            f.write(f"Status: {status_code}\n")
            f.write(f"Body: {body[:500]}\n")  # tránh log quá dài