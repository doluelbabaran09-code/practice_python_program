# Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.

# 1. Setup the test data
main_text_input = "www.google.com"
target_suffix = ".com"

# 2. Get the length of the suffix
suffix_length = len(target_suffix)

# 3. Handle the edge case: if suffix is longer than the string, it can't match
if suffix_length > len(main_text_input):
    manual_endswith_result = False
else:
    # 4. Use negative slicing to get the end of the main string
    # [-suffix_length:] starts 'n' characters from the right and goes to the end
    end_of_string_slice = main_text_input[-suffix_length:]
    
    # 5. Compare the slice to our target
    if end_of_string_slice == target_suffix:
        manual_endswith_result = True
    else:
        manual_endswith_result = False

# 6. Display the results
print(f"Main String: '{main_text_input}'")
print(f"Target Suffix: '{target_suffix}'")
print(f"Manual endswith() Result: {manual_endswith_result}")