import numpy as np
import matplotlib.pyplot as plt

dt = 0.1
time = np.arange(0, 100, dt)

# Neuron parameters
V1 = 0
V2 = 0

V_threshold = 1.0
V_reset = 0
tau = 10

input_current = 1.2
synaptic_weight = 0.8  # strength of connection

voltages1 = []
voltages2 = []
spikes1 = []
spikes2 = []

for t in time:
    # Neuron 1
    dV1 = (-V1 + input_current) / tau
    V1 += dV1 * dt

    spike1 = 0
    if V1 >= V_threshold:
        spike1 = 1
        V1 = V_reset

    # Neuron 2 receives spike from neuron 1
    synaptic_input = synaptic_weight * spike1

    dV2 = (-V2 + synaptic_input) / tau
    V2 += dV2 * dt

    spike2 = 0
    if V2 >= V_threshold:
        spike2 = 1
        V2 = V_reset

    voltages1.append(V1)
    voltages2.append(V2)
    spikes1.append(spike1)
    spikes2.append(spike2)

# Plot
plt.figure(figsize=(12,6))

plt.subplot(2,1,1)
plt.plot(time, voltages1)
plt.title("Neuron 1 Membrane Potential")

plt.subplot(2,1,2)
plt.plot(time, voltages2)
plt.title("Neuron 2 Membrane Potential")

plt.tight_layout()
plt.show()