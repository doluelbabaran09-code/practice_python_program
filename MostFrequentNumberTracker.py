#Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

# Initialize an empty list to store the numbers
numbers = []
# Ask the user to input numbers until an invalid input is given
while True:
    try:
        num = int(input("Enter a number (or a non-number to stop):"))
        numbers.append(num)
    except ValueError:
        break
# Create a dictionary to count the occurrences of each number
number_counts = {}
for num in numbers:
    if num in number_counts:
        number_counts[num] += 1
    else:
        number_counts[num] = 1
# Find the number with the most duplicates
most_frequent_number = None
for num, count in number_counts.items():
    if most_frequent_number is None or count > number_counts[most_frequent_number]:
        most_frequent_number = num
# Display the most frequent number
if most_frequent_number is not None:
    print(f"The number with the most duplicates is: {most_frequent_number}")