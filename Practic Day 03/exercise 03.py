"""

num = [10, 15, 20, 15, 30, 35]

for elem in num:
    print(elem, '--', num.index(elem))

# option 2

for elem in num:
    print(str(elem).zfill(2),'---',num.index(elem))

"""

list1 = [10, 20, 30]
list2 = [40, 50, 60]

list2.extend(list1)
print(list2)
list2.sort(reverse=True)
print(list2)