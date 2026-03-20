#Prog07: Create a program that ask the user to input a complete statement. Print the number of words in the input.
#Example:
#Input: We will weather the weather whatever the weather whether we like it or not
#Output: 14

# Ask the user to input a complete statement
statement = input("Enter a complete statement: ")
# Split the input into words and count them
word_count = len(statement.split())
# Print the number of words in the input
print(f"The number of words in your statement is: {word_count}")
