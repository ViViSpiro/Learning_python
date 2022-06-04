from time import sleep


class TrafficLight:
    __color = {"red": 7, "yellow": 2, "green": 6}

    def running(self):
        for keys, values in self.__color.items():
            print(keys)
            sleep(values)


t = TrafficLight()
t.running()
