my_list = [7, 5, 3, 3, 2]
n = int(input("Enter a natural number: "))
if n > 0:
    my_list.append(n)
    my_list.sort(reverse=True)
    print(my_list)
else:
    print("Invalid input")
