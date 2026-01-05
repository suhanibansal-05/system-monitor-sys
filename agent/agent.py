import psutil
import time
import requests
import socket
import os

NODE_ID = os.getenv("NODE_ID", socket.gethostname())
SERVER_URL = "http://127.0.0.1:8000/metrics"  # use YOUR port

def collect_metrics():
    return {
        "node_id": NODE_ID,
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent,
        "disk_read": psutil.disk_io_counters().read_bytes,
        "disk_write": psutil.disk_io_counters().write_bytes,
        "timestamp": time.time()
    }

while True:
    metrics = collect_metrics()
    try:
        response = requests.post(SERVER_URL, json=metrics)
        print(f"[{NODE_ID}] sent metrics | status={response.status_code}")
    except Exception as e:
        print(f"[{NODE_ID}] error:", e)
    time.sleep(2)
