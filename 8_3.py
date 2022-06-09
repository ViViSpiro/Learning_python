class NotANumber(Exception):
    pass


numeric_list = []
while True:
    try:
        value = input("Enter a number and press Enter: ")
        if value == "q":
            break
        if not value.isdigit():
            raise NotANumber(value)
        numeric_list.append(int(value))
    except NotANumber as err:
        print("It's not a number!", err)
print(numeric_list)
