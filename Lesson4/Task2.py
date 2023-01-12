
with open("TASK2polynomial1.txt", "r") as f:
    poly1 = f.read()


with open("TASK2polynomial2.txt", "r") as f:
    poly2 = f.read()

poly1 = poly1.split(" + ")
poly2 = poly2.split(" + ")

result = {}

for term in poly1:
    coeff, exp = term.split("x^")

    if exp in result:
        result[exp] += int(coeff)
    else:
        result[exp] = int(coeff)

for term in poly2:
    coeff, exp = term.split("x^")

    if exp in result:
        result[exp] += int(coeff)
    else:
        result[exp] = int(coeff)

terms = []

for exp, coeff in result.items():
    terms.append(str(coeff) + "x^" + str(exp))

result_str = " + ".join(terms)

with open("result.txt", "w") as f:
    f.write(result_str)