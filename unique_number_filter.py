# Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry

#  Initialize an empty list to store the 10 inputs
numbers = []

print("Please enter 10 numbers:")

#  Loop 10 times to collect user input
for i in range(10):
    while True:
        try:
            # Ask user for input and convert to an integer
            num = int(input(f"Enter number {i+1}: "))
            numbers.append(num)
            break # Exit the 'while' loop if input is valid
        except ValueError:
            # If the user enters text instead of a number, show an error
            print("Invalid input. Please enter an integer.")

#  Display the full list entered by the user
print("\nOriginal list:", numbers)

#  Filter and display unique numbers
print("Numbers (duplicates removed):")

# This list tracks which numbers we have already printed
seen = [] 

for num in numbers:
    # Check if we have encountered this number before
    if num not in seen:
        # If not seen, print it and add it to our tracking list
        print(num, end=" ")
        seen.append(num)

# Print a new line at the end for clean formatting
print()