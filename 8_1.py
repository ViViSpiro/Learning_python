from datetime import date


class Date:

    def __init__(self, my_date):
        self.my_date = str(my_date)

    @classmethod
    def extraction(cls, my_date):
        my_date_2 = []
        for i in my_date.split("-"):
            my_date_2.append(i)
        return cls.validation(int(my_date_2[2]), int(my_date_2[1]), int(my_date_2[0]))

    @staticmethod
    def validation(year, month, day):
        try:
            d = date(year, month, day)
            return print(f"{d.day:02d}:{d.month:02d}:{d.year:04d}")
        except ValueError:
            print(f"Incorrect date!")


Date.extraction("08-06-2022")
Date.extraction("31-02-1999")
