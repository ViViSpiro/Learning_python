from sys import argv


def salary():
    try:
        script_name, hours, rate, bonus = argv
        print(f"Salary = {(float(hours) * float(rate)) + float(bonus)}")
    except ValueError:
        print("Enter the correct data!")


salary()
