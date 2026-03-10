# Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.
even_count = 0
for i in range(10):
    num = float(input(f"Enter number {i + 1}:"))
    if num % 2 == 0:
        even_count += 1
        print(f"The number {num} is an even number")
print(f"The total number of even numbers is: {even_count}")