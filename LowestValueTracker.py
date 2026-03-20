#Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number

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

# Display the lowest number
if numbers:
    print("The lowest number is:", min(numbers))
else:
    print("No valid numbers were entered.")