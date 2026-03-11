# Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.
num_1 = float(input(("Enter the first number:")))
num_2 = float(input("Enter the second number: "))
if num_1 < num_2:
    for i in range(int(num_1) + 1, int(num_2)):
        print(i)
else:
    for i in range(int(num_2) +1, int(num_1)):
        print(i)