''' Task1 -Given a list of dictionaries, each representing a person with 'name' and 'age' keys, use lambda functions to
 filter out people under 18 and then map the remaining people's names to a new list.'''

people = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 16},
    {'name': 'Charlie', 'age': 30},
    {'name': 'David', 'age': 17},
    {'name': 'Eve', 'age': 22}
]

# Step 1: Filter people who are 18 or older
adults = list(filter(lambda x: x["age"] >= 18, people))

# Step 2: Map their names into a new list
adult_names = list(map(lambda x: x["name"], adults))

print(adult_names)  # Output: ['Alice', 'Charlie', 'Eve']

print("--------------------------------------------------")

'''Task 2 Given a list of numbers, use the reduce function and a
 lambda expression to calculate the product of all the numbers in the list. '''
from functools import reduce

# Sample list of numbers
numbers = [2, 3, 4, 5]

# Use reduce with a lambda function to calculate the product
# The lambda function (lambda x, y: x * y) takes two arguments (x and y)
# and multiplies them. The reduce function applies this sequentially
# across the list:
# 1. 2 * 3 = 6
# 2. 6 * 4 = 24
# 3. 24 * 5 = 120
product = reduce(lambda x, y: x * y, numbers)

print(f"The list of numbers is: {numbers}")
print(f"The product of all numbers is: {product}")
print("--------------------------------------------------")

''' Task 3 # Write a list comprehension that creates a new list of squares of even numbers from a given list,
 using a lambda function to check for even numbers.'''
# The initial list of integers.
numbers = [1, 2, 3, 4, 5, 6]

# Filter the 'numbers' list to keep only the even numbers.
# filter() applies the lambda function to each element:
# lambda x : x % 2 == 0 checks if the remainder when x is divided by 2 is 0.
# The result is cast to a list.
# even_number will become [2, 4, 6]
even_number = list(filter(lambda x: x % 2 == 0, numbers))

# Create a new list 'square_number' using a list comprehension.
# It iterates through the 'even_number' list and squares (x**2) each element.
# The squares of [2, 4, 6] are [4, 16, 36].
squre_number = [x**2 for x in even_number]

# Print the final list containing the squares of the original even numbers.
print(squre_number)

print("--------------------------------------------------")
''' Task 4 - write the lambda function to check if a given stringa is a number '''
# The list 'data' contains strings. Some represent numbers (integers, floats, negatives), and some are non-numeric text.
data = ["123", "45.6", "hello", "007", "98a", "-42", "0"]

# Define a function 'is_number' to robustly check if a string can be interpreted as a number.
def is_number(s):
    # Use a try-except block, the most reliable way to check for valid number conversion in Python.
    try:
        # Attempt to convert the input string 's' to a floating-point number.
        # This handles standard integers ("123"), floats ("45.6"), and negative numbers ("-42").
        float(s)
        # If conversion succeeds without error, 's' is a number, so return True.
        return True
    # If the string cannot be converted (e.g., "hello" or "98a"), a ValueError is raised.
    except ValueError:
        # Catch the ValueError and return False, indicating the string is not a valid number.
        return False

# Use the 'filter()' function to select only the elements from the 'data' list
# for which the provided function (the lambda) returns True.
# The lambda calls 'is_number(x)' for each element 'x', so only strings that are numbers will pass the filter.
# The result is cast to a list.
cheking_number = list(filter(lambda x: is_number(x), data))

# Print the final list, which contains only the original strings that represent numbers.
# Expected Output: ['123', '45.6', '007', '-42', '0']
print(cheking_number)

print("--------------------------------------------------")
'''Task 5  use lambda function to extract the year month and day from a datetime object '''
from datetime import datetime

# Import the 'datetime' class from the 'datetime' module.
# This class is used to create and manipulate date and time objects.

# Create a list named 'dates' containing three 'datetime' objects.
dates = [
    # The first datetime object: October 20, 2025
    datetime(2025, 10, 20),
    # The second datetime object: January 15, 2024
    datetime(2024, 1, 15),
    # The third datetime object: December 31, 2023
    datetime(2023, 12, 31)
]

# Use the 'map()' function to apply a transformation to every element in the 'dates' list.
# The result of 'map' is converted to a list and assigned to the variable 'data'.
data = list(map(
    # Define an anonymous function (lambda) that takes a single datetime object 'd'.
    # This function extracts the year, month, and day attributes from the datetime object 'd'.
    # It returns these three values as a tuple: (year, month, day).
    lambda d: (d.year, d.month, d.day),
    # The 'map' function iterates over the 'dates' list.
    dates
))

# Print the resulting 'data' list.
# This list will contain tuples, where each tuple represents the (year, month, day)
# components of the original datetime objects.
# Expected Output: [(2025, 10, 20), (2024, 1, 15), (2023, 12, 31)]
print(data)

print("--------------------------------------------------")
'''Task 6 create the lambda function to generate fibonacci series '''
# Define the input number, which specifies how many Fibonacci numbers to generate.
number = 20


# Define a function named 'fibonacci' that calculates the first 'n' numbers of the Fibonacci sequence.
def fibonacci(n):
    # Initialize the list 'fib' with the first two numbers of the Fibonacci sequence.
    # The sequence always starts with 0 and 1.
    fib = [0, 1]

    # Start a loop from index 2 up to (but not including) 'n'.
    # This loop generates the rest of the sequence elements.
    for i in range(2, n):
        # Calculate the next Fibonacci number by adding the two previous numbers in the list:
        # fib[i-1] (the number immediately before the current one)
        # plus fib[i-2] (the number two positions before the current one).
        next_fib = fib[i - 1] + fib[i - 2]

        # Append the newly calculated number to the end of the 'fib' list.
        fib.append(next_fib)

    # Return a slice of the 'fib' list.
    # 'fib[:n]' ensures that exactly 'n' numbers are returned, covering cases where 'n' is 0 or 1.
    return fib[:n]


# Define a lambda function 'b' that is simply an alias (a shortcut) for the 'fibonacci' function.
# It takes one argument 'x' and calls fibonacci(x).
b = lambda x: fibonacci(x)

# Call the lambda function 'b' with the value of 'number' (which is 20).
# This executes fibonacci(20) and prints the resulting list of the first 20 Fibonacci numbers.
print(b(number))