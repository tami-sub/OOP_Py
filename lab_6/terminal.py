from pizza import PizzaBBQ, Pepperoni, Mozarella
from order import Order

import time
import asyncio


async def bake(pizza):
    print("подготовка к испеканию")
    await asyncio.sleep(0)
    pizza.cooking()


async def wrap(pizza):
    print("подготовка к упаковке")
    await asyncio.sleep(0)
    pizza.wrapping()


class Terminal:
    print("Здравствуйте, выберите пиццу: ")
    storage = {1: Pepperoni(), 2: Mozarella(), 3: PizzaBBQ()}
    flag = True
    currentOrder = Order()
    loop = asyncio.get_event_loop()
    while flag:
        print("\n Имеющиеся пиццы \n 1-{0} \n 2-{1} \n 3-{2}".format(storage[1].name, storage[2].name, storage[3].name))
        print("Введите, пожалуйста, номер желаемой пиццы или укажите '0', чтобы закончить заказ")
        try:

            maPizza = int(input())
            if maPizza != 0:
                if currentOrder.add(storage[maPizza]):
                    loop = asyncio.get_event_loop()
                    tasks = [loop.create_task(bake(storage[maPizza])), loop.create_task(wrap(storage[maPizza]))]
                    loop.run_until_complete(asyncio.wait(tasks))
                    storage[maPizza].__str__()
                    currentOrder.__str__()
                else:
                    break
            else:
                break

        except Exception as e:
            print("Произошла ошибка {0} \n Попробуйте ввести значение снова".format(e))
    loop.close()
    currentOrder.change_status()
    currentOrder.__str__()


Terminal()
