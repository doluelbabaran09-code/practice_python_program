#Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function

# Initialize an empty list to store the numbers
numbers = []
# Ask the user to input numbers until an invalid input is given
while True:
    try:
        num = int(input("Enter a number (or a non-number to stop):"))
        numbers.append(num)
    except ValueError:
        break
# Sort the numbers in descending order
numbers.sort(reverse=True)
# Display the numbers from highest to lowest
print("Numbers in descending order:")
for num in numbers:
    print(num)
