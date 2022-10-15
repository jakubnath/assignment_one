"""
write a Python program to print a specified list
after removing the 0th, 4th and 5th elements.
Sample List: ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output: ['Green', 'White', 'Black']


sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
sample_list.pop()
sample_list.pop()
sample_list.pop(0)
print(sample_list)

sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

sample_list = [x for (i,x) in enumerate(sample_list) if i not in (0, 4, 5)]
print(sample_list)


seasons = ["Spring", "Summer", "Fall", "Winter"]
count = 1

for season in seasons:
    print(count, season)
    count += 1

"""
"""
seasons = ["Spring", "Summer", "Fall", "Winter"]

for count in range(len(seasons)):
    print(count+1, seasons[count])
"""

# enumerate function

seasons = ["Spring", "Summer", "Fall", "Winter"]

for count, season in enumerate(seasons, start=1):
    print(count, season)
