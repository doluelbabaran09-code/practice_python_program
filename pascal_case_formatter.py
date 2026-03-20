#Prog09: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.
#Example:
#Input: jUAn DEla CrUZ
#Output: JuanDelaCruz

# Ask the user to input their fullname in incorrect casing
fullname = input("Enter your fullname in incorrect casing: ")
# Convert the input to pascal case
pascalcase_fullname = ''.join(word.capitalize() for word in fullname.split())
# Print the input in pascal case
print(f"Your fullname in pascal case is: {pascalcase_fullname}")
