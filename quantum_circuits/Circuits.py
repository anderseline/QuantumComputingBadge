from qiskit import visualization, QuantumCircuit, QuantumRegister, ClassicalRegister, Aer, execute, assemble
from math import pi, sqrt

def getBloch(quantumC, backend):
    return visualization.plot_bloch_multivector(
        execute(quantumC, backend).result().get_statevector()
    )

def stateGenerator(state):
    state = state[::-1]
    current = int(state, 2)
    newState = [0 for i in range(0, 2**(len(state)))]
    newState[current] = 1
    return newState

def getMeasure(quantumC, n, circ, backend):
    measures = []
    for i in range(0, n):
        outcome = execute(circ, backend).result()
        hist = outcome.get_counts()
        for i in hist.keys():
            measures.append(i)
        return measures