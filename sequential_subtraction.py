# Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.
numbers = {}
for i in range(10):
    num = float(input(f"Enter number {i + 1}: "))
    numbers[i] = num
result = numbers[0]
for i in range(1, 10):
    result -= numbers[i]
    print(f"The result of the first number minus all of the remaining numbers is: {result}")