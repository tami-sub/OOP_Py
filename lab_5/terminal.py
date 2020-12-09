from pizza import PizzaBBQ, Pepperoni, Mozarella
from order import Order
import threading

class Terminal:
    print("Здравствуйте, выберите пиццу: ")
    storage = {1: Pepperoni(), 2: Mozarella(), 3: PizzaBBQ()}
    flag = True
    currentOrder = Order()

    while flag:
        print("\n Имеющиеся пиццы \n 1-{0} \n 2-{1} \n 3-{2}".format(storage[1].name, storage[2].name, storage[3].name))
        print("Введите, пожалуйста, номер желаемой пиццы или укажите '0', чтобы закончить заказ")
        try:
            maPizza = int(input())
            if maPizza != 0:
                if currentOrder.add(storage[maPizza]):

                    thread1 = threading.Thread(target=storage[maPizza].cooking())
                    thread2 = threading.Thread(target=storage[maPizza].wrapping())
                    thread1.start()
                    thread2.start()

                    storage[maPizza].__str__()
                    currentOrder.__str__()
                else:
                    break
            else:
                break
            thread1.join()
            thread2.join()
        except Exception as e:
            print("Произошла ошибка {0} \n Попробуйте ввести значение снова".format(e))
    currentOrder.change_status()
    currentOrder.__str__()


Terminal()
