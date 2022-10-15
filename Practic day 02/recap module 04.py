# if <conditional logic>:

#   <code to execute>

# a = 2
# if a > 0:
#     print('Number is positive')
# elif a == 0:
#     print('Number is Zoro')
# else:
#     print('Number is negative')
#
# num_input = -1
# while num_input < 0:
#     str_input = input('Enter positive number: ')
#     num_input = float(str_input)
#
# print('You have entered position number')

# infinite loop
# number = 0
# while number < 5:
#     print(number)
#     number += 1     # number = number +1
#     if number == 3:
#         break

i = 0
while i < 7:
    i = i + 1
    if i == 5:
        continue
    print(i)


