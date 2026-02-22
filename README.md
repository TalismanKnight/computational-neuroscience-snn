# 🧠 Spiking Neural Network with STDP

## Abstract

This project implements a biologically inspired spiking neural network using
Leaky Integrate-and-Fire (LIF) neurons and trace-based Spike Timing Dependent
Plasticity (STDP). The model demonstrates activity-dependent synaptic
adaptation and emergent learning dynamics in a minimal neural circuit.

## Demo Output

![STDP Demo](snn_demo.png)

This project implements a biologically inspired spiking neural network.

## Features

- Leaky Integrate-and-Fire (LIF) neurons
- Synaptic current with decay
- Hebbian learning
- Spike Timing Dependent Plasticity (STDP)
- Dynamic synaptic weight adaptation
- Voltage and weight visualization

## Run

Hebbian version:
python snn_hebbian.py

STDP version:
python snn_stdp.py

## Requirements


pip install numpy matplotlib

## How It Works

The model uses Leaky Integrate-and-Fire (LIF) neuron dynamics:

dv/dt = (-v + I) / τ

Synaptic plasticity is implemented using a trace-based Spike Timing Dependent Plasticity (STDP) rule:

Δw ∝ pre_trace × post_trace

The synaptic weight evolves dynamically depending on spike timing relationships between neurons.

## Future Work

- Add inhibitory neuron to simulate E/I balance
- Expand to multi-neuron recurrent network
- Add spike raster plot visualization
- Explore pattern learning and memory formation
- Compare Hebbian vs STDP dynamics


