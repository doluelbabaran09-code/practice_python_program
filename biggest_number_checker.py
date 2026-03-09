# Prog01: Create a program that asks user to input 2 numbers. Print the bigger number.

# To Get input from the user and convert the string inputs into floats (decimal numbers)
num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))

# To Check if the first number is strictly greater than the second
if num_1 > num_2:
    print(f"The Bigger number is: {num_1}")

# To Check if the second number is strictly greater than the first
elif num_2 > num_1:
    print(f"The Bigger number is: {num_2}")