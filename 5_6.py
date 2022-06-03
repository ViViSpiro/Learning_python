my_dict = {}
with open("text_6.txt", "r+", encoding="utf-8") as my_f:
    for el in my_f:
        el = el.replace("(пр)", " ").replace("(л)", " ").replace("(лаб)", " ").replace("-", " ")
        my_dict[el.split()[0]] = sum(map(int, el.split()[1:]))
    print(my_dict)


