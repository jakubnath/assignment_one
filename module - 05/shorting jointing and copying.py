# number = [10,20,30,40,50,60,70]
# number.sort()
# print(number)
#
# number.sort(reverse=True)
# print(number)
#
# number2 = number.copy()
# print(number2)
# number2.append(80)
# print(number2)

numbers = [1, 2, 3]
alphabets = ['a','b','c']
# result_append = numbers.append(alphabets)
# results = numbers+alphabets
# print(results)
# print(result_append)

numbers.extend(alphabets)
print(numbers)