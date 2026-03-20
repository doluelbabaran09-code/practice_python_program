#Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.

# 1. Setup the data
original_string = "Professor Juan Dela Cruz"
target_prefix = "Professor "

# 2. Get the length of the prefix we want to remove
prefix_length = len(target_prefix)

# 3. Perform the manual check
# We look at the original string from index 0 up to the length of the prefix
if original_string[0:prefix_length] == target_prefix:
    # If it matches, we slice the string starting FROM the end of the prefix
    manual_cleaned_string = original_string[prefix_length:]
    print("Prefix found and removed!")
else:
    # If it doesn't match, the string stays the same
    manual_cleaned_string = original_string
    print("Prefix not found. No changes made.")

# 4. Display the results
print("-" * 30)
print(f"Original : {original_string}")
print(f"Result   : {manual_cleaned_string}")
print("-" * 30)