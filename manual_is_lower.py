#Prog04: Create a program that asks the user to input a string. Check if all characters are in lower case without using the islower() function.Prog04: Create a program that asks the user to input a string. Check if all characters are in lower case without using the islower() function.

# To Get the string to be checked from the user
check_text = input("Enter text to check: ")

# To Initialize flags to track lowercase presence and uppercase violations
has_small_letter = False
has_capital_letter = False

# To Iterate through the string to inspect each character
for character in check_text:
    code = ord(character)
    # To Detect if a lowercase letter exists
    if 97 <= code <= 122:
        has_small_letter = True
    # To Detect if an uppercase letter exists (violation)
    elif 65 <= code <= 90:
        has_capital_letter = True
        break

# To Determine result: True only if lowercase exists and no uppercase was found
is_lower_result = has_small_letter and not has_capital_letter
print(f"Is it all lowercase? {is_lower_result}")