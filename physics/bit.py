from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram
from qiskit.providers.aer import AerSimulator

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0,1], [0,1])

simulator = AerSimulator()

job = execute(qc, simulator, shots=1024)
result = job.result()

counts = result.get_counts(qc)
print(counts)
plot_histogram(counts)
