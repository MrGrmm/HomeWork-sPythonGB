import random

def generate_random_polynomial(k):
    coefficients = [random.randint(0, 100) for _ in range(k+1)]
    return coefficients

def write_polynomial_to_file(coefficients, filepath):
    with open(filepath, 'w') as f:
        for i, c in enumerate(coefficients):
            if c != 0:
                if c > 0 and i != 0:
                    f.write(' + ')
                f.write(str(c))
                if i > 0:
                    f.write('x')
                    if i > 1:
                        f.write('^' + str(i))
        f.write(' = 0')

k = int(input('Enter natural degree k: '))
coefficients = generate_random_polynomial(k)
write_polynomial_to_file(coefficients, 'TASK1polynomial.txt')