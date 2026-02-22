import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
dt = 0.1
time = np.arange(0, 100, dt)

# Neuron parameters
V = 0              # membrane voltage
V_threshold = 1.0  # spike threshold
V_reset = 0        # reset voltage
tau = 10           # membrane time constant

input_current = 1.2   # constant input

voltages = []
spikes = []

for t in time:
    dV = (-V + input_current) / tau
    V += dV * dt

    if V >= V_threshold:
        spikes.append(1)
        V = V_reset
    else:
        spikes.append(0)

    voltages.append(V)

# Plot
plt.figure(figsize=(10,5))
plt.plot(time, voltages)
plt.title("Membrane Potential Over Time")
plt.xlabel("Time")
plt.ylabel("Voltage")
plt.show()