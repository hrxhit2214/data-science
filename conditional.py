# If-Else Statements

# Basic If-Else Statement
x = 10
if x > 5:
    print("x is greater than 5")  # This will be printed since x is 10
else:
    print("x is less than or equal to 5")

# Elif (Else If) Statement
y = 15
if y > 20:
    print("y is greater than 20")
elif y > 10:
    print("y is greater than 10 but less than or equal to 20")  # This will be printed because y is 15
else:
    print("y is 10 or less")

# Nested If-Else
z = 30
if z > 10:
    if z > 20:
        print("z is greater than 20")  # This will be printed
    else:
        print("z is greater than 10 but less than or equal to 20")
else:
    print("z is 10 or less")

# Logical Operators (and, or, not)

# Using 'and' operator
a = 5
b = 10
if a > 0 and b > 5:
    print("Both a and b are positive and b is greater than 5")  # This will be printed

# Using 'or' operator
c = -1
d = 8
if c > 0 or d > 5:
    print("At least one of c or d is greater than 0 or d is greater than 5")  # This will be printed

# Using 'not' operator
e = 0
if not e:
    print("e is falsy")  # This will be printed because 0 is considered falsy in Python

# Ternary Operator (One-line If-Else)
f = 8
result = "Even" if f % 2 == 0 else "Odd"
print("f is:", result)  # This will print "Even" because 8 is even

# Checking Multiple Conditions
g = 7
if g % 2 == 0:
    print("g is even")
elif g % 3 == 0:
    print("g is divisible by 3")  # This will be printed since 7 is divisible by 3
else:
    print("g is neither even nor divisible by 3")

# Chained Conditions (Multiple conditions with comparison operators)
h = 12
if 5 < h <= 15:
    print("h is between 5 and 15")  # This will be printed because h is 12

# Using 'in' operator with condition
fruit = "apple"
if fruit in ["apple", "banana", "cherry"]:
    print(f"{fruit} is in the list of fruits")  # This will be printed
else:
    print(f"{fruit} is not in the list of fruits")
