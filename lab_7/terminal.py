from pizza import PizzaBBQ, Pepperoni, Mozarella
from order import Order
import asyncio
from tkinter import *


async def bake(pizza):
    print("подготовка к испеканию")
    await asyncio.sleep(0)
    pizza.cooking()


async def wrap(pizza):
    print("подготовка к упаковке")
    await asyncio.sleep(0)
    pizza.wrapping()


class Terminal:
    storage = {1: Pepperoni(), 2: Mozarella(), 3: PizzaBBQ()}
    currentOrder = Order()

    def __init__(self):
        self.current_order = Order()
        self.window = Tk()
        self.window.title("Пиццерия у Луиджи")
        self.window.geometry("480x240")
        self.window.configure()

        header = Label(self.window, text="Molto bene это Pizza!", font=("Helvetica", 20, "bold"), pady="15")

        self.pizzas = Frame(self.window)
        self.cost_var = StringVar()
        self.cost = Label(self.window, textvariable=self.cost_var, font=("Helvetica", 16, "italic"),
                         fg="grey", anchor="s")

        nav = Frame(width="6")
        self.main = Button(nav, text="Сделать заказ", command=lambda: self.nav(self.current_order),
                           width="100", font=("Helvetica", 20), pady="10")
        self.exit = Button(nav, text="Выход", command=lambda: self.window.destroy(),
                           width="100", font=("Helvetica", 20), pady="10")

        header.pack(side=TOP)
        self.main.pack()
        self.exit.pack()
        self.cost.pack(side=BOTTOM)
        nav.pack(side=BOTTOM)
        self.pizzas.pack(side=TOP)

    def start(self):
        self.window.mainloop()

    def nav(self, currentOrder):
        self.window.geometry("480x540")
        self.main.config(text="Подсчитать итоговую стоимость",
                         command=lambda: (currentOrder.change_status(),currentOrder.__str__(), self.pizzas.destroy(),
                                          self.main.destroy(), self.cost_var.set(currentOrder.__str__())))
        self.add_pizza(currentOrder)

    def add_pizza(self, order):
        asyncio.get_event_loop()
        choice = Label(self.pizzas, text="Выберите свою пиццу", pady="3", font=("Helvetica", 16, "bold"))
        choice.pack(side=TOP)

        pizza_btn1 = Button(self.pizzas, text="{0} \n{1} рублей".format(self.storage[1].name, self.storage[1].cost),
                            command=lambda: self.choosePizza(1, order), width="15", font=("Helvetica", 15, "bold"))
        pizza_btn1.pack(side=TOP)

        pizza_btn2 = Button(self.pizzas, text="{0} \n{1} рублей".format(self.storage[2].name, self.storage[2].cost),
                            command=lambda: self.choosePizza(2, order), width="15", font=("Helvetica", 15, "bold"))
        pizza_btn2.pack(side=TOP)

        pizza_btn3 = Button(self.pizzas, text="{0} \n{1} рублей".format(self.storage[3].name, self.storage[3].cost),
                            command=lambda: self.choosePizza(3, order), width="15", font=("Helvetica", 15, "bold"))
        pizza_btn3.pack(side=TOP)

    def choosePizza(self, maPizza, currentOrder):
        asyncio.get_event_loop()
        try:
            if currentOrder.add(self.storage[maPizza]):
                loop = asyncio.get_event_loop()
                tasks = [loop.create_task(bake(self.storage[maPizza])), loop.create_task(wrap(self.storage[maPizza]))]
                loop.run_until_complete(asyncio.wait(tasks))
                self.storage[maPizza].__str__()
                self.cost_var.set(currentOrder.__str__())
        except Exception as e:
            print("Произошла ошибка {0} \n Попробуйте ввести значение снова".format(e))
