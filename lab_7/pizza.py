from abc import ABC, abstractmethod
from time import sleep
class Pizza(ABC):
    __filling = []
    name = ""
    dough = ""
    sauce = ""

    @abstractmethod
    def cooking(self):
        pass

    @abstractmethod
    def wrapping(self):
        pass


class SuperPizza():
    def __str__(self):
        print("Эта пицца была упомянута в Rabbit")


class Pepperoni(Pizza):
    def __init__(self):
        self.name = "Пепперони"
        self.dough = "Толстое"
        self.sauce = "Сырный"
        self.__filling = ["Пепперони", "Шампиньоны", "Моцарелла"]
        self.cost = 450

    def cooking(self):
        print("Пицца " + self.name + " готовится")
        sleep(2)
        print(" Пицца готова")

    def wrapping(self):
        print("Пицца " + self.name + " запаковывается")
        sleep(1)
        print("Пицца упакована!")


class Mozarella(Pizza, SuperPizza):
    def __init__(self):
        self.name = "Моцапелла"
        self.dough = "Тонкое"
        self.sauce = "Чесночный"
        self.__filling = ["Моцарелла", "Помидоры", "Базилик"]
        self.cost = 650

    def cooking(self):
        print("Пицца " + self.name + " готовится")
        sleep(2)
        print(" Пицца готова")

    def wrapping(self):
        print("Пицца " + self.name + " запаковывается")
        sleep(1)
        print("Пицца упакована!")


class PizzaBBQ(Pizza):
    def __init__(self):
        self.name = "Барбекю"
        self.dough = "Тонкое"
        self.sauce = "Томатный барбекю"
        self.__filling = ["Курочка", "Томатная паста", "Помидоры"]
        self.cost = 550

    def cooking(self):
        print("Пицца " + self.name + " готовится")
        sleep(2)
        print(" Пицца готова")

    def wrapping(self):
        print("Пицца " + self.name + " запаковывается")
        sleep(1)
        print("Пицца упакована!")