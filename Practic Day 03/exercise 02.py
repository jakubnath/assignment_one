num = [10, 15, 20, 15, 30, 35]

# option 1
num_list = []
for elem in num:
    if elem%2 == 1:
        num_list.append(elem)
print(num_list)

# option 2
num = [x for x in num if x %2 !=0]
print(num)
