import unittest
import numpy as np
from src.utils import black_scholes, calculate_statistics

class TestUtils(unittest.TestCase):
    def test_black_scholes(self):
        S = 100
        K = 100
        T = 1
        r = 0.05
        sigma = 0.2
        expected_price = 10.45  # Approximate value
        calculated_price = black_scholes(S, K, T, r, sigma)
        self.assertAlmostEqual(calculated_price, expected_price, places=2)

    def test_calculate_statistics(self):
        prices = [10, 12, 15, 11, 13]
        mean, std = calculate_statistics(prices)
        self.assertAlmostEqual(mean, np.mean(prices), places=6)
        self.assertAlmostEqual(std, np.std(prices), places=6)

if __name__ == '__main__':
    unittest.main()
