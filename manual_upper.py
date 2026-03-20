# Prog03: Create a program that asks the user to input a string. Convert all characters to upper case without using the upper() function.

# To Get the input string from the user
lowercase_input = input("Enter a string: ")

# To Initialize an empty string to build the uppercase version
uppercase_output = ""

# To Loop through each character and check its ASCII value
for character in lowercase_input:
    ascii_value = ord(character)
    # To Check if the character is a lowercase letter (a-z range: 97-122)
    if 97 <= ascii_value <= 122:
        # To Subtract 32 from the ASCII value to convert it to Uppercase
        uppercase_output += chr(ascii_value - 32)
    else:
        # To Keep the character as it is if it's already uppercase or a symbol
        uppercase_output += character

print(f"Uppercase Result: {uppercase_output}")