from functools import reduce
import time
import math

# 1.
def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

numbers = [2, 3, 4, 5]
print("Product of list:", multiply_list(numbers))


# 2.
def count_case(s):
    upper_case = sum(1 for c in s if c.isupper())
    lower_case = sum(1 for c in s if c.islower())
    return upper_case, lower_case

string = "Hello World!"
upper, lower = count_case(string)
print("Uppercase letters:", upper, "Lowercase letters:", lower)


# 3.
def is_palindrome(s):
    return s == s[::-1]

test_string = "madam"
print(f"Is '{test_string}' a palindrome?", is_palindrome(test_string))


# 4.
def delayed_sqrt(number, milliseconds):
    time.sleep(milliseconds / 1000)  
    return math.sqrt(number)

number = 25100
milliseconds = 2123
result = delayed_sqrt(number, milliseconds)
print(f"Square root of {number} after {milliseconds} milliseconds is {result}")


# 5.
def all_true(tup):
    return all(tup)

test_tuple = (True, True, False)
print("Are all elements true?", all_true(test_tuple))
