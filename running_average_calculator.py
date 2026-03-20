#Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.

# Initialize an empty list to store the numbers
numbers = []
# Ask the user to input numbers until an invalid input is given
while True:
    try:
        num = int(input("Enter a number (or a non-number to stop): "))
        numbers.append(num)
    except ValueError:
        break
# Calculate the average
if numbers:
    average = sum(numbers) / len(numbers)
    print(f"The average is; {average}")
else:
    print("No valid numbers were entered.")
