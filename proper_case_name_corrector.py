#Prog05: Create a program that ask the user to input their fullname in incorrect casing. Print the input in proper casing.
#Example:
#Input: jUAn DEla CrUZ
#Output: Juan Dela Cruz

# Ask the user to input their fullname in incorrect casing
fullname = input("Enter your fullname in incorrect casing: ")
# Convert the input to proper case
propercase_fullname = fullname.title()
# Print the input in proper case
print(f"Your fullname in proper case is: {propercase_fullname}")