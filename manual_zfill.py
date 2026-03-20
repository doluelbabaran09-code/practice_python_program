# Prog07: Create a program that asks the user to input a string and a width. Add zero characters at the beginning of the string without using the zfill() function.Prog07: Create a program that asks the user to input a string and a width. Add zero characters at the beginning of the string without using the zfill() function.Prog07: Create a program that asks the user to input a string and a width. Add zero characters at the beginning of the string without using the zfill() function.

# To Get the numeric string and the required length from the user
id_number = input("Enter a number: ")
min_length = int(input("Enter required length: "))

# To Calculate the number of zeros needed to fill the leading gap
zero_padding = min_length - len(id_number)

# To Prepend zeros only if the current length is less than the minimum
if zero_padding > 0:
    formatted_id = ("0" * zero_padding) + id_number
else:
    formatted_id = id_number

print(f"Formatted ID: {formatted_id}")
