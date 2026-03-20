# Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

# Initialize an 'accumulator' variable to zero
total = 0

# Loop 10 times to collect 10 different inputs
for i in range(10):
    # Ask the user for a number; use f-string to show which number they are entering
    num = float(input(f"Enter number {i+1}: "))
    
    # Add the current number to the running total
    # This is shorthand for: total = total + num
    total += num

# After the loop finishes, print the final sum
print(f"The sum of all the numbers is: {total}")