System Resource Monitor & Predictive Auto-Scaler

Distributed Linux Monitoring with Python & FastAPI

This project implements a distributed system resource monitoring and autoscaling framework for Linux-based environments. Lightweight agents run on multiple nodes to collect real-time CPU, memory, and disk I/O metrics, which are sent to a centralized FastAPI server.

The system performs both threshold-based (reactive) and predictive (proactive) autoscaling decisions using historical metrics, enabling smarter resource management and reduced risk of performance degradation.

The project was prototyped and validated using WSL2, with a cloud-agnostic architecture that can be directly adapted to VM, container, or HPC environments.


+-------------------+
| Linux Nodes       |
| (Monitoring Agent)|
+---------+---------+
          |
          | System Metrics (CPU, Memory, Disk I/O)
          v
+---------------------------+
| Central FastAPI Server    |
|  - Metric Ingestion API  |
|  - CSV Time-Series Store |
+-------------+-------------+
              |
              v
+---------------------------+
| Autoscaling Engine        |
|  - Threshold-based Logic |
|  - Predictive Logic      |
+---------------------------+




Key Features

Distributed Linux agents for real-time system monitoring

High-concurrency REST APIs built with FastAPI

Threshold-based autoscaling decisions

Predictive autoscaling using recent historical trends

Time-series metric logging for ML-based analysis

Designed and tested in a Linux-compatible WSL2 environment


Tech Stack

Language: Python

Backend Framework: FastAPI, Uvicorn

System Monitoring: psutil

Prediction / ML: scikit-learn

Environment: Linux (WSL2)




system-moniter-sys/
├── agent/
│   └── agent.py              # Monitoring agent
├── api/
│   ├── __init__.py
│   └── main.py               # FastAPI server
├── autoscaler/
│   ├── __init__.py
│   └── autoscaler.py         # Scaling logic
├── ml/
│   ├── __init__.py
│   └── predictor.py          # Metric analysis / prediction
├── data/
│   └── metrics.csv           # Runtime data (gitignored)
├── README.md
└── .gitignore



How to Run:
1 Setup virtual environment
python3 -m venv venv
source venv/bin/activate

2️ Install dependencies
pip install fastapi uvicorn psutil requests pandas scikit-learn

3️ Start the API server
python -m uvicorn api.main:app --reload

4️ Run monitoring agents (separate terminals)
export NODE_ID=node_A
python agent/agent.py


You can run multiple agents with different NODE_IDs to simulate distributed nodes.
