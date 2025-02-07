# Python mein strings aur functions ka introduction

# Ek string ek sequence hota hai characters ka jo quotes (' ya ") ke andar likha jata hai.
# Yeh immutable hota hai, matlab ek baar create hone ke baad isme changes nahi kar sakte.

# String ka declaration
a = "Hello, World!"  # Double quotes ka use
b = 'Python Programming'  # Single quotes ka use
print(a)
print(b)

# Multiline string triple quotes (''' ya """) se likha jata hai
c = '''Yeh ek
multiline string hai.'''
print(c)

# String indexing aur slicing
s = "Python"
print(s[0])  # 'P' - Indexing (0-based index hota hai)
print(s[-1])  # 'n' - Negative indexing last se count karta hai
print(s[0:4])  # 'Pyth' - Slicing, yeh 0 se 3 tak lega (4 exclude hota hai)
print(s[:4])  # 'Pyth' - Starting index default 0 hota hai
print(s[2:])  # 'thon' - End index default last hota hai

# Strings immutable hote hain
# s[0] = 'J'  # Yeh error dega kyunki hum strings modify nahi kar sakte

# String concatenation aur repetition
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)  # Concatenation (Do strings ko jodna)
print(s1 * 3)  # String repetition

# String methods
string = "  Python Programming  "
print(string.lower())  # Lowercase mein convert karega
print(string.upper())  # Uppercase mein convert karega
print(string.strip())  # Leading aur trailing spaces hata dega
print(string.replace("Python", "Java"))  # Replace karega
print(string.split())  # Default space ke basis pe split karega

# String ka length pata karne ke liye len() function use hota hai
print(len(string))

# String formatting
name = "Rahul"
age = 20
print(f"Mera naam {name} hai aur meri umar {age} saal hai.")  # f-string method
print("Mera naam {} hai aur meri umar {} saal hai.".format(name, age))  # format() method

# Functions ka introduction
# Function ek block hota hai jo specific task perform karta hai

def greet(name):  # Function definition
    """Yeh function ek naam leta hai aur uska greeting return karta hai"""
    return "Namaste, " + name + "!"

print(greet("Amit"))  # Function call

# Function with default parameter
def add(a, b=5):  # b default 5 hoga agar user koi value na de
    return a + b

print(add(10))  # 10 + 5 = 15
print(add(10, 20))  # 10 + 20 = 30

# Function with multiple return values
def calculate(a, b):
    sum = a + b
    diff = a - b
    return sum, diff  # Multiple values return kar raha hai

result = calculate(10, 5)
print(result)  # Tuple ke form mein values return hongi (15, 5)

# Yeh sab kuch basic cheezein hain jo string aur functions ke baare mein jaanna zaroori hai.
