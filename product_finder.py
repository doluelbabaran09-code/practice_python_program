# Prog04: Create a program that ask user to input 2 numbers. Print the product of the two numbers.

# Prompt the user for two inputs and convert them to floats
# Using float allows the program to multiply decimals, not just whole integers
num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))

# Use the asterisk (*) operator to perform multiplication
product_of_numbers = num_1 * num_2

# Print the result using an f-string for clear formatting
print(f"The product of the two numbers is: {product_of_numbers}")