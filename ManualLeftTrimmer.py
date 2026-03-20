#Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.

# 1. Get the input name
# Example: "      Juan Dela Cruz"
raw_name_input = input("Enter your full name (with spaces at the start): ")

# 2. Find the index of the first character that is NOT a space
first_non_space_index = 0

# We loop through the string using the index 'i'
for i in range(len(raw_name_input)):
    if raw_name_input[i] != " ":
        first_non_space_index = i
        break # Exit the loop as soon as we find the first real character
else:
    # This part runs only if the entire string was nothing but spaces
    first_non_space_index = len(raw_name_input)

# 3. Use string slicing to keep everything from that index to the end
# The [index:] syntax means "start here and go to the very last character"
manual_cleaned_name = raw_name_input[first_non_space_index:]

# 4. Display the results
print("\n--- Manual Trimming Result ---")
print(f"Original: '{raw_name_input}'")
print(f"Manual  : '{manual_cleaned_name}'")
print("------------------------------")