import numpy as np
from src.utils import black_scholes, plot_results, calculate_statistics
from src.quantum_circuit import generate_quantum_random_numbers

def classical_monte_carlo(S, K, T, r, sigma, num_simulations):
    """
    Perform classical Monte Carlo simulation for option pricing.
    
    :param S: Current stock price
    :param K: Strike price
    :param T: Time to expiration (in years)
    :param r: Risk-free interest rate
    :param sigma: Volatility
    :param num_simulations: Number of simulations to run
    :return: List of option prices
    """
    dt = T / 252  # Assuming 252 trading days in a year
    nudt = (r - 0.5 * sigma**2) * dt
    sidt = sigma * np.sqrt(dt)
    
    prices = []
    for _ in range(num_simulations):
        St = S
        for _ in range(252):
            epsilon = np.random.normal(0, 1)
            St *= np.exp(nudt + sidt * epsilon)
        
        option_price = max(St - K, 0)
        prices.append(np.exp(-r * T) * option_price)
    
    return prices

def quantum_monte_carlo(S, K, T, r, sigma, num_simulations):
    """
    Perform quantum Monte Carlo simulation for option pricing.
    
    :param S: Current stock price
    :param K: Strike price
    :param T: Time to expiration (in years)
    :param r: Risk-free interest rate
    :param sigma: Volatility
    :param num_simulations: Number of simulations to run
    :return: List of option prices
    """
    dt = T / 252  # Assuming 252 trading days in a year
    nudt = (r - 0.5 * sigma**2) * dt
    sidt = sigma * np.sqrt(dt)
    
    quantum_random_numbers = generate_quantum_random_numbers(num_simulations * 252, 10)
    
    prices = []
    for i in range(num_simulations):
        St = S
        for j in range(252):
            epsilon = np.sqrt(2) * np.erfinv(2 * quantum_random_numbers[i * 252 + j] - 1)
            St *= np.exp(nudt + sidt * epsilon)
        
        option_price = max(St - K, 0)
        prices.append(np.exp(-r * T) * option_price)
    
    return prices

def main():
    # Set option parameters
    S = 100  # Current stock price
    K = 100  # Strike price
    T = 1    # Time to expiration (in years)
    r = 0.05 # Risk-free interest rate
    sigma = 0.2  # Volatility
    num_simulations = 10000

    # Run classical Monte Carlo simulation
    classical_prices = classical_monte_carlo(S, K, T, r, sigma, num_simulations)

    # Run quantum Monte Carlo simulation
    quantum_prices = quantum_monte_carlo(S, K, T, r, sigma, num_simulations)

    # Calculate statistics
    classical_mean, classical_std = calculate_statistics(classical_prices)
    quantum_mean, quantum_std = calculate_statistics(quantum_prices)

    # Print results
    print(f"Classical Monte Carlo: Mean = {classical_mean:.4f}, Std Dev = {classical_std:.4f}")
    print(f"Quantum Monte Carlo: Mean = {quantum_mean:.4f}, Std Dev = {quantum_std:.4f}")

    # Calculate Black-Scholes price for comparison
    bs_price = black_scholes(S, K, T, r, sigma)
    print(f"Black-Scholes price: {bs_price:.4f}")

    # Plot results
    plot_results(classical_prices, quantum_prices, "Option Price Distribution: Classical vs Quantum")

if __name__ == "__main__":
    main()
