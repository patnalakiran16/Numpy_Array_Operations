NumPy Array Operations

Project Description

This project demonstrates basic mathematical operations using NumPy arrays in Python. Two NumPy arrays are created, and addition, subtraction, multiplication, and division operations are performed on them.

Objective

To understand NumPy vectorization and perform mathematical operations efficiently on arrays.

Technologies Used

- Python
- NumPy
- Jupyter Notebook

Operations Performed

1. Created two NumPy arrays using "np.array()".
2. Checked the shape of both arrays.
3. Performed addition of two arrays.
4. Performed subtraction of two arrays.
5. Performed multiplication of two arrays.
6. Performed division of two arrays.
7. Explained vectorization in NumPy.

Python Code

import numpy as np

array1 = np.array([10, 20, 30, 40, 50])
array2 = np.array([2, 4, 5, 8, 10])

print("Array 1:", array1)
print("Array 2:", array2)

print("Shape of Array 1:", array1.shape)
print("Shape of Array 2:", array2.shape)

print("\nAddition:", array1 + array2)
print("Subtraction:", array1 - array2)
print("Multiplication:", array1 * array2)
print("Division:", array1 / array2)

print("\nVectorization:")
print("NumPy performs operations on all array elements directly.")

Expected Output

Array 1: [10 20 30 40 50]
Array 2: [ 2  4  5  8 10]
Shape of Array 1: (5,)
Shape of Array 2: (5,)

Addition: [12 24 35 48 60]
Subtraction: [ 8 16 25 32 40]
Multiplication: [ 20  80 150 320 500]
Division: [5. 5. 6. 5. 5.]

Vectorization:
NumPy performs operations on all array elements directly.

What Is Vectorization?

Vectorization is a technique that allows mathematical operations to be performed on entire arrays without using explicit loops. It makes code shorter, simpler, and often faster for numerical calculations.

How to Run

1. Install Python on your system.
2. Install NumPy using the command:
   "pip install numpy"
3. Open Jupyter Notebook.
4. Copy the Python code into a cell.
5. Run the cell and observe the output.

Conclusion

This project helped me understand how NumPy arrays work and how to perform mathematical operations efficiently using vectorization in Python.

Author

Kiran Patnala