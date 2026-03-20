# Prog02: Create a program that asks the user to input a string and a suffix. Remove the suffix from the end of the string without using the removesuffix() function.

# To Get the main string and the suffix to be removed from the user
original_text = input("Enter the full text: ")
suffix_to_cut = input("Enter the suffix to remove: ")

# To Calculate the length of the suffix to determine the slice size
suffix_length = len(suffix_to_cut)

# To Check if the end of the original text matches the suffix using negative slicing
if original_text[-suffix_length:] == suffix_to_cut:
    # To Slice the string and keep everything except the suffix part
    final_result = original_text[:-suffix_length]
else:
    # To Keep the original text if no suffix match is found
    final_result = original_text

print(f"Result: {final_result}")