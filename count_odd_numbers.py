# Prog08: Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)

# Initialize the starting point for our loop at zero
number = 0
# Logic: Keep looping as long as the number is 100 or less
while number <= 100:
    # Check if the number is NOT even (meaning it's odd)
    if number % 2 != 0:
        print(number)
    
    # Increment the counter in every iteration to avoid an infinite loop
    number += 1
