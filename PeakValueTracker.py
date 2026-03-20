#Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number

# Initialize an empty list to store the numbers
numbers = []
# Ask the user to input numbers until an invalid input is given
while True:
    try:
        num = int(input("Enter a number (or a non-number to stop): "))
        numbers.append(num)
    except ValueError:
        break

# Find the highest number
if numbers:
    highest_number = max(numbers)
    print(f"The highest number is: {highest_number}")
else:
    print("No valid numbers were entered.")
