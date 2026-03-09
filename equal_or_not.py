# Prog02: Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.

# Ask the user for two numbers and convert the input strings into float (decimal) format
num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))

# Compare the two numbers using the equality operator (==)
if num_1 == num_2:
    # This Part runs only if num_1 and num_2 have the exact same value
    print("Equal")
else: 
    # This Part runs if the numbers are different
    print("Not Equal")