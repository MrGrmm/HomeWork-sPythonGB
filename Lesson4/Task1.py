


import random

def generate_coefficients(degree):
    return [random.randint(0, 100) for _ in range(degree + 1)]

def write_polynomial(coefficients, file):
    with open(file, 'w') as f:
        for i, coefficient in enumerate(coefficients):
            if coefficient != 0:
                if i == 0:
                    f.write(str(coefficient))
                elif i == 1:
                    f.write(f'{coefficient}*x')
                else:
                    f.write(f'{coefficient}*x^{i}')
                if i != len(coefficients) - 1:
                    f.write(' + ')

k = int(input('Enter natural power k: '))
coefficients = generate_coefficients(k)
print(f'Random coefficients:  {coefficients}')
write_polynomial(coefficients, 'polynomial.txt')
coefficients2 = generate_coefficients(k)
print(f'Random coefficients:  {coefficients2}')
write_polynomial(coefficients2, 'polynomial2.txt')




