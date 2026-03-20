# # 1. Get the input from the user
# Example: "jUAn DEla CrUZ"
raw_input_string = input("Enter a string with mixed casing: ")

# 2. Create an empty string to build our result
swapped_result = ""

# 3. Loop through each character and check its ASCII value
for char in raw_input_string:
    ascii_val = ord(char)
    
    # Is it Uppercase? (A-Z: 65-90)
    if 65 <= ascii_val <= 90:
        # Convert to Lowercase by adding 32
        swapped_result += chr(ascii_val + 32)
        
    # Is it Lowercase? (a-z: 97-122)
    elif 97 <= ascii_val <= 122:
        # Convert to Uppercase by subtracting 32
        swapped_result += chr(ascii_val - 32)
        
    # If it's not a letter (space, number, etc.), keep it as is
    else:
        swapped_result += char

# 4. Display the result
print("\n--- Manual Swapcase Result ---")
print(f"Original: {raw_input_string}")
print(f"Swapped : {swapped_result}")
print("------------------------------")