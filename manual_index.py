# Prog09: Create a program that asks the user to input a string and a parameter. Return the first location of the parameter without using the index() function.

# To Get the text and the fragment to search for from the user
source_data = input("Enter the text: ")
target_fragment = input("Enter fragment to find: ")

# To Measure fragment length and initialize the index to -1 (not found)
frag_len = len(target_fragment)
first_match_idx = -1

# To Iterate through the string to find the first matching window
for i in range(len(source_data) - frag_len + 1):
    if source_data[i : i + frag_len] == target_fragment:
        # To Store the current index as the first match and stop searching
        first_match_idx = i
        break 

print(f"First match found at index: {first_match_idx}")