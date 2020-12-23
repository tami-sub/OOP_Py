class Man:

    def __init__(self, name):
        self._name = name

    def say(self):
        print('Привет! Меня зовут %s!' % self._name)


class Chief:

    def __init__(self, man):
        self._man = man

    def __getattr__(self, item):
        return getattr(self._man, item)

    def do(self):
        print('%s готов принимать заказ!' % self._man._name)

