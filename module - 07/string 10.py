str1 = "jakub"
str2 = "Jakub \t Nath"
str3 = "coxs bazar"


print(len(str1))
print(str1.center(20,"*"))
print(str1.ljust(20,"*"))
print(str1.rjust(20,"*"))

print(str2)
print(str2.expandtabs(20))
print(str2.expandtabs(50))
print(str2.expandtabs(5))

mylist = ['My', 'name', 'is', 'Jakub']

str6 = ' '.join(mylist)
print(str6)

# slicing

print(mylist[2])

print(str3[1])

# string[start, end]
print(str3[:8])