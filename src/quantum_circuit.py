from qiskit import QuantumCircuit, Aer, execute

def create_qrng_circuit(num_qubits):
    """
    Create a quantum circuit for random number generation.
    
    :param num_qubits: Number of qubits to use
    :return: Quantum circuit
    """
    circuit = QuantumCircuit(num_qubits, num_qubits)
    circuit.h(range(num_qubits))
    circuit.measure(range(num_qubits), range(num_qubits))
    return circuit

def generate_quantum_random_numbers(num_samples, num_qubits):
    """
    Generate random numbers using a quantum circuit.
    
    :param num_samples: Number of random numbers to generate
    :param num_qubits: Number of qubits to use
    :return: List of random numbers between 0 and 1
    """
    circuit = create_qrng_circuit(num_qubits)
    backend = Aer.get_backend('qasm_simulator')
    job = execute(circuit, backend, shots=num_samples)
    result = job.result().get_counts()
    
    max_value = 2**num_qubits - 1
    random_numbers = [int(outcome, 2) / max_value for outcome in result.keys()]
    
    return random_numbers
