# Time Complexity Examples

def constant_time_example(arr):
    # O(1) - Constant Time: Accessing an element by index takes the same time regardless of input size
    return arr[0] if arr else None  # Returns the first element if the list is not empty


def linear_time_example(arr):
    # O(n) - Linear Time: Iterates through the entire list, taking time proportional to its size
    for item in arr:
        print(item)  # Prints each element in the array


def quadratic_time_example(arr):
    # O(n^2) - Quadratic Time: Nested loops result in a time complexity of n squared
    for i in arr:
        for j in arr:
            print(i, j)  # Prints all pairs of elements


# Space Complexity Examples

def space_constant_example():
    # O(1) - Constant Space: Uses a fixed amount of memory regardless of input size
    x = 10  # Single integer variable
    return x


def space_linear_example(n):
    # O(n) - Linear Space: Creates a list of size 'n', requiring memory proportional to 'n'
    arr = [i for i in range(n)]  # List comprehension to create an array of size n
    return arr


def space_quadratic_example(n):
    # O(n^2) - Quadratic Space: Creates an n x n matrix, requiring n squared space
    matrix = [[0] * n for _ in range(n)]  # 2D list (matrix) of size n x n
    return matrix


# Example usage
arr = [1, 2, 3, 4, 5]
constant_time_example(arr)
linear_time_example(arr)
quadratic_time_example(arr)

space_constant_example()
space_linear_example(5)
space_quadratic_example(5)
