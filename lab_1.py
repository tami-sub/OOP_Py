n = float(input())
f = open("test.txt", 'w+')
"""Открыт или создан файл test.txt в зависимотсти от существования файла с таким названием"""
lst = []
"""Создан список lst"""

def list_filling(n):
    k = 0
    while k < n:
        lst.append(float(input()))
        k = k + 1
"""Заполнение списка"""


def list_changing(local_list):
    local_list = [x * 0.13 for x in local_list]
    local_list.sort()
    return local_list
"""Умножение всех значений списка на 0.13 и сортировка"""

list_filling(n)
lst = list_changing(lst)
for x in lst:
    f.write(str(round(x, 2)) + "\n")
"""Вывод с округлением до 2-х цифр"""
f.close()
"""Файл закрыт"""