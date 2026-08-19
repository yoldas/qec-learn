#!/usr/bin/env python
"""
Demonstrate a basic quantum measurement experiment using AerSimulator.

The program puts one qubit into an equal superposition of 0 and 1, measures it
many times, and plots the circuit and the distribution of results.
"""

# https://quantum.cloud.ibm.com/docs/en/api/qiskit
# https://qiskit.github.io/qiskit-aer/stubs/qiskit_aer.AerSimulator.html
# https://github.com/LinkedInLearning/quantum-computing-fundamentals-2833097/blob/main/src/01_03_measurement/01_03_measurement_end.ipynb


from qiskit import (
    QuantumRegister,
    ClassicalRegister,
    QuantumCircuit,
    transpile,
)
from qiskit.qasm2 import dumps as qasm2_dumps
from qiskit.qasm3 import dumps as qasm3_dumps
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
from matplotlib import pyplot as plt

def main():
    qr = QuantumRegister(1) # Create a quantum register with 1 qubit
    cr = ClassicalRegister(1) # Create a classical register to store the result
    circuit = QuantumCircuit(qr, cr) # Create a quantum circuit
    circuit.h(0) # Apply a Hadamard gate to the qubit to create superposition
    circuit.measure(qr, cr) # Add a measurement operation to the circuit

    # print(circuit.draw(output="text")) # Plot the circuit as text

    # 1/ on classical register wire: "1" bit.
    # 0 on the connection: the target bit index "0".
    circuit.draw(output="mpl") # Plot the circuit
    plt.show(block=False)
    plt.pause(1)

    simulator = AerSimulator() # Simulator backend
    compiled_circuit = transpile(circuit, simulator) # Compile the circuit
    job = simulator.run(compiled_circuit, shots=10_000) # Execute the circuit

    # Show the compiled circuit in QASM formats
    print("QASM3 dump")
    print(qasm3_dumps(compiled_circuit))

    print("QASM2 dump")
    print(qasm2_dumps(compiled_circuit))

    result = job.result() # Get the result of the execution
    counts = result.get_counts(compiled_circuit)  # Get the measurement counts
    plot_histogram(counts) # Plot the histogram of the measurement results

    plt.show() # Display the plots; see the circuit and the result distribution

if __name__ == "__main__":
  main()
