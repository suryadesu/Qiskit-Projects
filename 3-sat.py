#Solve 3-sat problem using Aqua
import numpy as np
from qiskit import(
  BasicAer,
  QuantumCircuit,
  execute,
  ClassicalRegister, QuantumRegister,
  Aer)
import math
import matplotlib.pyplot as plt
from qiskit.aqua import QuantumInstance, run_algorithm
from qiskit.aqua.algorithms import Grover
from qiskit.aqua.components.oracles import LogicalExpressionOracle, TruthTableOracle
from qiskit.compiler import transpile
input_3sat = ''' 
c example DIMACS-CNF 3-SAT
p cnf 3 1
1 -2 -3 0
'''
oracle = LogicalExpressionOracle(input_3sat)
# cir = oracle.construct_circuit()
# print(cir)
grover = Grover(oracle)
circuit = grover.construct_circuit()
circuit.draw(filename="3-sat.png")
# cir.draw(filename="3-sat_diffusion_operator.png")
# cir.draw(filename="circuit.png")
backend = BasicAer.get_backend('qasm_simulator')
quantum_instance = QuantumInstance(backend, shots=1024)
result = grover.run(quantum_instance)
print(result['result'])
plt.bar(result['measurement'].keys(),result['measurement'].values())
grover_compiled = transpile(result['circuit'], backend=backend, optimization_level=3)

plt.show()
