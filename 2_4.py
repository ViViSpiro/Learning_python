s = input("Enter a set of words separated by a space: ").split()
for ind, el in enumerate(s, 1):
    if len(el) > 10:
        print(ind, el[:10])
    else:
        print(ind, el)
