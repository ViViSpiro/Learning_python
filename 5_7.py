import json

with open("text_7.txt", "r", encoding="utf-8") as my_f:
    my_dict_1 = {el.split()[0]: int(el.split()[2]) - int(el.split()[3]) for el in my_f}
    profit = [r for r in my_dict_1.values() if r > 0]
    my_dict_2 = {"average_profit": round(sum(profit) / len(profit))}
    my_list = [my_dict_1, my_dict_2]

with open("text_77.json", "w", encoding="utf-8") as my_j:
    json.dump(my_list, my_j, ensure_ascii=False)
