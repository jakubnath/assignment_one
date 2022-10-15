import random
mobile_list = [
    {'name':'Iphone 22', 'price': 150000},
    {'name':'Nokia 23', 'price': 50000},
    {'name':'Huwai 24', 'price': 35000},
    {'name':'Xiaomi 4', 'price': 39000},
    {'name':'Samsung 5', 'price': 20000},
]

# Iphone 22 price is 150000

for mobile in mobile_list:
    text = [
        f'{mobile.get("name")} price is {mobile.get("price")} BDT.',
        f'The price of {mobile.get("name")} is {mobile.get("price")} BDT.'
    ]
    print(random.choice(text))
