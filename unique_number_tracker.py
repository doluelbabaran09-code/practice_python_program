#Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.

# Initialize an empty list to store the numbers
numbers = []
while True:
    try:
        # Ask the user to input a number
        num = int(input("Enter a number (or a non-integer to stop): "))
        
        # Check if the number is unique or duplicate
        if num in numbers:
            print("Duplicate")
        else:
            print("Unique")
        
        # Add the number to the list
        numbers.append(num)
    except ValueError:
        # If the user enters a non-integer, break the loop
        print("Invalid input. Stopping the program.")
        break

