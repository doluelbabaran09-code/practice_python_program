# Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.

num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))
if num_1 > num_2:
    print(f"The bigger number is: {num_1}")
elif num_2 > num_1:
    print(f"The bigger number is: {num_2}")
else:
    print("Both numbers are equal.")