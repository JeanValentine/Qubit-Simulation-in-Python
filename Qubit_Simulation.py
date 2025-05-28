#Qubit_simulation.py
import numpy as np 
import matplotlib.pyplot as plt

#Defining the base states |0> and |1>
zero = np.array([[1], [0]], dtype=complex)
one = np.array([[0], [1]], dtype=complex)

#now create a superposition state: (|0> + |1>)/sqrt(2)
alpha = 1/np.sqrt(2)
beta = 1/np.sqrt(2)
psi = alpha * zero + beta * one

print("Initial state |psi>:\n", psi)

#apply the Hadamard gate if you wish to make it deterministic. 
#we are already in a 50/50 superposition here, so we can skip this step. 

#H = (1 / np.sqrt(2)) * np.array([[1, 1],
#                                 [1, -1]])
#psi_after_H = H @ psi
#print("\nAfter Hadamard gate:\n", psi_after_H)

#Measure probabilities
prob_0 = np.abs(psi[0, 0])**2
prob_1 = np.abs(psi[1, 0])**2

print("\nMeasurement probabilities:")
print("P(0) =", prob_0)
print("P(1) =", prob_1)

#now simulate the actual measurement
outcome = np.random.choice([0, 1], p=[prob_0, prob_1])
print("\nSimulated measurement result:", outcome)

#visualize the result
plt.bar(['|0>', '|1>'], [prob_0, prob_1], color=['blue', 'orange'])
plt.title("Qubit Measurement Probabilities")
plt.ylabel("Probability")
plt.xlabel("Qubit States")
plt.ylim(0, 1)
plt.axhline(y=0.5, color='gray', linestyle='--', linewidth=0.5)
plt.show()

#Simulating trials and plotting them on a histogram

trial = 1000
results = np.random.choice([0, 1], size=trial, p=[prob_0, prob_1])

plt.hist(results, bins=[-0.5, 0.5, 1.5], density=True, alpha=0.7, color='purple', edgecolor='black')
plt.title(f"Simulated Qubit Measurements over {trial} Trials")
plt.xlabel("Measurement Outcome ")
plt.ylabel("Frequency")
plt.xticks([0, 1], ['|0>', '|1>'])
plt.axhline(y=prob_0, color='blue', linestyle='--', linewidth=0.5, label='P(0)')
plt.axhline(y=prob_1, color='orange', linestyle='--', linewidth=0.5, label='P(1)')
plt.legend()
plt.show()
