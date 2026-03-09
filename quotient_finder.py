# Prog05: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point

# Get two numbers from the user and convert them to floats
num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))

# Check if the divisor (num_2) is not zero to prevent a ZeroDivisionError
if num_2 != 0:
    # Use the single slash (/) operator for standard division, which results in a float
    quotient_of_numbers = num_1 / num_2
    print(f"The quotient of the two numbers is: {quotient_of_numbers}")
else:
    # Handle the case where the user enters zero as the second number
    print("Error: Division by zero is not allowed.")