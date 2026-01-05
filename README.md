# System Resource Monitor & Predictive Auto-Scaler

A distributed Linux system monitoring and autoscaling prototype built with Python and FastAPI.

---

## Overview

This project monitors **CPU, memory, and disk I/O** across multiple Linux nodes using lightweight agents.

Collected metrics are sent to a central FastAPI server, which applies **reactive** and **predictive autoscaling logic** to decide scaling actions.

The system was prototyped using **WSL2**, but the architecture is cloud-agnostic and transferable to VM, container, or HPC environments.

---

## How It Works


---

## Autoscaling Logic

### Reactive (Threshold-Based)

- **Scale Up**
  - CPU > 75%
  - Memory > 80%
- **Scale Down**
  - CPU < 30%
  - Memory < 40%

### Predictive (Proactive)

- Maintains a rolling window of recent CPU values
- Estimates near-future load from trends
- Triggers predictive scale-up on sustained load

---

## Tech Stack

- Python
- FastAPI + Uvicorn
- psutil
- scikit-learn
- Linux / WSL2

---

## Running the Project

### 1. Setup environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn psutil requests pandas scikit-learn
```
### 2. Start API server
```bash
python -m uvicorn api.main:app --reload
```
### 3. Run monitoring agents
```bash
export NODE_ID=node_A
python agent/agent.py
```
Done! you have a working monitoring system.
