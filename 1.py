# Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.

num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))

if num_1 < num_2:
    print(f"The smaller number is: {num_1}")
else:
    print(f"The smaller number is: {num_2}")