# Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.

# Initialize the starting point for our loop at zero
number = 0

# Use a while loop to iterate from 0 through 100
while number <= 100:
    # Logic: Numbers ending in 0 or 5 are all divisible by 5.
    # However, checking 'number % 10' specifically targets the last digit.
    # If the remainder when divided by 10 is not 0 AND not 5, we print it.
    if number % 10 != 0 and number % 10 != 5:
        print(number)
    
    # Increment the counter to move to the next number
    # This is placed outside the 'if' to ensure the loop always progresses
    number += 1