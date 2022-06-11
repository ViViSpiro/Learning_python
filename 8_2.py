class DivisionByZero(Exception):
    def __init__(self, alarm_text):
        self.alarm_text = alarm_text


def division():
    try:
        divisible = float(input("Enter the divisible: "))
        divisor = float(input("Enter the divisor: "))
        if divisor == 0:
            raise DivisionByZero("Division by zero is impossible!")
    except ValueError:
        print("It's not a number!")
    except DivisionByZero as err:
        print(err)
    else:
        result = divisible / divisor
        print(f"Division result: {result:.2f}.")


division()
