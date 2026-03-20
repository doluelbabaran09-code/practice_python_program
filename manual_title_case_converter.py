# Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.

# 1. Get input from the user
# Example: "jUAn dELa cRuz"
raw_input = input("Enter a string: ")

# 2. Create an empty string for the result
title_result = ""

# 3. Loop through the string using the index 'i'
for i in range(len(raw_input)):
    char = raw_input[i]
    ascii_val = ord(char)
    
    # Logic: Is this character the start of a word?
    # It's the start if it's the first character (i == 0) 
    # OR if the character before it was a space.
    if i == 0 or raw_input[i-1] == " ":
        # Make it Uppercase if it's currently lowercase (97-122)
        if 97 <= ascii_val <= 122:
            title_result += chr(ascii_val - 32)
        else:
            title_result += char
    else:
        # Not the start of a word: Make it Lowercase if it's currently uppercase (65-90)
        if 65 <= ascii_val <= 90:
            title_result += chr(ascii_val + 32)
        else:
            title_result += char

# 4. Display the result
print(f"Original: {raw_input}")
print(f"Manual Title Case: {title_result}")