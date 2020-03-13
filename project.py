# Задание №2 "Ханойские башни"

# Количество дисков на первом стержне
number = int(input('Введите количество дисков на первом стержне: '))

def rod(number, where_from, where):
    if number != 0:
        additional = 6 - where_from - where
        # Перекладываем n - 1 элементов на вспомогательный стержень
        rod(number - 1, where_from, additional)
        
        # Перекладываем наибольший диск на итоговый стержень
        print('Переместить диск с ', where_from, 'на', where)

        # Перекладываем n - 1 дисков на итоговый стержень
        rod(number - 1, additional, where)

rod(number, 1, 3)