# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

num = int(input('Enter a decimal number: '))
num_for_res = num
res = ''

while num != 0:
    res = str(num % 2) + res
    num //= 2

print(f'Number {num_for_res} in binary number system = {int(res)}')
