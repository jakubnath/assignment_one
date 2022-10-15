bio = {
    'name':'jakub',
    'age':'25 years',
    'location':'coxsbazar'
}

print(bio['name'],bio.get('age'))
print(bio)
bio['name']='jakub nath'
bio['full name']='mr jakub nath'
bio.update({'age':'24 years'})
print(bio)

# Remove Items
bio.pop('name')
bio.popitem()
print(bio)

# accessing keys and values
print(bio.keys())
print(bio.values())

# membership operators
if 'age' in bio.keys():
    print('Your age is ', bio['age'])


print(bio.items())
