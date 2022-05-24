def my_f(num_1, num_2):
    try:
        n_1 = num_1
        n_2 = num_2
        print(n_1 / n_2)
    except (ZeroDivisionError) as Error:
        print(Error)


num_1 = int(input("Enter the divisible: "))
num_2 = int(input("Enter the divisor: "))
my_f(num_1, num_2)
