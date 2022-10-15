import random
'''
1. list - Name, age
2. Hellow this is Jakub, He is 28 years old
'''
chelebrity_name_list = ['Ananta', 'Rakib', 'Bappa', 'Alam', 'Shombu']
chelebrity_age_list = [25,33,55,66,44]

i = 0
while i < len(chelebrity_name_list):
    chelebrity_name = chelebrity_name_list[i]
    chelebrity_age = chelebrity_age_list[i]


    sentence_one_list = [
        f'Hellow this is {chelebrity_name}.',
        f'Let introduce the celebrity {chelebrity_name}.',
        f'This celebrity is known as {chelebrity_name}.',
        f'{chelebrity_name} is one of the popular celebrity in Internet.',
    ]

    sentence_two_list = [
        f'He is {chelebrity_age} years old.',
        f'His age is {chelebrity_age} years.',
        f'This celebrity\'s age is {chelebrity_age} years.',
        f'{chelebrity_age} years has been passed after the birth of this celebrity.',
    ]



    sentence_one = random.choice(sentence_one_list)
    sentence_two = random.choice(sentence_two_list)



    print(sentence_one, sentence_two)
    i += 1

