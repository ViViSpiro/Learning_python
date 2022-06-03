with open("text_4.txt", "r", encoding="utf-8") as my_f:
    list = my_f.readline()
    with open("text_4_rus.txt", "w", encoding="utf-8") as my_f_2:
        print(list.replace("One", "Один"), file=my_f_2, end="")
    list = my_f.readline()
    with open("text_4_rus.txt", "a", encoding="utf-8") as my_f_2:
        print(list.replace("Two", "Два"), file=my_f_2, end="")
    list = my_f.readline()
    with open("text_4_rus.txt", "a", encoding="utf-8") as my_f_2:
        print(list.replace("Three", "Три"), file=my_f_2, end="")
    list = my_f.readline()
    with open("text_4_rus.txt", "a", encoding="utf-8") as my_f_2:
        print(list.replace("Four", "Четыре"), file=my_f_2, end="")
