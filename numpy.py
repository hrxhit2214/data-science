# Importing NumPy
import numpy as np

# Creating a NumPy array from a list
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)

# Checking the type of the array
print("Type:", type(arr))

# Creating a 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr2d)

# Checking the shape and size of the array
print("Shape:", arr2d.shape)
print("Size:", arr2d.size)

# Creating arrays with specific values
zeros_arr = np.zeros((3, 3))  # 3x3 array of zeros
ones_arr = np.ones((2, 4))  # 2x4 array of ones
full_arr = np.full((2, 2), 7)  # 2x2 array filled with 7

print("Zeros Array:\n", zeros_arr)
print("Ones Array:\n", ones_arr)
print("Full Array:\n", full_arr)

# Creating an array with a range of numbers
range_arr = np.arange(0, 10, 2)  # Start at 0, end before 10, step of 2
print("Range Array:", range_arr)

# Creating an array with evenly spaced values
linspace_arr = np.linspace(0, 1, 5)  # 5 values from 0 to 1
print("Linspace Array:", linspace_arr)

# Creating an identity matrix
identity_matrix = np.eye(3)  # 3x3 identity matrix
print("Identity Matrix:\n", identity_matrix)

# Generating random numbers
random_arr = np.random.rand(3, 3)  # 3x3 array with random values between 0 and 1
randint_arr = np.random.randint(1, 10, (2, 2))  # 2x2 array with random integers from 1 to 9

print("Random Array:\n", random_arr)
print("Random Integer Array:\n", randint_arr)

# Accessing elements in an array
print("Element at index 2:", arr[2])  # Accessing a single element
print("Slicing array:", arr[1:4])  # Slicing from index 1 to 3

# Accessing elements in a 2D array
print("Element at (1,2):", arr2d[1, 2])  # Accessing row 1, column 2

# Boolean masking
bool_mask = arr > 2  # Returns a boolean array
print("Boolean Mask:", bool_mask)
filtered_arr = arr[arr > 2]  # Filters elements greater than 2
print("Filtered Array:", filtered_arr)

# Basic arithmetic operations
arr_sum = arr + 5  # Adds 5 to each element
arr_prod = arr * 2  # Multiplies each element by 2
arr_square = arr ** 2  # Squares each element

print("Sum Array:", arr_sum)
print("Product Array:", arr_prod)
print("Square Array:", arr_square)

# Matrix operations
dot_product = np.dot(arr2d, arr2d.T)  # Matrix multiplication
print("Dot Product:\n", dot_product)

# Aggregation functions
print("Sum:", arr.sum())
print("Mean:", arr.mean())
print("Max:", arr.max())
print("Min:", arr.min())

# Reshaping an array
reshaped_arr = np.reshape(arr2d, (3, 2))  # Changing shape to 3x2
print("Reshaped Array:\n", reshaped_arr)

# Stacking arrays
stacked_arr = np.vstack((arr, arr))  # Stacking vertically
hstacked_arr = np.hstack((arr, arr))  # Stacking horizontally

print("Vertically Stacked Array:\n", stacked_arr)
print("Horizontally Stacked Array:\n", hstacked_arr)

# Splitting arrays
split_arr = np.array_split(arr, 2)  # Splitting into 2 parts
print("Split Arrays:", split_arr)

# Transposing a matrix
transposed_arr = arr2d.T
print("Transposed Array:\n", transposed_arr)

# Finding unique elements in an array
unique_elements = np.unique(arr2d)
print("Unique Elements:", unique_elements)

# Sorting an array
sorted_arr = np.sort(arr)
print("Sorted Array:", sorted_arr)

# Concatenating arrays
concat_arr = np.concatenate((arr, arr))
print("Concatenated Array:", concat_arr)

# Broadcasting example
broadcast_arr = arr + np.array([10])  # Adding a scalar (broadcasting)
print("Broadcasted Array:", broadcast_arr)

# Finding index of max and min values
max_index = np.argmax(arr)
min_index = np.argmin(arr)

print("Index of Max Element:", max_index)
print("Index of Min Element:", min_index)

# Copying an array
copied_arr = arr.copy()
print("Copied Array:", copied_arr)

# Conditional replacement
modified_arr = np.where(arr > 3, 100, arr)  # Replace values >3 with 100
print("Modified Array:", modified_arr)

# Flattening an array
flattened_arr = arr2d.flatten()
print("Flattened Array:", flattened_arr)

# Saving and loading arrays
np.save('saved_array.npy', arr)
loaded_arr = np.load('saved_array.npy')

print("Loaded Array:", loaded_arr)
