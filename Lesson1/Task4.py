# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarterNum = int(input('Enter quarter number: '))

if quarterNum == 1:
    print('X: 0 - ∞')
    print('Y: 0 - ∞')
elif quarterNum == 2:
    print('X: -∞ - 0')
    print('Y: 0 - ∞')
elif quarterNum == 3:
    print('X: -∞ - 0')
    print('Y: -∞ - 0')
elif quarterNum == 4:
    print('X: 0 - ∞')
    print('Y: -∞ - 0')
else:
    print('ERROR: There is only 4 quarter')