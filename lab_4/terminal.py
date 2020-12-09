from pizza import PizzaBBQ, Pepperoni, Mozarella
from order import Order


class Terminal():
    print("Здравствуйте, выберите пиццу: ")
    storage = {1: Pepperoni(), 2: Mozarella(), 3: PizzaBBQ()}
    flag = True
    currentOrder = Order()
    while flag:
        print("\n Имеющиеся пиццы \n 1-{0} \n 2-{1} \n 3-{2}".format(storage[1].name, storage[2].name, storage[3].name))
        print("Введите, пожалуйста, номер желаемой пиццы или укажите '0', чтобы закончить заказ")
        maPizza = int(input())
        if maPizza != 0:
            storage[maPizza].cooking()
            storage[maPizza].wrapping()
            storage[maPizza].__str__()
            currentOrder.__str__()
        else:
            break
    currentOrder.change_status()
    currentOrder.__str__()

Terminal()
