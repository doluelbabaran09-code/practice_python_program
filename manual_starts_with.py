# Prog05: Create a program that asks the user to input a string and a prefix. Check if the string begins with the prefix without using the startswith() function.

# To Get the main string and the search prefix from the user
full_string = input("Enter the main text: ")
prefix_query = input("Enter the prefix to find: ")

# To Store the length of the prefix for slicing comparison
query_length = len(prefix_query)

# To Compare the beginning slice of the string to the prefix
if full_string[:query_length] == prefix_query:
    match_status = True
else:
    match_status = False

print(f"Starts with '{prefix_query}'? {match_status}")