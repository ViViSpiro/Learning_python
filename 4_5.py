from functools import reduce

my_list = [n for n in range(100, 1001) if n % 2 == 0]
result = reduce(lambda x, y: x * y, my_list)
print(my_list)
print(result)
