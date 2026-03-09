# Prog03: Create a program that ask user to input 2 numbers. Print the sum of the two numbers.

# Prompt the user for two inputs and convert them to floats
# Using float() ensures that the program can handle both whole numbers and decimals
num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))

# Use the plus (+) operator to calculate the total
sum_of_numbers = num_1 + num_2

# Display the result using an f-string for a clean, readable output
print(f"The sum of the two numbers is: {sum_of_numbers}")