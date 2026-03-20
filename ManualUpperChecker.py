#Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.

# 1. Get input from the user
test_string = input("Enter a string to check: ")

# 2. Initialize tracking flags
contains_lowercase = False
contains_uppercase = False

# 3. Loop through every character in the string
for char in test_string:
    ascii_val = ord(char)
    
    # Check if character is Lowercase (97-122)
    if 97 <= ascii_val <= 122:
        contains_lowercase = True
        break # We found a lowercase letter, no need to keep checking
        
    # Check if character is Uppercase (65-90)
    elif 65 <= ascii_val <= 90:
        contains_uppercase = True

# 4. Final Logic Determination
# A string is "isupper" if it has uppercase letters AND zero lowercase letters
if contains_uppercase and not contains_lowercase:
    is_all_upper_manual = True
else:
    is_all_upper_manual = False

# 5. Display the result
print(f"String: '{test_string}'")
print(f"Manual isupper() result: {is_all_upper_manual}")