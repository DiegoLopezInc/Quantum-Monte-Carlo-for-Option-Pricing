## Quantum Monte Carlo for Option Pricing

### Project Overview
This project explores the application of quantum computing to financial engineering by implementing a quantum Monte Carlo simulation for option pricing. It compares the results of classical and quantum Monte Carlo methods for pricing European call options.

### Goals
* Understand the fundamentals of option pricing and Monte Carlo simulation.
* Explore the potential of quantum computing for financial applications.
* Implement a basic quantum circuit for random number generation.
* Compare quantum and classical Monte Carlo results for option pricing.

### Methodology
1. **Classical Option Pricing:** Implement a classical Monte Carlo simulation for a call option.
2. **Quantum Random Number Generation:** Create a quantum circuit to generate random numbers using a quantum random number generator (QRNG).
3. **Quantum Monte Carlo Simulation:** Modify the classical simulation to use quantum-generated random numbers.
4. **Comparison:** Compare the results of both simulations and the Black-Scholes model.

### Code Structure
* **quantum_circuit.py:** Contains the quantum circuit for random number generation.
* **monte_carlo.py:** Implements both classical and quantum Monte Carlo simulations.
* **utils.py:** Helper functions for data processing, visualization, and Black-Scholes calculation.

### Dependencies
* Qiskit
* NumPy
* Matplotlib
* SciPy

### Usage
1. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Run the `monte_carlo.py` script:
   ```
   python src/monte_carlo.py
   ```
3. Adjust parameters as needed in the `main()` function of `monte_carlo.py` (e.g., number of simulations, option parameters).

### Results
The script will output:
1. Mean and standard deviation of option prices for both classical and quantum Monte Carlo simulations.
2. The Black-Scholes price for comparison.
3. A histogram comparing the distribution of option prices from classical and quantum simulations.

### Future Work
* Explore different option types (e.g., American, exotic).
* Incorporate quantum machine learning techniques.
* Optimize the quantum circuit for performance.
* Implement more sophisticated pricing models and compare their performance.

### Acknowledgements
* Qiskit for quantum computing framework
* Black-Scholes model for option pricing