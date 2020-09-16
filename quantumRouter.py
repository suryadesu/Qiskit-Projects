#Circuit implementation of Quantum router
import numpy as np
from qiskit import(
  QuantumCircuit,
  execute,
  Aer)
import operator
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram

# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')

# Create a Quantum Circuit acting on the q register
circuit = QuantumCircuit(3, 3)

# Add a H gate on qubit 0
circuit.h(0)
circuit.h(1)
circuit.h(2)
circuit.s(0)
circuit.t(1)
circuit.t(0)
circuit.h(1)
circuit.s(0)
circuit.s(1)
circuit.cx(1, 2)
circuit.cx(0,2)
circuit.h(1)
circuit.tdg(2)
circuit.t(0)
circuit.t(1)
circuit.cx(1,2)
circuit.t(2)
circuit.cx(0,1)
circuit.cx(0,2)
circuit.tdg(1)
circuit.tdg(2)
circuit.cx(0,1)
circuit.cx(1,2)
circuit.t(2)
circuit.h(1)
circuit.cx(1,2)

# Map the quantum measurement to the classical bits
circuit.measure([0,1,2], [0,1,2])

# Execute the circuit on the qasm simulator
job = execute(circuit, simulator, shots=1000)

# Grab results from the job
result = job.result()

# Returns counts
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
plt.bar(counts.keys(),counts.values())

plt.show()
# Draw the circuit
# print(circuit)
circuit.draw(filename="quantumRouter.png")
circuit.draw()

