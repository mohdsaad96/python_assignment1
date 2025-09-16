# Task 1:

# Taking two numbers from user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Performing operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Checking division by zero
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (cannot divide by zero)"

# Displaying results
print("\nResults of Basic Operations:")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)


# Task 2:

# Taking user's first and last name
first_name = input("\nEnter your first name: ")
last_name = input("Enter your last name: ")

# Creating full name
full_name = first_name + " " + last_name

# Displaying personalized greeting
print("Hello,", full_name + "! Welcome to Python programming.")




