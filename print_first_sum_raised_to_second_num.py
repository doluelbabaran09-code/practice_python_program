# Prog06: Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.

# Get the base and the exponent from the user and convert to float for decimal support
num_1 = float(input("Enter the first number : "))
num_2 = float(input("Enter the second number : "))

# Use the double asterisk (**) operator to calculate power
# This is equivalent to num_1 to the power of num_2
result = num_1 ** num_2

# Display the final calculated value
print(f"The result of raising the first number to the second number is: {result}")