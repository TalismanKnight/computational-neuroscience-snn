import numpy as np
import matplotlib.pyplot as plt

# -------------------------
# Simulation parameters
# -------------------------
time_steps = 300
tau = 10
threshold = 1.0

# STDP parameters
A_plus = 0.02
A_minus = 0.015
trace_decay = 0.9

# Initial synaptic weight
synaptic_weight = 0.5

# Neuron states
v1 = 0
v2 = 0

# Synaptic current
syn_current = 0

# STDP traces
pre_trace = 0
post_trace = 0

# Tracking
v1_history = []
v2_history = []
weight_history = []

for t in range(time_steps):

    # -------------------------
    # Neuron 1 (input neuron)
    # -------------------------
    input_current = 1.5

    dv1 = (-v1 + input_current) / tau
    v1 += dv1

    spike1 = 0
    if v1 >= threshold:
        spike1 = 1
        v1 = 0

    # -------------------------
    # Synaptic dynamics
    # -------------------------
    if spike1:
        syn_current += synaptic_weight * 5

    syn_current *= 0.9

    # -------------------------
    # Neuron 2
    # -------------------------
    dv2 = (-v2 + syn_current) / tau
    v2 += dv2

    spike2 = 0
    if v2 >= threshold:
        spike2 = 1
        v2 = 0

    # -------------------------
    # STDP learning (trace-based)
    # -------------------------

    # Decay traces
    pre_trace *= trace_decay
    post_trace *= trace_decay

    # Pre spike event
    if spike1:
        pre_trace += 1
        synaptic_weight += A_plus * post_trace

    # Post spike event
    if spike2:
        post_trace += 1
        synaptic_weight -= A_minus * pre_trace

    # Clamp weight to stable range
    synaptic_weight = max(0, min(synaptic_weight, 5))

    # -------------------------
    # Store history
    # -------------------------
    v1_history.append(v1)
    v2_history.append(v2)
    weight_history.append(synaptic_weight)

# -------------------------
# Plot results
# -------------------------
plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.plot(v1_history)
plt.title("Neuron 1 Voltage")

plt.subplot(3, 1, 2)
plt.plot(v2_history)
plt.title("Neuron 2 Voltage")

plt.subplot(3, 1, 3)
plt.plot(weight_history)
plt.title("Synaptic Weight (STDP)")

plt.tight_layout()
plt.show()