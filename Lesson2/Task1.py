# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

while True:
    try:
        num = input('Input your num: ').replace(',','').replace('-','')
        sum = 0

        for i in range(len(num)):
            sum += int(num[i])
        break
    except:
        print('Try again')    
print(sum)