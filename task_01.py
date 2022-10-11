# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

# v1
print(my_favorite_songs[0:14])
print(my_favorite_songs[-13:])
print(my_favorite_songs[16:30])
print(my_favorite_songs[-26:-15])

# что еще можно использовать
print(my_favorite_songs.find('Was')) # 0
print(my_favorite_songs.find('ent')) # 11 + 3 = 14
print()
print(my_favorite_songs.rfind('New')) # 64
print(my_favorite_songs.rfind('tion')) # 73

# как хотелось
print(my_favorite_songs.split(', ')[0])
print(my_favorite_songs.split(', ')[-1])
print(my_favorite_songs.split(', ')[1])
print(my_favorite_songs.split(', ')[-2])
