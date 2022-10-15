# name = input('Enter your name: ')
# if name == '':
#     print('Hi', name)

number = int(input('Enter a positive Number: '))

while number < 0:
    number = int(input('Enter a positive Number: '))

print('Square root of', number, 'is', number ** 0.5)