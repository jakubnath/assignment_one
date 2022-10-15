# number = float(input('Enter any number: '))

ch = 'y'
sum = 0
while ch.lower() == 'y':
    number = float(input('Enter any number: '))
    sum += number
    ch = input('Do you want to continue(y/n): ')
print('Total sum', sum)