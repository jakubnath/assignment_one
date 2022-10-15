# split , rsplit , lspilit , splitlines

str1 = "hello, my name is Jakub, \n I am 28 years old"

print(str1.split())     #space
print(str1.split(','))      #comma
print(str1.split(',', maxsplit=1))      # max split

print(str1)
print(str1.splitlines(True))
print(str1.splitlines())