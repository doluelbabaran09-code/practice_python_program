# Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.
number = 0
while number <= 100:
    if number % 10 != 0 and number % 10 != 5:
        print(number)
        number += 1
    else:
        number += 1
