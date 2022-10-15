# raw string
path = r'G:\jakubnath\'coxsbazar'
print(path)

name = 'Jakub'
age = 28
gender = 'male'
earning = '50 BDT daily'

# my Name is Jakub. I am 28 years old. I am male. My daily income is 5000

print('My name is ', name, '. I am ', age, ' years old. I am ', gender, '. my daily income is ', earning, sep="")

print('My name is '+name+'. I am '+str(age)+' years old. I am '+gender+'. my daily income is '+earning)

print(f'my Name is {name}. I am {age} years old. I am {gender}. My daily income is {earning}')