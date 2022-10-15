car = {
    'brand': 'BMW',
    'model': '2010'
}

print(car['model'], car.get('brand'))
car['brand'] = 'Ford'
car.update({'model': 2022})
car['Menufacturur'] = 'USA'
car.update({'menufactered in': 'USA'})
print('new', car)

car.pop('model')
car.popitem()
del car['brand']
car.clear()
print('Latest', car)