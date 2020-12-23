from pizza import PizzaBBQ, Pepperoni, Mozarella
from order import Order
from tkinter import *
from payment import *
from chief import Chief, Man


class Terminal:
    storage = {1: Pepperoni(), 2: Mozarella(), 3: PizzaBBQ()}
    currentOrder = Order()

    def __init__(self):
        self.current_order = Order()
        self.window = Tk()
        self.window.title("Пиццерия у Луиджи")
        self.window.geometry("480x240")

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
        man = Man('Луиджи')
        man_jet = Chief(man)

        man_jet.say()
        man_jet.do()
        self.window.mainloop()

    def nav(self, currentOrder):
        self.window.geometry("480x540")
        self.main.config(text="Подсчитать итоговую стоимость",
                         command=lambda: (currentOrder.change_status(), currentOrder.__str__(), self.pizzas.destroy(),
                                          self.main.destroy(), self.cost_var.set(currentOrder.__str__()),
                                          self.payment()))

        self.add_pizza(currentOrder)

    def payment(self):
        pay = Frame(self.window)
        pay.pack(side=TOP)

        ph1 = CardPaymentHandler()
        ph2 = ApplePaymentHandler()
        ph3 = BitcoinPaymentHandler()

        ph1.successor = ph2
        ph2.successor = ph3

        choice = Label(pay, text="Выберите тип оплаты", pady="3", font=("Helvetica", 16, "bold"))
        choice.pack(side=TOP)
        pizza_btn1 = Button(pay, text="Оплата картой", command=lambda: (ph1.handle(PaymentMethod(True, False, False)),
                                                                        self.cost_var.set("Ваш заказ успешно оплачен"),
                                                                        pay.destroy()),
                            width="15", font=("Helvetica", 15, "bold"))
        pizza_btn1.pack(side=TOP)

        pizza_btn2 = Button(pay, text="Apple Pay", command=lambda: (ph1.handle(PaymentMethod(False, True, False)),
                                                                    self.cost_var.set("Ваш заказ успешно оплачен"),
                                                                    pay.destroy()),
                            width="15", font=("Helvetica", 15, "bold"))
        pizza_btn2.pack(side=TOP)

        pizza_btn3 = Button(pay, text="Bitcoin", command=lambda: (ph1.handle(PaymentMethod(False, False, True)),
                                                                  pay.destroy(),
                                                                  self.cost_var.set("Ваш заказ успешно оплачен")),
                            width="15", font=("Helvetica", 15, "bold"))
        pizza_btn3.pack(side=TOP)

    def add_pizza(self, order):
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
        try:
            if currentOrder.add(self.storage[maPizza]):
                self.storage[maPizza].templateMethod()
                self.storage[maPizza].__str__()
                self.cost_var.set(currentOrder.__str__())
        except Exception as e:
            print("Произошла ошибка {0} \n Попробуйте ввести значение снова".format(e))
