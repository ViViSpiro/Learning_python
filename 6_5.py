class Stationary:
    title = "stationary"

    def draw(self):
        print("Starting drawing")


class Pen(Stationary):

    def draw(self):
        self.title = "pen"
        print(f"Draw with a {self.title}")


class Pencil(Stationary):

    def draw(self):
        self.title = "pencil"
        print(f"Draw with a {self.title}")


class Handle(Stationary):

    def draw(self):
        self.title = "handle"
        print(f"Draw with a {self.title}")


stationary = Stationary()
stationary.draw()
pen = Pen()
pencil = Pencil()
handle = Handle()
pen.draw()
pencil.draw()
handle.draw()
