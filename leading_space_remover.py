#Prog01: Create a program that ask the user to input their fullname with several space characters at the beginning. Print the input without the spaces in the beginning.
#Example:
#Input:         Juan Dela Cruz
#Output: Juan Dela Cruz

# Ask the user to input their fullname with leading spaces
fullname = input("Enter your fullname with leading spaces: ")
# Remove leading spaces from the input
trimmed_fullname = fullname.lstrip()
# Print the input without leading spaces
print(f"Your fullname without leading spaces is: {trimmed_fullname}")
