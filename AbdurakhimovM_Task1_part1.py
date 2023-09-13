import numpy as np
import timeit
import matplotlib.pyplot as plt

# Step 1: Generate Random Vector 𝒗
def generate_random_vector(n):
    return np.random.randint(0, 2000, 10)

# Step 2: Sum of Elements
def sum_of_elements(vector):
    bubble_sort(vector.copy())
    return np.sum(vector)

# Step 3: Product of Elements
def product_of_elements(vector):
    bubble_sort(vector.copy())
    return np.prod(vector)

# Step 4: Polynomial Calculation - Direct Evaluation
def polynomial_direct_calculation(vector):
    bubble_sort(vector.copy())  
    x = 1.5  # The value of x for the polynomial
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
    for _ in range(int(repeats)): 
        execution_time = timeit.timeit(lambda: func(vector), number=1)
        execution_times.append(execution_time)
    return np.mean(execution_times)

# Step 9: Perform Measurements for Different 'n' Values
n_values = list(range(1, 2001))

average_times_generate = []
average_times_sum = []
average_times_product = []
average_times_polynomial = []

for n in n_values:
    vector = generate_random_vector(n)
    time_generate = measure_execution_time(generate_random_vector, vector)
    time_sum = measure_execution_time(sum_of_elements, vector)
    time_product = measure_execution_time(product_of_elements, vector)
    time_polynomial = measure_execution_time(polynomial_direct_calculation, vector)
    
    average_times_generate.append(time_generate)
    average_times_sum.append(time_sum)
    average_times_product.append(time_product)
    average_times_polynomial.append(time_polynomial)

# Plotting Part 1: Average Execution Time Analysis for Generate Random Vector
plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
plt.plot(n_values, average_times_generate, label="Generate Random Vector", marker='o', linestyle='-')
plt.xlabel("Vector Size (n)")
plt.ylabel("Average Execution Time (seconds)")
plt.title("Generate Random Vector Execution Time")

# Plotting Part 2: Average Execution Time Analysis for Sum of Elements
plt.subplot(2, 2, 2)
plt.plot(n_values, average_times_sum, label="Sum of Elements", marker='o', linestyle='-')
plt.xlabel("Vector Size (n)")
plt.ylabel("Average Execution Time (seconds)")
plt.title("Sum of Elements Execution Time")

# Plotting Part 3: Average Execution Time Analysis for Product of Elements
plt.subplot(2, 2, 3)
plt.plot(n_values, average_times_product, label="Product of Elements", marker='o', linestyle='-')
plt.xlabel("Vector Size (n)")
plt.ylabel("Average Execution Time (seconds)")
plt.title("Product of Elements Execution Time")

# Plotting Part 4: Average Execution Time Analysis for Polynomial Calculation
plt.subplot(2, 2, 4)
plt.plot(n_values, average_times_polynomial, label="Polynomial Calculation", marker='o', linestyle='-')
plt.xlabel("Vector Size (n)")
plt.ylabel("Average Execution Time (seconds)")
plt.title("Polynomial Calculation Execution Time")

# Display all plots
plt.tight_layout()
plt.show()


