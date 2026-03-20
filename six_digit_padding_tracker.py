#Prog02: Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.
#Example:
#Input: 143
#Output: 000143

# Ask the user to input a number between 0 and 1000
while True:
    try:
        num = int(input("Enter a number between 0 and 1000: "))
        if 0 <= num <= 1000:
            break
        else:
            print("Please enter a valid number between 0 and 1000.")
    except ValueError:
        print("Invalid input. Please enter a number,")
# Format the number to 6 digits with leading zeros
formatted_num = f"{num:06d}"
# Print the formatted number
print(f"The number in 6 digit format is: {formatted_num}")