from time import *


class Journal(object):
    def __new__(cls):
        # Перекрываем создание объекта класса
        if not hasattr(cls, 'instance'):
            cls.instance = super(Journal, cls).__new__(cls)
            current_time = time()
            res = ctime(current_time)
            my_file = open("journal.txt", "a+")
            my_file.write("Новый заказ был начат {0}\n".format(res))
            my_file.close()
        return cls.instance
