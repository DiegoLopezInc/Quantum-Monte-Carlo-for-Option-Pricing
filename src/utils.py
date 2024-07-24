import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def black_scholes(S, K, T, r, sigma):
    """
    Calculate the Black-Scholes option price for a European call option.
    
    :param S: Current stock price
    :param K: Strike price
    :param T: Time to expiration (in years)
    :param r: Risk-free interest rate
    :param sigma: Volatility
    :return: Option price
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

def plot_results(classical_prices, quantum_prices, title):
    """
    Plot the distribution of option prices for classical and quantum simulations.
    
    :param classical_prices: List of option prices from classical simulation
    :param quantum_prices: List of option prices from quantum simulation
    :param title: Title for the plot
    """
    plt.figure(figsize=(10, 6))
    plt.hist(classical_prices, bins=30, alpha=0.5, label='Classical')
    plt.hist(quantum_prices, bins=30, alpha=0.5, label='Quantum')
    plt.title(title)
    plt.xlabel('Option Price')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()

def calculate_statistics(prices):
    """
    Calculate mean and standard deviation of option prices.
    
    :param prices: List of option prices
    :return: Mean and standard deviation
    """
    return np.mean(prices), np.std(prices)
