# Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.

# 1. Setup the initial data
original_string = "Hello"
target_total_width = 10

# 2. Calculate the current length of the string
current_length = len(original_string)

# 3. Determine how many spaces are needed
# If the target is 10 and current is 5, we need 5 spaces.
padding_needed = target_total_width - current_length

# 4. Check if padding is actually required
if padding_needed > 0:
    # Create a string of spaces by multiplying the space character
    spaces_to_add = " " * padding_needed
    # Add the spaces to the END (right side) of the string
    manual_ljust_result = original_string + spaces_to_add
else:
    # If the string is already long enough, do nothing
    manual_ljust_result = original_string

# 5. Display the result
# We use brackets [ ] so you can clearly see the empty spaces at the end
print(f"Original: [{original_string}]")
print(f"Target Width: {target_total_width}")
print(f"Result  : [{manual_ljust_result}]")
print(f"Final Length: {len(manual_ljust_result)}")