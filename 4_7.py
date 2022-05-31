from math import factorial


def fact(n):
    for i in range(1, n + 1):
        yield factorial(i)


for el in fact(int(input("Enter the number whose factorial you want to get: "))):
    print(el)
