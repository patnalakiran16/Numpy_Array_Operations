import numpy as np

# Step 1: Create two NumPy arrays
array1 = np.array([10, 20, 30, 40, 50])
array2 = np.array([2, 4, 5, 8, 10])

# Step 2: Display the arrays
print("Array 1:", array1)
print("Array 2:", array2)

# Step 3: Check the shape of arrays
print("Shape of Array 1:", array1.shape)
print("Shape of Array 2:", array2.shape)

# Step 4: Perform mathematical operations
print("\nAddition:", array1 + array2)
print("Subtraction:", array1 - array2)
print("Multiplication:", array1 * array2)
print("Division:", array1 / array2)

# Step 5: Explanation of vectorization
print("\nVectorization:")
print("NumPy performs operations on all array elements directly.")
