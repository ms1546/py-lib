import numpy as np
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
from qiskit.quantum_info import Statevector

def one_dimensional_quantum_walk(steps, initial_position=0):
    # 回路
    qc = QuantumCircuit(steps + 1, steps + 1)

    qc.h(0)
    if initial_position != 0:
        qc.x(initial_position)

    # 量子ウォーク
    for t in range(steps):
        qc.h(0)
        for i in range(1, steps + 1):
            qc.cx(0, i)
    qc.measure(range(steps + 1), range(steps + 1))

    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, simulator, shots=1000).result()
    counts = result.get_counts(qc)
    return counts

steps = 5
result = one_dimensional_quantum_walk(steps)
plot_histogram(result)
