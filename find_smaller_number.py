# Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.

# Prompt the user for two numbers and convert them to floats for decimal support
num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))

# Use the 'less than' operator (<) to compare values
if num_1 < num_2:
    # If num_1 is smaller, print it
    print(f"The smaller number is: {num_1}")
else:
    # If num_2 is smaller or if they are equal, print num_2
    print(f"The smaller number is: {num_2}")