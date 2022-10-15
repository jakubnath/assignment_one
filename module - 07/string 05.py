# endswith, startswith, index, rindex

str1 = 'python is awesome, is not it? I love python'

print(str1.endswith('on'))
print(str1.endswith('o'))

print(str1.startswith('p'))
print(str1.startswith('on'))

print(str1.index('is', 8))
print(str1.rindex('is'))