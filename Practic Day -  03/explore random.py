import random
# number = [10, 20, 30, 555, 22, 888, 333, 55, 44, 854]
#
# random_number = random.choice(number)
#
# print(random_number)

user_name = input('Enter your name: ')
sentences = [
    f'This is {user_name}',
    f'My name is {user_name}',
    f'Hello, I am {user_name}',
    f'Hi, whats up {user_name}'
]
print(random.choice(sentences))