# Prog01: Create a program that asks the user to input a string. Remove the space characters at the end of the string without using the lstrip() function.

# To Get input from the user
user_input = input("Enter a string with spaces at the end: ")

# To Initialize the index to the end of the string
last_valid_index = 0

# To Scan the string backwards from the last character to find the first non-space
for i in range(len(user_input) - 1, -1, -1):
    if user_input[i] != " ":
        # To Mark the position right after the last valid character
        last_valid_index = i + 1
        break

# To Slice the string from the start to the last valid index found
cleaned_name = user_input[:last_valid_index]

# To Print the result showing the trimmed string
print(f"Original: '{user_input}'")
print(f"Cleaned : '{cleaned_name}'")