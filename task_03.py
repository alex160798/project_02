# Задача 4
# Вывести по номеру месяца кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

user_input = input("Введите номер месяца: ")
month = int(user_input)

def days_in_month(month):
    if month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 28
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        return 'Некорректный номер месяца'

print('Вы ввели', month)
print('Считаем количество дней в месяце...')
print(days_in_month(month))
