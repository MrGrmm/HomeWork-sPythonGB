# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

numDayOfWeek = int(input('Enter the num 1-7: '))
saDay = 6
suDay = 7

if numDayOfWeek == saDay:
    print(f"{numDayOfWeek}, it's Saturday, it is a weekend")
elif numDayOfWeek == suDay:
    print(f"{numDayOfWeek}, it's Saturday, it is a weekend")
elif numDayOfWeek in range(1,6):
    print(f"{numDayOfWeek}, it's a weekday")
else:
    print('ERROR: There are only 7 days in a week')

# Стоун, хочу понять почему любая цифра идёт к print('Yes') если написать:

# if numDayOfWeek == saDay or suDay:
#     print('Yes')
# elif numDayOfWeek == 1 or 2 or 3 or 4 or 5:
#     print('No')
# else:
#     print('Error')

#Заранее спасибо за ответ!!

