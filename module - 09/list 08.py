program_lan = ['Python', 'Java', 'Javascript']
# newlist = []
#
# for elem in program_lan:
#     newlist.append(elem.upper())
#
# print(newlist)

newlist = [elem.upper() for elem in program_lan]

print(newlist)

num_list = [1, 2, 3, 4, 5, 6, 7, 8]
new_num_list = [x for x in num_list if x%2 ==0]

print(new_num_list)

# new_list = [expression for x in (list/set/tuple) if condition == true]