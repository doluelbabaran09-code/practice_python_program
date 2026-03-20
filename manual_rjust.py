# Prog06: Create a program that asks the user to input a string and a width. Add space characters at the beginning of the string without using the rjust() function.

# To Get the string and the target total width from the user
name_to_align = input("Enter a name: ")
target_width = int(input("Enter the total width: "))

# To Calculate how many spaces are needed to reach the target width
padding_count = target_width - len(name_to_align)

# To Check if padding is necessary
if padding_count > 0:
    # To Prepend the required number of spaces to the front of the string
    justified_name = (" " * padding_count) + name_to_align
else:
    justified_name = name_to_align

print(f"Result: '{justified_name}'")