# Understanding Loops in Python

# A loop is a programming structure that repeats a set of instructions until a condition is met.
# Loops are useful when you want to run the same block of code multiple times.

# 1. FOR LOOP EXAMPLE
print("For Loop Example:")

# The for loop runs a block of code a specified number of times.
for i in range(5):  # 'range(5)' generates numbers from 0 to 4 (5 iterations)
    print("Iteration number:", i)  # Prints the current iteration number

# 2. WHILE LOOP EXAMPLE
print("\nWhile Loop Example:")

# The while loop continues to run as long as a condition is true.
count = 0  # Initialize a counter variable
while count < 5:  # The loop will run while 'count' is less than 5
    print("Count is:", count)
    count += 1  # Increments count by 1 each time the loop runs

# 3. BREAK STATEMENT EXAMPLE
print("\nBreak Statement Example:")

# The break statement stops the loop even if the condition is still true.
for num in range(10):  # Looping through numbers from 0 to 9
    if num == 5:  # If num reaches 5, exit the loop
        print("Breaking at", num)
        break  # Stops the loop
    print("Number:", num)

# 4. CONTINUE STATEMENT EXAMPLE
print("\nContinue Statement Example:")

# The continue statement skips the rest of the code inside the loop for the current iteration.
for num in range(5):  # Looping through numbers 0 to 4
    if num == 2:  # If num is 2, skip the rest of the code in this iteration
        print("Skipping", num)
        continue  # Goes to the next iteration
    print("Number:", num)

# 5. NESTED LOOPS EXAMPLE
print("\nNested Loops Example:")

# A loop inside another loop is called a nested loop.
for i in range(3):  # Outer loop (Runs 3 times)
    for j in range(2):  # Inner loop (Runs 2 times for each outer loop iteration)
        print("Outer loop iteration:", i, "- Inner loop iteration:", j)

# 6. LOOPING THROUGH A LIST
print("\nLooping Through a List Example:")

fruits = ["apple", "banana", "cherry"]  # A list of fruits
for fruit in fruits:  # Loop through each item in the list
    print("Fruit:", fruit)  # Print the current fruit
