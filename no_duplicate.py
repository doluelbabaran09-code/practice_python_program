#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

# Initialize an empty list to store the numbers
numbers = []
# Ask the user to input 10 numbers
for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)
# Create a set to store unique numbers
unique_numbers = set()
# Create a set to store duplicate numbers   
duplicate_numbers = set()
# Iterate through the list of numbers
for num in numbers:
    if num in unique_numbers:
        duplicate_numbers.add(num)
    else:
        unique_numbers.add(num)
# Display numbers that don't have duplicates
print("Numbers that don't have duplicates:")
for num in unique_numbers:
    if num not in duplicate_numbers:
        print(num)
