f = open("test.txt", 'w+')  # Откры/создан файл test.txt в зависимотсти от существования файла с таким названием 
# Достоинства txt: -простота - экономичность


def list_filling():  # Ввод значений через пробел, а затем изменение типа элементов списка
    temp = input().split(' ')
    temp = [float(x) for x in temp]
    return temp


def list_changing(local_list):  # Умножение всех значений списка на 0.13 и сортировка
    local_list = [x * 0.13 for x in local_list]
    local_list.sort()
    return local_list


def list_rounding(local_list):  # Округление элементов списка до двух знаков
    return [round(x, 2) for x in local_list]


def list_writing(local_list):  # Запись значений в файл
    for x in local_list:
        f.write(str(x) + "\n")


lst = list_filling()
lst = list_changing(lst)
lst = list_rounding(lst)
list_writing(lst)

f.close()  # Закрытие файла на запись
