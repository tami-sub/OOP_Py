from exeptions import MaxPizzaAmount, Discount
from journal import Journal


class Order:
    order = []
    finalCost = 0
    status = False

    def add(self, pizza):
        try:
            if len(self.order) == 15:
                raise MaxPizzaAmount(len(self.order))

            else:
                self.order.append(pizza)
                self.finalCost = self.finalCost + pizza.cost
                Journal()
                if len(self.order) > 3:
                    raise Discount
                return True
        except MaxPizzaAmount as e:
            e.__str__()
        except Discount as e:
            self.finalCost = self.finalCost * 0.95
            e.__str__()
            return True

    def change_status(self):
        self.status = True

    def __str__(self):

        if self.status:
            return "Ваш заказ с учётом НДС стоит: {0}".format(self.finalCost + self.finalCost * 0.2)
        else:
            return "Ваш заказ стоит: {0} ".format(self.finalCost)
