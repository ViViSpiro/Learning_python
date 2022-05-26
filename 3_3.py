def my_func(a_1, a_2, a_3):
    print(sum([a_1, a_2, a_3]) - min(a_1, a_2, a_3))

a_1 = int(input("Enter a number: "))
a_2 = int(input("Enter a number: "))
a_3 = int(input("Enter a number: "))
my_func(a_1, a_2, a_3)
