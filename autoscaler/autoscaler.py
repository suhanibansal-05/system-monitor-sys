import time
from collections import deque

SCALE_UP_CPU = 75
SCALE_UP_MEM = 80
SCALE_DOWN_CPU = 30
SCALE_DOWN_MEM = 40

cpu_history = deque(maxlen=10)


def evaluate_scaling(metric):
    node = metric["node_id"]
    cpu = metric["cpu"]
    mem = metric["memory"]

    decision = "NO_ACTION"

    # Reactive scaling
    if cpu > SCALE_UP_CPU or mem > SCALE_UP_MEM:
        decision = "SCALE_UP"

    elif cpu < SCALE_DOWN_CPU and mem < SCALE_DOWN_MEM:
        decision = "SCALE_DOWN"

    # Predictive scaling
    cpu_history.append(cpu)

    if len(cpu_history) == 10:
        predicted_cpu = sum(cpu_history) / len(cpu_history)
        if predicted_cpu > SCALE_UP_CPU:
            decision = "PREDICTIVE_SCALE_UP"

    return {
        "node": node,
        "cpu": cpu,
        "memory": mem,
        "decision": decision,
        "timestamp": time.time()
    }
