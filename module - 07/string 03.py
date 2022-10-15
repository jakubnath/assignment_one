"""
'isalnum', 'isalpha', 'isascii', 'isprintable', 'isnumberic', 'isdecimal', 'isdigit', i
"""

num1 = '1234567889'
str1 = 'éè'

print(num1.isalnum())
print(num1.isnumeric())
print(num1.isdecimal())
print(num1.isdigit())

print(num1.isalpha())
print(num1.isprintable())

print(str1.isascii())
