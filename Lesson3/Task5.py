# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

fib1 = 1
fib2 = 1
num = int(input('Enter a number for the desired sequence: '))
fib_list = [fib1, fib2]

for i in range(num - 2):
    fib1, fib2 = fib2, fib1 + fib2
    fib_list.append(fib2)

negfib_list = list(reversed(fib_list))

for i in range(len(negfib_list)):
    negfib_list[i] *= -1
else:
    negfib_list.append(0)

res_list = negfib_list + fib_list

print(f'For the number {num}, the Fibonacci and Negafibonacci sequence: ')
print(len(res_list) * '⇩⇩⇩⇩')
print(res_list)
print(len(res_list) * '⇧⇧⇧⇧')
