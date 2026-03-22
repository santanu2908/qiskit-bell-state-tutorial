from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

# Step 1: Create a quantum circuit with 2 qubits and 2 classical bits
qc = QuantumCircuit(2, 2)

# Step 2: Apply a Hadamard gate to qubit 0 (superposition)
qc.h(0)

# Step 3: Apply a CNOT gate (entangle qubit 0 and qubit 1)
qc.cx(0, 1)

# Step 4: Measure both qubits
# The first argument is the list of qubits to measure, and the second argument is the list of classical bits to store the results
# Here, we measure qubit 0 into classical bit 0 and qubit 1 into classical bit 1
# This will allow us to see the entangled state of the two qubits when we run the circuit.
# The expected result is that we will get either '00' or '11' with equal probability, since the qubits are entangled in a Bell state.
# The measurement will collapse the quantum state into one of the basis states, and we will see the correlation between the two qubits in the results.
# For example, if we measure '00', it means both qubits are in the state |0⟩, and if we measure '11', it means both qubits are in the state |1⟩. We should not see '01' or '10' because of the entanglement.
# qc.measure([qubit_0, qubit_1], [classical_bit_0, classical_bit_1])
qc.measure([0, 1], [0, 1])

# Step 5: Draw the circuit
print(qc.draw(output='text', fold=-1))

# Step 6: Simulate and get results
sampler = StatevectorSampler()
job = sampler.run([qc], shots=1000)
result = job.result()
counts = result[0].data.c.get_counts()

print(counts)
