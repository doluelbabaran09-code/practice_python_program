# Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
if num_1 < num_2:
    print(f"The numbers between {num_1} and {num_2} are:")
    for i in range(num_1 + num_2):
        print(i)