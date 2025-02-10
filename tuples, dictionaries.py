
# Tuples, Sets & Dictionaries ka code

# 1. Tuple banana
my_tuple = (1, 2, 3, 4, 5)  # Tuple ek immutable collection hai
print(my_tuple)  # Output: (1, 2, 3, 4, 5)

# Tuple elements ko access 
print(my_tuple[0])  # Pehla element
print(my_tuple[-1])  # Aakhri element

# Tuple unpacking
a, b, c, d, e = my_tuple  # Multiple variables ko values assign 
print(a, b, c, d, e)  # Output: 1 2 3 4 5

# 2. Set banana
my_set = {1, 2, 3, 4, 5}  # Set ek unordered collection hai unique elements ka
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Set mein elements add 
my_set.add(6)  # Ek element add 
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Set se elements remove 
my_set.remove(3)  # Specific element remove 
print(my_set)  # Output: {1, 2, 4, 5, 6}

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))  # Dono sets ko combine : {1, 2, 3, 4, 5}
print(set1.intersection(set2))  # Common elements: {3}
print(set1.difference(set2))  # Elements jo set1 mein hain but set2 mein nahi: {1, 2}

# 3. Dictionary banana
my_dict = {"name": "Alice", "age": 25, "city": "New York"}  # Dictionary key-value pairs store karta hai
print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Dictionary values ko access 
print(my_dict["name"])  # Output: Alice
print(my_dict.get("age"))  # Output: 25

# Values ko add aur update 
my_dict["age"] = 26  # Age update 
my_dict["gender"] = "Female"  # Naya key-value pair add 
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'gender': 'Female'}

# Ek key-value pair remove 
del my_dict["city"]
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'gender': 'Female'}

# Dictionary methods
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'gender'])
print(my_dict.values())  # Output: dict_values(['Alice', 26, 'Female'])
print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 26), ('gender', 'Female')])
