name = 'jakub nath'
print(name.upper())
print('Capitalize: ', name.capitalize())
print('Title: ', name.title())

heading = ' This is a  post title '
# Step 1: remove spaces from text
# Step 2: replace double space with single space
# convert all letter to lowercase
# this-is-a-post-title // replace single space with

print('initial')
print(heading)
heading = heading.strip()
print('After Striping')

heading = heading.replace('  ',' ')
print(heading)
heading = heading.lower()
print(heading)
slug = heading.replace(' ','-')
print(slug)