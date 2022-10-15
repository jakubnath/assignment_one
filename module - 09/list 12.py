program_lan = ['Python', 'Java', 'Javascript', 'asp']
num_list = [1,2,3,4,4,6,7]

# programing_lan = program_lan.copy()
# del program_lan
#
# print(programing_lan)

# program_lan.extend(num_list)
# print(program_lan)


#sort

# num_list.sort(reverse=True)
# print(num_list)

# num_list.reverse()
# print(num_list)

program_lan.sort(key=str.lower)
print(program_lan)

