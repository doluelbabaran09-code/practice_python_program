# Prog09: Create a program that print all the even numbers starting from 0 to 100. (Use for loop)

# Use range(0, 101) to include the number 100
for i in range(0, 101):
    # The modulo operator (%) returns the remainder of a division.
    # If a number divided by 2 has a remainder of 0, it is even.
    if i % 2 == 0:
        # Print the current value of i only if it is even
        print(i)