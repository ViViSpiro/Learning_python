with open("text_5.txt", "w+", encoding="utf-8") as my_f:
    line = my_f.write("5 13 49 55 66 77 3 9 2 42 81 23 9")
    my_f.seek(0)
    my_list = my_f.read().split()
    print(sum(map(int, my_list)))
