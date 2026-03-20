#Prog10: Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.
#Example:
#Input: jUAn DEla CrUZ
#Output: juan_dela_cruz

# Ask the user to input their fullname in incorrect casing
fullname = input("Enter your fullname in incorrect casing: ")
# Convert the input to snake case
snakecase_fullname = '_'.join(word.lower() for word in fullname.split())
# Print the input in snake case
print(f"Your fullname in snake case is: {snakecase_fullname}")
