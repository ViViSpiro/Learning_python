class Stock:
    def __init__(self, name, model, price, count):
        self.name = name
        self.model = model
        self.price = price
        self.count = count

    dict = {}

    def incoming(self, article):
        self.article = article.__class__.__name__
        self.dict.setdefault(self.name, [self.model, self.price, self.count]).append(article)


"""    def outgoing(self):
        self.dict.setdefault(name).pop(name)"""


class OfficeEquipment:
    def __init__(self, name, model, price, count):
        self.name = name
        self.model = model
        self.price = price
        self.count = count


class Printer(OfficeEquipment, Stock):
    def __init__(self, name, model, price, count, action):
        super().__init__(name, model, price, count)
        self.action = action
        return

    def function(self):
        self.action = "Printing"
        return self.action


class Scanner(OfficeEquipment, Stock):
    def __init__(self, name, model, price, count, action):
        super().__init__(name, model, price, count)
        self.action = action
        return

    def function(self):
        self.action = "Scanning"
        return self.action


class Copier(OfficeEquipment, Stock):
    def __init__(self, name, model, price, count, action):
        super().__init__(name, model, price, count)
        self.action = action
        return

    def function(self):
        self.action = "Copying"
        return self.action


def reception():
    try:
        name = input(f"Enter the product name: ")
        model = input(f"Enter the product model name: ")
        price = float(input(f"Enter the unit price: "))
        count = int(input(f"Enter the quantity of the product: "))
        product = {name: [model, price, count]}
        stock.dict.update(product)
        print(stock.dict)
    except ValueError:
        print("Invalid value!")


stock = Stock("Printer", "HP Neverstop", 18500, 40)
printer = Printer("Printer", "HP Laser", 12500, 60, "Printing")
stock.incoming(printer)
scanner = Scanner("Scanner", "HP ScanJet", 50700, 55, "Scanning")
stock.incoming(scanner)
copier = Copier("Copier", "Xerox", 38900, 70, "Copying")
stock.incoming(copier)
print(stock.dict)
""""stock.outgoing(Printer)
print(stock.dict)"""
reception()
