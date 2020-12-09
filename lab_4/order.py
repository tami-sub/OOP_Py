def method_friendly_decorator(method_to_decorate):
    def wrapper(self):
        if (self.status == True):
            print("Ваш заказ с учётом НДС стоит: {0}".format(self.finalCost + self.finalCost*0.2))
        else:
            method_to_decorate(self)
    return wrapper


class Order:
    order = []
    finalCost = 0
    status = False

    def add(self, pizza):
            self.order.append(pizza)
            self.finalCost = self.finalCost + pizza.cost

    def change_status(self):
        self.status = True

    @method_friendly_decorator
    def __str__(self):
        return print("Ваш заказ стоит: {0} ".format(self.finalCost))