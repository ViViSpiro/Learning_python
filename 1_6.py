a = float(input(2))
b = float(input(3))
day = 1
while a < b:
    a = (a * 0.1) + a
    day = day + 1
    print(day)

