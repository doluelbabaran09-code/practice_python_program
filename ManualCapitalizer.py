#Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.

# # 1. Get user input
# Example: "jUAn dELa cRuz"
raw_input = input("Enter a string: ")

if len(raw_input) == 0:
    capitalized_result = ""
else:
    # 2. Process the FIRST character (The Head)
    first_char = raw_input[0]
    ascii_first = ord(first_char)
    
    # If it's lowercase, make it uppercase
    if 97 <= ascii_first <= 122:
        first_char = chr(ascii_first - 32)
    
    # 3. Process the REST of the characters (The Tail)
    rest_of_string = ""
    for i in range(1, len(raw_input)):
        char = raw_input[i]
        ascii_char = ord(char)
        
        # If it's uppercase, make it lowercase
        if 65 <= ascii_char <= 90:
            rest_of_string += chr(ascii_char + 32)
        else:
            rest_of_string += char
            
    # 4. Combine them
    capitalized_result = first_char + rest_of_string

# 5. Display the result
print(f"Original: {raw_input}")
print(f"Manual Capitalize: {capitalized_result}")