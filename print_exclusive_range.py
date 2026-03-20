# Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.
\
# Collect inputs as floats to prevent errors, but convert to int for range logic
num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))

# Case 1: The first number is smaller
if num_1 < num_2:
    print(f"Numbers between {num_1} and {num_2}:")
    # range(start, stop) excludes the stop value. 
    # Adding +1 to start ensures num_1 is not printed.
    for i in range(int(num_1) + 1, int(num_2)):
        print(i)

# Case 2: The second number is smaller
elif num_1 > num_2:
    print(f"Numbers between {num_2} and {num_1}:")
    for i in range(int(num_2) + 1, int(num_1)):
        print(i)

# Case 3: Numbers are equal
else:
    print("There are no numbers strictly between two equal values.")