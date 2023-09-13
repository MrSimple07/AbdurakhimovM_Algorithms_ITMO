import numpy as np
import timeit
import matplotlib.pyplot as plt

# Function to generate a random matrix of size n x n with non-negative elements
def generate_random_matrix(n):
    return np.random.rand(3, 3) * 100  # Adjust the scale (e.g., 100) for your desired range

# Function to calculate the matrix product of A and B
def matrix_product(A, B):
    return np.dot(A, B)

# Step 9: Perform Measurements for Different 'n' Values
n_values = list(range(1, 2001))
average_times_matrix_product = []

for n in n_values:
    A = generate_random_matrix(n)
    B = generate_random_matrix(n)
    time_matrix_product = timeit.timeit(lambda: matrix_product(A, B), number=1)
    average_times_matrix_product.append(time_matrix_product)

# Plotting: Average Execution Time Analysis for Matrix Multiplication
plt.figure(figsize=(12, 6))
plt.plot(n_values, average_times_matrix_product, label="Matrix Multiplication", marker='o', linestyle='-')
plt.xlabel("Matrix Size (n)")
plt.ylabel("Average Execution Time (seconds)")
plt.title("Matrix Multiplication Execution Time")
plt.grid(True)
plt.show()
