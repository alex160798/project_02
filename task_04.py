# Задача 4
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут
# Для того, чтобы задавать случайные значения, используйсте модуль random

# import random as r
import numpy as np

def length_calculator(songs_list, *args):
    '''
    Демонстрационная функция для отработки args, enumerate и др.
    Получает список песен в формате: [песня, ее длительность],
    а также номера песен, для которых считаем общую длину.
    Возвращает общую длину в фомате float c округлением до сотых
    '''
    total_length = 0

    for i, elem in enumerate(args):
        total_length += songs_list[elem][1]

    return round(total_length, 2)


my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

r_lst = np.random.randint(0, len(my_favorite_songs), size=3)
# Можно заменить на random.choice(), но функция потребует 
# соотвествующей переработки

result = length_calculator(*r_lst, songs_list=my_favorite_songs)

print('Три песни звучат', result, 'минут(ы)')
