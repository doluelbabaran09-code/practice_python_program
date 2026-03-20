# Prog05: Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.

# Get the two numbers by using input and floats
num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))

# Logic: % is the modulo operator. It gives you the "leftover" after division.
remainder_of_numbers = num_1 % num_2

print(f"The remainder is: {remainder_of_numbers}")