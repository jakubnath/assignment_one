# A company decided to give bonus of 50 to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount
# problem 1
"""
salary = int(input('Enter your salary: '))
years = int(input('Enter your job years: '))

if years > 5:
    print ('You will get',int((salary * 5)/100),'TK bonus')
else:
    print('you will not get bonus')
"""
# problem 2

"""
unit_price = 100
quantity = int(input('Enter your quantity: '))
total_sale = unit_price * quantity

if total_sale > 1000:
    print('Total Cost = ', int(total_sale - (total_sale * 10)/100), 'TK Only')



# problem 3


age = int(input('Your Age: '))
gender = input('Gender(M/F): ')

if gender == 'F':
    print('Your service area is urban')
elif gender == 'M' and age >= 20 and age <= 40:
    print('you service area is anywhere')
elif gender == 'M' and age >= 40 and age <= 60:
    print('Your service area is urban')
else:
    print('ERROR')

# problme 3/ alternative solution    

gender = input('Gender(M/F): ')

if gender == 'F':
    print('Your service area is urban')
elif gender == 'M':
    age= int(input('Your Age: '))
    if age >= 20 and age <= 40:
        print('you service area is anywhere')
    elif age >= 40 and age <= 60:
        print('Your service area is urban')
else:
    print('ERROR')

"""

# problem 4
# number = int(input('Write a random number: '))
#number = input('Write a random numer')
# number = '1234'
# # #sum = int(number[0])+int(number[1])+int(number[2])+int(number[4])
# # sum = int(number[0])+int(number[1])+int(number[2])+int(number[3])
# # print(sum)
# # print(type(sum))

number = int(input('Enter Random Numbers: '))

while number[]



