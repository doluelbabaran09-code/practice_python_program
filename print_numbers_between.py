# Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

# Get two integers from the user
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

# Check if the first number is smaller to ensure the range moves forward
if num_1 < num_2:
    print(f"The numbers between {num_1} and {num_2} are:")
    
    # range(start, stop) starts at 'start' and ends just before 'stop'.
    # We use num_1 + 1 so that num_1 itself is not printed.
    for i in range(num_1 + 1, num_2):
        print(i)