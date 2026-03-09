# Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.

# Initialize a counter variable to zero to keep track of odd numbers found
odd_count = 0
# Use a for loop to repeat the input process 10 times
# range(10) generates numbers from 0 to 9
for i in range(10):
    # Ask the user for an integer; f-string used to show the current count (1 to 10)
    num = int(input(f"Enter number {i+1}: "))
    
    # Use the modulo operator (%) to check for a remainder when divided by 2
    # If the remainder is NOT 0, the number is odd
    if num % 2 != 0:
        # Increment the counter by 1 if the condition is met
        odd_count += 1

# After the loop finishes, print the final tally
print(f"The total count of odd numbers is: {odd_count}")