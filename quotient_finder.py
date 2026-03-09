# Prog05: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point
num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))

if num_2 != 0:
    quotient_of_numbers = num_1 / num_2
    print(f"The quotient of the two numbers is: {quotient_of_numbers}")
else:
    print("Error: Division by zero is not allowed.")