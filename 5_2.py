with open("text.txt", "r", encoding="utf-8") as my_f:
    my_lines = my_f.readlines()
    print(f"There are {len(my_lines)} lines in the file")
    for line in my_lines:
        words = len(line.split())
        print(f"The number of words is equal to {words}")
