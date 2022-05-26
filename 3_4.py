def my_func(x, y):
    if x > 0 and y < 0:
        print(x ** y)
    else:
        print("Check the correctness of the entered values!")


x = float(input("Enter a positive number: "))
y = int(input("Enter a negative integer: "))
my_func(x, y)
