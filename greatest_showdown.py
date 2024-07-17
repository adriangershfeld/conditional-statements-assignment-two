# Task 1: Identify the Greatest 
# Write a Python program that asks the user to enter three numbers.
# Your code should then identify and print out the largest number among the three.

# Task 2: Identify the Smallest 
# Improve upon your code from Task 1 to also determine the smallest number among the three and print it out.
# Expected Outcome: If we provide the numbers 3, 3, and 4, it should print out that "The smallest number is 3. The largest number is 4. "

smallest_number = ''
greatest_number = ''

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the third number: "))

if first_number >= second_number and first_number >= third_number:
    greatest_number = first_number
elif second_number >= first_number and second_number >= third_number:
    greatest_number = second_number
else:
    greatest_number = third_number

if first_number <= second_number and first_number <= third_number:
    smallest_number = first_number
elif second_number <= first_number and second_number <= third_number:
    smallest_number = second_number
else:
    smallest_number = third_number

print(f"The smallest number is {smallest_number}. The largest number is {greatest_number}. ")