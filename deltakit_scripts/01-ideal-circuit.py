#!/usr/bin/env python

"""
Follow https://deltakit.riverlane.com/api/docs/guide/getting_started.html
"""

from deltakit.explorer import codes
import matplotlib.pyplot as plt

# 2 x 2 rotated planar code patch
# data qubits = 4; measure qubits = 3; total qubits = 7
code = codes.RotatedPlanarCode(width=2, height=2)
code.draw_patch()
plt.show() # close to continue

# noiseless circuit: ideal quantum gates applied to the qubits
# noiseless: perfect world; no accidental flips; no heat or interference
# using single round: measure once
# pauli-z: keep |0> the same and change the sign of |1>
# experiment: initialise 4 data qubits, let them idle, then measure them

from deltakit.explorer.codes import css_code_memory_circuit
from deltakit.circuit.gates import PauliBasis

circuit = css_code_memory_circuit(code, num_rounds=1, logical_basis=PauliBasis.Z)

# 7 qubits patch
# 4 qubits - RZ - odd coordinates
# 3 qubits - RX - even coordinates
# GateLayers
# 1. initialisation (Identity gate for making data qubits sit idle
# 2. Entangling: central measure and left and right borders
# (todo: look up time-sequencing and spatial parallelism)
# (todo: look up PyMatching library)
# 3. readout
# MX and MZ
# Detector - odd parity: error signal; even parity: no error signal
# ShiftCoordinates - move 1 unit of time for the next round of measurement
print(circuit)

stim_circuit = circuit.as_stim_circuit()
svg = stim_circuit.diagram(type="timeline-svg")
with open("circuit.svg", "w") as f:
    f.write(str(svg))
