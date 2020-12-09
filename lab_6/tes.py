import asyncio

class Pepperoni():
    def __init__(self):
        self.name = "Pepperoni"
        self.cost = 450

    def cooking(self):
        print("Пицца " + self.name + " готовится \n Пицца готова")

    def wrapping(self):
        print("Пицца " + self.name + " запаковывается \n Пицца упакована!")


async def bake(pizza):
    print("подготовка к испеканию")
    await asyncio.sleep(0)
    pizza.cooking()


async def wrap(pizza):
    print("подготовка к упаковке")
    await asyncio.sleep(0)
    pizza.wrapping()


pizza = Pepperoni()
pizza.cooking()

ioloop = asyncio.get_event_loop()
tasks = [ioloop.create_task(bake(pizza)), ioloop.create_task(wrap(pizza))]
ioloop.run_until_complete(asyncio.wait(tasks))
ioloop.close()