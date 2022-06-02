my_f = open("text.txt", "w", encoding="utf-8")
while True:
    lines = input("Enter the text or press Enter twice to exit: ")
    if not lines:
        break
    my_f.write(f"{lines}\n")
my_f.close()
