"""
person = []

name = input('Enter user name: ')
age = int(input('Enter Age: '))
gender = input('Enter Gender: ')
person.append(name)
person.append(age)
person.append(gender)

print(person)

person = ['jakub', 'male', 45]
person.remove('Male')
del person[0]
print(person)
person.clear()
print(person)


i = 0
fruits = ['apple', 'banana', 'chery', 'orange', 'malon', 'mango']
while i < len(fruits):
    print(fruits[i])
    i += 1
    if fruits[i] == 'chery':
        break

"""

numbers = [212,552,12,5566,85442,25]
numbers.sort(reverse=True)
temp = numbers.copy()
print(numbers)
print(temp)