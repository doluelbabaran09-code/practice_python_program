# Prog02: Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.

# Collect two numbers from the user
num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))

# The != operator stands for "not equal to"
if num_1 != num_2:
    # This block executes only if the numbers are different
    print("Not Equal")
else:
    # This block executes if the numbers are exactly the same
    print("Equal")