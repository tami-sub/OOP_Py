class MaxPizzaAmount(Exception):

    def __init__(self, count):
        self.count = count

    def __str__(self):
        return print("Вы заказали максимально возможное количесвто пицц за один заказ: {0} шт".format(self.count))

class Discount(Exception):
    def __str__(self):
        return print("Вы получаете скидку на всю сумму заказа в размере 5% с каждой новой пиццей после заказанных 3-х")
