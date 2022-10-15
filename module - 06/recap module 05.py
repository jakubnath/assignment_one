"""
gender = input('Enter M/F: ')
if gender.lower() == 'm':
    gender = 'male'
    pronoun = 'He'
    relative_pronoun = 'his'
else:
    gender = 'Female'
    pronoun = 'She'
    relative_pronoun = 'Her'

print(gender,pronoun, relative_pronoun)

i = 1
while i < 20:
    print(i)
    i += 2
"""

person = ['Jakub Nath', 28, True]
print(person[0])
if person[2] == True:
    merital_status = 'Married'
else:
    marital_status = 'Single'
template = f'This is {person[0]}. I am {person[1]}. I am {merital_status}'
print(template)

fruits = ['apple', 'banana', 'chery', 'orange', 'malon', 'mango']
print(fruits[3:])

if 'apple' in fruits:
    print('He eats apple')
else:
    print('He doesn\'t eat apple')






