import unittest
import numpy as np
from src.monte_carlo import classical_monte_carlo, quantum_monte_carlo

class TestMonteCarlo(unittest.TestCase):
    def setUp(self):
        self.S = 100
        self.K = 100
        self.T = 1
        self.r = 0.05
        self.sigma = 0.2
        self.num_simulations = 1000

    def test_classical_monte_carlo(self):
        prices = classical_monte_carlo(self.S, self.K, self.T, self.r, self.sigma, self.num_simulations)
        self.assertEqual(len(prices), self.num_simulations)
        self.assertTrue(all(price >= 0 for price in prices))

    def test_quantum_monte_carlo(self):
        prices = quantum_monte_carlo(self.S, self.K, self.T, self.r, self.sigma, self.num_simulations)
        self.assertEqual(len(prices), self.num_simulations)
        self.assertTrue(all(price >= 0 for price in prices))

    def test_monte_carlo_comparison(self):
        classical_prices = classical_monte_carlo(self.S, self.K, self.T, self.r, self.sigma, self.num_simulations)
        quantum_prices = quantum_monte_carlo(self.S, self.K, self.T, self.r, self.sigma, self.num_simulations)
        
        self.assertAlmostEqual(np.mean(classical_prices), np.mean(quantum_prices), delta=2)

if __name__ == '__main__':
    unittest.main()
