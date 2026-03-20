# Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.

# 1. Setup the data
original_text = "Hello"
target_width = 12

# 2. Check if the string actually needs padding
current_len = len(original_text)

if target_width > current_len:
    # 3. Calculate total spaces needed
    total_padding = target_width - current_len
    
    # 4. Split the padding in half
    # '//' is integer division (e.g., 7 // 2 = 3)
    left_padding_count = total_padding // 2
    
    # The right side gets whatever is left over
    right_padding_count = total_padding - left_padding_count
    
    # 5. Build the final string
    manual_center_result = (" " * left_padding_count) + original_text + (" " * right_padding_count)
else:
    # If the string is already wider than the target, return as is
    manual_center_result = original_text

# 6. Display results
# We use pipes | | to show the boundaries of the string
print(f"Original: [{original_text}] (Length: {current_len})")
print(f"Target Width: {target_width}")
print(f"Result  : |{manual_center_result}|")
print(f"Final Length: {len(manual_center_result)}")