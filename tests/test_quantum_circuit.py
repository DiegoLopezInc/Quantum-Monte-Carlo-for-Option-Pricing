import unittest
from src.quantum_circuit import create_qrng_circuit, generate_quantum_random_numbers

class TestQuantumCircuit(unittest.TestCase):
    def test_create_qrng_circuit(self):
        num_qubits = 5
        circuit = create_qrng_circuit(num_qubits)
        self.assertEqual(circuit.num_qubits, num_qubits)
        self.assertEqual(circuit.num_clbits, num_qubits)

    def test_generate_quantum_random_numbers(self):
        num_samples = 1000
        num_qubits = 8
        random_numbers = generate_quantum_random_numbers(num_samples, num_qubits)
        self.assertEqual(len(random_numbers), num_samples)
        self.assertTrue(all(0 <= num <= 1 for num in random_numbers))

if __name__ == '__main__':
    unittest.main()
