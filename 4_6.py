from itertools import cycle
from itertools import count

my_inter = count(3)
my_cycle = cycle("NEXT")
for el in range(8):
    print(next(my_inter), next(my_cycle))
