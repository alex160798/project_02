# Задача 6
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.
import random as r

my_favorite_songs = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}


def length_calculator(songs_dict: dict, count: int) -> float:
    '''
    Function receives songs dict {song_name: lenth}
    Returns sum of lengths of 'count' random songs (float)
    '''
    total_length = 0
    random_songs = r.choices(list(songs_dict.keys()), k=count)

    for key, value in songs_dict.items():
        if key in random_songs:
            total_length += value

    return round(total_length, 2)


result = length_calculator(my_favorite_songs, 3)

print('Три песни звучат', result, 'минут(ы)')
