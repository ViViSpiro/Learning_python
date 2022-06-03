with open("text_3.txt", "r", encoding="utf-8") as my_f:
    salary = []
    sename = []
    my_list = my_f.read().split("\n")
    for el in my_list:
        el = el.split()
        if float(el[1]) < 20000:
            sename.append(el[0])
        salary.append(el[1])
print(f"Оклад меньше 20000 у следующих сотрудников: {sename}. "
      f"Средняя зарплата равна {sum(map(float, salary)) / len(salary)}.")
