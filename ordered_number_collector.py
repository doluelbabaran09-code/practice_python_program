#Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function

# Initialize an empty list to store the numbers
numbers = []
while True:
    try:
        # Ask the user to input a number
        num = int(input("Enter a number (or a non-integer to stop): "))
        
        # Add the number to the list
        numbers.append(num)
    except ValueError:
        # If the user enters a non-integer, break the loop
        print("Invalid input. Stopping the program.")
        break

# Display the numbers from lowest to highest
if numbers:
    numbers.sort()
    print("The numbers from lowest to highest are:", numbers)
else:
    print("No valid numbers were entered.")