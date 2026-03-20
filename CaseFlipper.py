#Prog06: Create a program that ask the user to input their fullname in incorrect casing. Print each character of the input in reverse casing.
#Example:
#Input: jUAn DEla CrUZ
#Output: JuaN deLA cRuz

# Ask the user to input their fullname in incorrect casing
fullname = input("Enter your fullname in incorrect casing: ")
# Reverse the casing of each character in the input
reversed_casing_fullname = ''.join([char.lower() if char.isupper() else char.upper() for char in fullname])
# Print the input with reversed casing
print(f"Your fullname with reversed casing is: {reversed_casing_fullname}")