from abc import ABC, abstractmethod


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
        print("Эта пицца была упомянута в JoJo")


class Pepperoni(Pizza):
    def __init__(self):
        self.name = "Пепперони"
        self.dough = "Толстое"
        self.sauce = "Сырный"
        self.__filling = ["Пепперони", "Шампиньоны", "Моцарелла"]
        self.cost = 450

    def cooking(self):
        print("Пицца " + self.name + " готовится \n Пицца готова")

    def wrapping(self):
        print("Пицца " + self.name + " запаковывается \n Пицца упакована!")


class Mozarella(Pizza, SuperPizza):
    def __init__(self):
        self.name = "Моцапелла"
        self.dough = "Тонкое"
        self.sauce = "Чесночный"
        self.__filling = ["Моцарелла", "Помидоры", "Базилик"]
        self.cost = 650

    def cooking(self):
        print("Пицца " + self.name + " готовится \n Пицца готова")

    def wrapping(self):
        print("Пицца " + self.name + " запаковывается \n Пицца упакована!")


class PizzaBBQ(Pizza):
    def __init__(self):
        self.name = "Барбекю"
        self.dough = "Тонкое"
        self.sauce = "Томатный барбекю"
        self.__filling = ["Курица", "Томатная паста", "Помидоры"]
        self.cost = 550

    def cooking(self):
        print("Пицца " + self.name + " готовится \n Пицца готова")

    def wrapping(self):
        print("Пицца " + self.name + " запаковывается \n Пицца упакована!")


class Order:
    order = []
    count = 0

    def add(self, pizza):
        self.order.append(pizza)
        self.count = self.count + pizza.cost

    def __str__(self):
        return print("Ваш заказ стоит: {0}".format(self.count))


class Terminal():
    print("Здравствуйте, выберите пиццу: ")
    storage = {1: Pepperoni(), 2: Mozarella(), 3: PizzaBBQ()}

    currentOrder = Order()
    while True:
        print("\n Имеющиеся пиццы \n 1-{0} \n 2-{1} \n 3-{2}".format(storage[1].name, storage[2].name, storage[3].name))
        print("Введите, пожалуйста, номер желаемой пиццы или укажите '0', чтобы закончить заказ")
        maPizza = int(input())
        if maPizza != 0:
            currentOrder.add(storage[maPizza])
            storage[maPizza].cooking()
            storage[maPizza].wrapping()

            storage[maPizza].__str__()
            currentOrder.__str__()
        else:
            break
    currentOrder.__str__()


Terminal()
