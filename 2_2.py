x = list(input("Enter the list items: "))
if len(x) % 2 == 0:
    x[::2], x[1::2] = x[1::2], x[::2]
    print(x)
if len(x) % 2 != 0:
    y = x[-1]
    x.pop()
    x[::2], x[1::2] = x[1::2], x[::2]
    x.append(y)
    print(x)