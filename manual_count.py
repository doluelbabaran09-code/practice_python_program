# Prog08: Create a program that asks the user to input a string and a parameter. Return how many times the parameter appears without using the count() function.

# To Get the full text and the substring pattern to count from the user
search_space = input("Enter the full text: ")
target_pattern = input("Enter the pattern to count: ")

# To Initialize the counter and measure the pattern length
occurrence_count = 0
pattern_len = len(target_pattern)

# To Use a sliding window to check every possible substring of the target length
for i in range(len(search_space) - pattern_len + 1):
    if search_space[i : i + pattern_len] == target_pattern:
        # To Increment the count every time a match is found
        occurrence_count += 1

print(f"Pattern found {occurrence_count} times.")