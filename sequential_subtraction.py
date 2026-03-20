# Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

# Use a dictionary to store inputs with their index as the key
numbers = {}
for i in range(10):
    num = float(input(f"Enter number {i + 1}: "))
    numbers[i] = num

# Start the result with the first number entered (index 0)
result = numbers[0]

# Subtract the remaining numbers (index 1 through 9) from the result
for i in range(1, 10):
    result -= numbers[i]

# Moved the print outside the loop to show only the final result
print(f"The final result is: {result}")