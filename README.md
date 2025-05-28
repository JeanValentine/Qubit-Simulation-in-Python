# Qubit Simulation in Python
**Project Overview:**
---
In this project we simulate the behavior of a single qubit using quantum mechanics and visualized measurements. This will allow us to see the outcomes through probability distributions after repeated trials. 

**What does this project do exactly?**
---
This simulation: 
* Initializes a qubit in the superposition state
  `|ψ⟩ = (1/√2)(|0⟩ + |1⟩)`

* Calculates the measurement probabilites for each basis state (|0> and |1>)

* Simulates one random measurement based on those probabilities

* Repeats this measurement **1000 times** to show the probabilistic nature of quantum mechanics

* Displays results using two plots:
    - A bar graph showing the theoretical probabilities
    - A histogram showing the **empirical measurement frequencies**

 ---

## What is a Qubit? 
---
Unlike a classical bit (which is either 0 or 1), a **qubit** can be in a superposition of both: 
`|ψ⟩ = α|0⟩ + β|1⟩
where |α|² + |β|² = 1`

Upon measurement, the qubit will **collapse** to one of the basis states (|0> or |1>) with probabilities: 
`P(0) = |α|²
P(1) = |β|²`

# How it works (Step-by-Step) 

## Defining Basis Sates 
We define the classical basis states using Numpy arrays: 

```python 
zero = np.array([[1], [0]], dtype=complex) # |0>
one = np.array([[0], [1]], dtype=complex) # |1>

```
## Create in Superposition 
We create the equal superposition state as such: 
```python
alpha = 1 / np.sqrt(2)
beta = 1 / np.sqrt(2)
psi = alpha * zero + beta * one
```
This means we should expect: 
* P(0) = 0.5
* P(1) = 0.5

## Calculating Probabilities 
```python
prob_0 = np.abs(psi[0, 0])**2
prob_1 = np.abs(psi[1, 0])**2
```
These reflect the theoretical values from quantum mechanics. 

## Simulate Measurement
We simulate a single quantum measurement here: 
```python
outcome = np.random.choice([0, 1], p=[prob_0, prob_1])
```
Each time you run the code, you'll randomly get either |0> or |1>

## Run Many Trials (1000 Times)
To demostrate the randomness statistically we can use: 
```python
result = np.random.choice([0, 1]. size = 1000, p=[prob_0, prob_1])
```
Then we plot a histogram to show the results approximate 50/50 over many trials. 

# Examples: 


# How to Run?
Make sure you have python and the following libraries installed: 
<pre> pip install numpy matplotlib</pre>

Then run: 
<pre> python Qubit_Simulation.py</pre>

