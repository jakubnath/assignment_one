# Write a Python program that accepts an integer(n) and
# computes the value of n + nn + nnn.
# 5+55+555 =

number = input('Enter Number: ')
result = number + (number * 2) + (number * 3)

print(result)

result = int(number) + int(number * 2) + int(number * 3)

print(result)


# Write a Python program to sum of the first n positive integers.
# 1+2+3+4+6+7+8 =

num1 = int(input('Enter any positive Number: '))
sum = num1 * (num1 + 1) / 2
print(int(sum))
