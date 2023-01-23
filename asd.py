# # Напишите программу вычисления арифметического выражения заданного строкой. 

# data = input()

# data = data.replace('+', ' + ').replace('-', ' - ').replace('+', ' + ').replace('*', ' * ').replace('/', ' / ')
# data = data.split()
# print(data)

# operat = {
#     '+': lambda x, y: int(x) + int(y),
#     '-': lambda x, y: int(x) + int(y),
#     '*': lambda x, y: int(x) + int(y),
#     '/': lambda x, y: int(x) + int(y)
# }

# def calc(data: list) -> int:
#     for i in range(len(data) - 1):
#         if data[i] in '*/':
#             operation = data[i]
#             left = data[i - 1]
#             right = data[i + 1]
#             res = operat[operation](left, right)
#             return data[:i - 1] + res + data[i + 1:]
#         elif data[i] in '-+' and i != 0:
#             operation = data[i]
#             left = data[i - 1]
#             right = data[i + 1]

print(2%1)
