#Circuit implementation of phase estimation
import numpy as np
from qiskit import(
  QuantumCircuit,
  execute,
  ClassicalRegister, QuantumRegister,
  Aer)
import math
import matplotlib.pyplot as plt
import operator
from qiskit.visualization import plot_histogram
#Subroutine for qft
def qft(circ, q, n):
    for j in range(n):
        circ.h(q[j])
        for k in range(j+1,n):
            circ.cu1(math.pi/float(2**(k-j)), q[k], q[j])
#Subroutine for inverse qft or qft dagger
def qft_dagger(circ, q, n):
    for j in range(n):
        k = (n-1) - j
        for m in range(k):
            circ.cu1(-math.pi/float(2**(k-m)), q[k], q[m])
        circ.h(q[k])
#Circuit is designed by assigning respective gates to qubits
q2 = QuantumRegister(6, 'q') #an array of qubits
#First four contains the phase, last two are used as ancilla qubits
c2 = ClassicalRegister(4, 'c')
circuit = QuantumCircuit(6,4) #Circuit
simulator = Aer.get_backend('qasm_simulator')
circuit.h(q2[0])
circuit.h(q2[1]) #Hadamard
circuit.h(q2[2])
circuit.h(q2[3])

circuit.x(q2[4]) #CNOT
circuit.x(q2[5])

circuit.h(q2[5])
circuit.ccx(q2[3], q2[4], q2[5]) #Toffoli
circuit.h(q2[5])	
qft_dagger(circuit, q2, 4)
circuit.measure([q2[0],q2[1],q2[2],q2[3]],[c2[0],c2[1],c2[2],c2[3]]) #Measurement
circuit.draw(filename="phaseEstimation.png") #Uncomment to save the circuit as a png
# print(circuit) Uncomment to print circuit on terminal
job = execute(circuit, simulator, shots=3200) #Executes on the simulator

# Grab results from the job
result = job.result()

# Returns counts
counts = result.get_counts(circuit) #dictionary of state and its count
print(counts)
plt.bar(counts.keys(),counts.values()) #To plot the counts
plt.show()
m = max(counts.items(), key=operator.itemgetter(1))[0]
print(m) # The state with highest probability(count)
# Finding the phase int(m) = 2^n x phase
m = int(m, 2) 
phase = (m/16)
print(phase)
