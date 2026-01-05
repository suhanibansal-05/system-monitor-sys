import csv
from autoscaler.autoscaler import evaluate_scaling
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import time

app = FastAPI(title="System Resource Monitor")

metrics_store = []
CSV_FILE = "data/metrics.csv"

class Metric(BaseModel):
    node_id: str
    cpu: float
    memory: float
    disk_read: int
    disk_write: int
    timestamp: float

@app.post("/metrics")
async def receive_metrics(metric: Metric):
    data = metric.dict()
    metrics_store.append(data)

    # save to CSV
    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data.keys())
        if f.tell() == 0:
            writer.writeheader()
        writer.writerow(data)

    scaling_decision = evaluate_scaling(data)
    print("[AUTOSCALER]", scaling_decision)

    return {
        "status": "received",
        "scaling_decision": scaling_decision["decision"]
    }
@app.get("/metrics/latest")
def get_latest():
    return metrics_store[-10:]

@app.get("/health")
def health():
    return {"status": "ok", "time": time.time()}
