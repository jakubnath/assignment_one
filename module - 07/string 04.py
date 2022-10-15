# 'count', len usage
str1 = 'Python is awesome, isn\'t it?'

print('The totol character count is ', len(str1))

# count method
substring = 'awesome'
print('The substring', substring, 'present ', str1.count(substring), 'times')


substring2 = 'i'
print(str1.count(substring2, 8,20))

# string.count(substring) ---- Return Total count
# string.count(substring, start num, end num) ---- Return Total count between start and end

