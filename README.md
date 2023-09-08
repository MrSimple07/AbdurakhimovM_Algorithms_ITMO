# AbdurakhimovM_Task1
Goal
The main aim here is to dive into various computer algorithms and see how fast or slow they are in real-life scenarios. We want to understand if these algorithms speed up or slow down when dealing with bigger tasks.

Formulation of the problem
When we use computers, we want things to happen quickly. But different computer tricks (called algorithms) have different speeds. Some work well for small tasks, others for bigger ones. This project is all about testing these tricks. We're going to try them out with different types of problems, and for each one, we'll see how long it takes. Then, we'll make some cool charts to show how these tricks behave as the problems get larger. This will help us understand which tricks are speedy and which ones are a bit sluggish.

Brief theoretical part
I. We're curious about several things, like generating random lists of numbers, adding them up, multiplying them, and even solving some math problems. We want to see how these tasks behave when we make the lists longer.
Generating Random Lists: First, we create lists filled with random numbers. These lists can be as short as you like or as long as 2000 numbers.
The Constant Function: This task is super easy. It's like saying "Hello!" once and not doing anything else. It takes the same amount of time no matter how long the list is.
Summing Up the Numbers: Here, we add up all the numbers in the list. If we have a longer list, it takes more time because we have to go through each number.
Multiplying the Numbers: Similar to the addition, we multiply all the numbers in the list. Again, the time it takes grows with the length of the list.
Polynomial Math: We're doing some fancy math here. Imagine we have a special formula, and we want to find the answer using our list of numbers. The longer the list, the more time it takes because we have to go through each number.
Bubble Sort: This is like arranging a deck of cards from smallest to largest. If you have more cards, it takes longer because you need to compare and swap them more.
Quick Sort: Another way to arrange cards, but faster than bubble sort, especially when you have a lot of them.
Timsort: Yet another card-sorting technique, but this one is super smart and efficient. It's like quick sort but even better.
II. Matrix Operations
Making Random Matrices: We create random grids filled with numbers. The grids can be small or large, depending on what we want.
Matrix Multiplication: We want to find out what happens when we multiply these grids together. The more rows and columns we have, the longer it takes.
By doing all these tasks and timing them, we can figure out how quickly the computer works for different things and compare them when we change the size of what we're working with. It's like experimenting with different recipes in the kitchen and seeing which one takes more time when you're cooking for a big party!
III. Data Structures and Design Techniques in the Algorithms:

Generating Random Lists:
Data Structure: We use a simple array or list to store the random numbers.
Design Technique: This task doesn't involve any complex algorithms or data structures. It's straightforward and involves generating random numbers one by one and storing them in the list.
The Constant Function:
Data Structure: No specific data structure is needed for this task.
Design Technique: It's the simplest task, like saying "Hello World" in programming. The execution time remains constant, irrespective of list size.
Summing Up the Numbers:
Data Structure: We use an array or list to store the numbers.
Design Technique: This task utilizes a loop to iterate through the list and accumulate the numbers. The time it takes grows linearly with the list size.
Multiplying the Numbers:
Data Structure: Similar to the sum task, we use an array or list.
Design Technique: It employs a loop to traverse the list and perform multiplications. Like addition, the execution time increases linearly with list size.
Polynomial Math:
Data Structure: We use an array to store coefficients and a variable for the x value.
Design Technique: This task involves polynomial evaluation either directly or using Horner's method. It uses loops to calculate each term and sum them. Execution time increases with list size due to the loop iterations.
Bubble Sort:
Data Structure: Again, we use an array or list to store elements.
Design Technique: Bubble sort is a basic sorting algorithm that compares and swaps adjacent elements until the list is sorted. It has nested loops, making it less efficient for large lists.
Quick Sort:
Data Structure: Utilizes an array or list.
Design Technique: Quick sort is a more efficient sorting algorithm than bubble sort. It uses divide-and-conquer, recursion, and pivot selection techniques to sort the list faster, especially for larger lists.
Timsort:
Data Structure: Same as above, it operates on arrays or lists.
Design Technique: Timsort is a hybrid sorting algorithm that combines merge sort and insertion sort. It adapts to the data's characteristics and performs well in various scenarios, making it suitable for real-world sorting tasks.

Results
In this section, we present the empirical results of our study, which involved the execution of various algorithms on datasets of different sizes. These results are instrumental in understanding how each algorithm's performance scales with the size of the input data.

The "Generate Random Vector" algorithm exhibits relatively constant execution time since it only generates random numbers. "Sum of Elements" and "Product of Elements" show linear growth in execution time with input size, which is expected as they perform operations on all elements of the vector. "Polynomial Calculation" and "Bubble Sort" demonstrate significant increases in execution time with larger inputs, especially bubble sort, which is a less efficient sorting algorithm.

The "Generate Random Matrix" operation exhibits an increasing execution time with larger input sizes, as expected when generating more elements. "Matrix Product" execution time grows significantly with input size. Matrix multiplication is a computationally intensive task, and the execution time scales with the cube of the input size.

The results obtained from our empirical analysis underscore the crucial relationship between algorithmic performance and input data size. Algorithms with theoretically lower time complexities, such as constant function evaluation, summation, and product of elements, indeed displayed flat or linear growth in execution time as expected. Conversely, algorithms like Bubble Sort exemplify the repercussions of higher time complexities when handling substantial datasets. Furthermore, the superiority of certain algorithms, such as Quick Sort and Horner's method, in terms of execution time is evident. These findings reiterate the importance of algorithm selection, as they illustrate how more efficient algorithms can significantly reduce computational time, especially when processing extensive datasets.

Conclusions
In conclusion, our study aimed to understand algorithmic time complexity practically. Our key findings reveal the significance of algorithm selection in data processing:
Efficiency is critical: Algorithms with low theoretical time complexities are essential for handling large datasets. The choice matters: Opting for efficient algorithms like Quick Sort and Horner's method drastically reduces computation time for extensive data. Timsort's adaptability: Timsort's adaptable behavior, sometimes linear, highlights the diverse behavior of algorithms in different scenarios. Bridging theory and practice: Our results consistently align with theoretical expectations, providing practical guidance for algorithm selection. Practical relevance: These insights are invaluable for developers and data scientists, assisting them in selecting the right algorithms for specific tasks and datasets. In summary, our study successfully explored algorithmic time complexity in a practical context, providing practical insights that can benefit professionals in computer science and data analysis.

