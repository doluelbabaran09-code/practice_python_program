#Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.

# 1. Get the input
raw_input_string = input("Enter a string with UPPERCASE letters: ")

# 2. Create an empty string to store our result
manual_lowercase_result = ""

# 3. Loop through each character
for char in raw_input_string:
    # Get the ASCII numerical value of the character
    ascii_value = ord(char)
    
    # Check if the character is an Uppercase letter (A-Z are 65-90)
    if 65 <= ascii_value <= 90:
        # Add 32 to the value to find the lowercase equivalent
        lowercase_ascii = ascii_value + 32
        # Convert the number back into a character and add to our result
        manual_lowercase_result += chr(lowercase_ascii)
    else:
        # If it's not uppercase, just keep the character as it is
        manual_lowercase_result += char

# 4. Display the result
print("\n--- Manual Conversion Result ---")
print(f"Original: {raw_input_string}")
print(f"Manual  : {manual_lowercase_result}")
print("--------------------------------")