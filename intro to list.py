# Creating a list
fruits = ['apple', 'banana', 'cherry', 'date']
print("Fruits List:", fruits)

# Accessing elements
print("First Fruit:", fruits[0])  # Indexing
print("Last Fruit:", fruits[-1])  # Negative Indexing

# Slicing a list
print("First two fruits:", fruits[:2])
print("Last two fruits:", fruits[-2:])

# Modifying elements
fruits[1] = 'blueberry'
print("Modified List:", fruits)

# Adding elements
fruits.append('elderberry')  # Append at the end
print("After Append:", fruits)

fruits.insert(2, 'fig')  # Insert at a specific position
print("After Insert:", fruits)

# Removing elements
fruits.remove('cherry')  # Remove by value
print("After Remove:", fruits)

popped_fruit = fruits.pop()  # Remove last element
print("Popped Fruit:", popped_fruit)
print("After Pop:", fruits)

# List comprehension
numbers = [x for x in range(1, 6)]  # Creates [1, 2, 3, 4, 5]
print("Numbers List:", numbers)

doubled = [x * 2 for x in numbers]  # Double each element
print("Doubled List:", doubled)

# Sorting a list
fruits.sort()  # Ascending order
print("Sorted List:", fruits)

fruits.sort(reverse=True)  # Descending order
print("Reverse Sorted List:", fruits)

# Checking existence
print("Is 'apple' in list?", 'apple' in fruits)
print("Is 'mango' in list?", 'mango' in fruits)

# Iterating through a list
for fruit in fruits:
    print("Fruit:", fruit)

# List length
print("Length of Fruits List:", len(fruits))

# Copying a list
fruits_copy = fruits.copy()
print("Copied List:", fruits_copy)
