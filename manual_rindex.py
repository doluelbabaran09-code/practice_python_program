# Prog10: Create a program that asks the user to input a string and a parameter. Return the first location starting from the last character without using the rindex() function.

# To Get the text and the character/substring to search for from the user
main_data = input("Enter the text: ")
search_char = input("Enter the character to find from the right: ")

# To Initialize the last match index to -1
char_len = len(search_char)
last_match_idx = -1

# To Scan the string backwards using a range with a step of -1
for i in range(len(main_data) - char_len, -1, -1):
    if main_data[i : i + char_len] == search_char:
        # To Record the index of the first match found from the right
        last_match_idx = i
        break 

print(f"Last match found at index: {last_match_idx}")
