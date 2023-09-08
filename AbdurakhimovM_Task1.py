import numpy as np
import timeit
import matplotlib.pyplot as plt

# Step 1: Generate Random Vector 𝒗
def generate_random_vector(n):
    return np.random.randint(1, 2001, 100)

# Step 2: Sum of Elements
def sum_of_elements(vector):
    bubble_sort(vector.copy())
    return np.sum(vector)

# Step 3: Product of Elements
def product_of_elements(vector):
    bubble_sort(vector.copy())  
    return np.prod(vector)

# Step 4: Polynomial Calculation - Direct Evaluation
def polynomial_direct_calculation(vector, x):
    bubble_sort(vector.copy()) 
    result = 0
    for i, coeff in enumerate(vector):
        result += coeff * (x ** i)
    return result

# Step 5: Bubble Sort Algorithm
def bubble_sort(vector):
    n = len(vector)
    for i in range(n):
        for j in range(0, n-i-1):
            if vector[j] > vector[j+1]:
                vector[j], vector[j+1] = vector[j+1], vector[j]

# Step 8: Measure Execution Time
def measure_execution_time(func, vector, repeats=5):
    execution_times = []
    for _ in range(repeats):
        execution_time = timeit.timeit(lambda: func(vector), number=1)
        execution_times.append(execution_time)
    return np.mean(execution_times)

# Function to generate a random matrix of size n x n with non-negative elements
def generate_random_matrix(n):
    return np.random.rand(n, n) * 100

# Function to calculate the matrix product of A and B
def matrix_product(A, B):
    return np.dot(A, B)

# Step 9: Perform Measurements for Different 'n' Values
n_values = list(range(1, 2001))
average_times_generate = []
average_times_sum = []
average_times_product = []
average_times_polynomial = []
average_times_bubble = []
average_times_matrix_generate = []
average_times_matrix_product = []

# Define a constant value for x
x = 1.5

for n in n_values:
    vector = generate_random_vector(n)
    time_generate = measure_execution_time(generate_random_vector, vector)
    time_sum = measure_execution_time(sum_of_elements, vector)
    time_product = measure_execution_time(product_of_elements, vector)
    time_polynomial = measure_execution_time(lambda v: polynomial_direct_calculation(v, x), vector, repeats=1)
    time_bubble = measure_execution_time(bubble_sort, vector)
    
    A = generate_random_matrix(n)
    B = generate_random_matrix(n)
    time_matrix_generate = measure_execution_time(generate_random_matrix, n)
    time_matrix_product = timeit.timeit(lambda: matrix_product(A, B), number=1)
    
    average_times_generate.append(time_generate)
    average_times_sum.append(time_sum)
    average_times_product.append(time_product)
    average_times_polynomial.append(time_polynomial)
    average_times_bubble.append(time_bubble)
    
    average_times_matrix_generate.append(time_matrix_generate)
    average_times_matrix_product.append(time_matrix_product)

# Step 10: Create two plots
plt.figure(figsize=(12, 6))

# Plot 1: Algorithms
plt.subplot(1, 2, 1)
plt.plot(n_values, average_times_generate, label="Generate Random Vector", marker='o', linestyle='-')
plt.plot(n_values, average_times_sum, label="Sum of Elements (with Bubble Sort)", marker='o', linestyle='-')
plt.plot(n_values, average_times_product, label="Product of Elements (with Bubble Sort)", marker='o', linestyle='-')
plt.plot(n_values, average_times_polynomial, label="Polynomial Calculation (with Bubble Sort)", marker='o', linestyle='-')
plt.plot(n_values, average_times_bubble, label="Bubble Sort", marker='o', linestyle='-')
plt.xlabel("Size (n)")
plt.ylabel("Average Execution Time (seconds)")
plt.title("Algorithms Execution Time Analysis")
plt.legend()
plt.grid(True)

# Plot 2: Matrix Operations
plt.subplot(1, 2, 2)
plt.plot(n_values, average_times_matrix_generate, label="Generate Random Matrix", marker='o', linestyle='-')
plt.plot(n_values, average_times_matrix_product, label="Matrix Product", marker='o', linestyle='-')
plt.xlabel("Size (n)")
plt.ylabel("Average Execution Time (seconds)")
plt.title("Matrix Operations Execution Time Analysis")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
