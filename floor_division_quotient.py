# Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point

# Ask the user for two numbers make them into floats
num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))

# Logic: // is the floor division operator. 
# It divides numbers and rounds down to the nearest whole number.
quotient_of_numbers = num_1 // num_2

print(f"The quotient of the two numbers is: {quotient_of_numbers}")