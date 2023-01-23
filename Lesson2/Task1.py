# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

while True:
    try:
        num = input('Input your num: ').replace(',','').replace('-','')
        print(sum(list(map(int, [item for item in num]))) )       #
        # sum_of_dig = 0

        # for i in range(len(num)):
        #     sum += int(num[i])

        # print(f"Sum of digit's = {sum_of_dig}")
        break
    except:
        print('Try again')    



