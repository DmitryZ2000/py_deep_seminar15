# Разработайте программное обеспечение для ведения журнала событий. Вам необходимо создать класс,
# который будет представлять строки журнала и включать в себя информацию об авторе и времени создания каждой записи.
# Условие задачи:
# Создайте класс MyStr, который наследуется от встроенного класса str и добавлять дополнительную
# информацию о создателе строки и времени ее создания. Этот класс будет представлять строки с информацией о событиях.
# Класс MyStr должен иметь следующие атрибуты и методы:
# value (str): Строковое значение с описанием события.
# author (str): Имя автора, создавшего запись.
# time: Время создания записи в формате '%Y-%m-%d %H:%M'.
# Магические методы (Dunder-методы):
# Реализуйте метод __new__(cls, value, author), который создает новый объект класса MyStr с
# заданным value и author. Метод также автоматически фиксирует время создания записи.
# В этом методе создается новый объект MyStr с указанными атрибутами и текущим временем в атрибуте time.
# Реализуйте метод __str__(self), который возвращает строковое представление объекта
# класса MyStr с информацией о событии, авторе и времени создания.
# Реализуйте метод __repr__(self), который возвращает строковое представление объекта класса MyStr.
# Метод __repr__ возвращает строку, которая может быть использована для создания точно
# такого же объекта MyStrс теми же значениями value и author.

# Пример использования.
# На входе:
# event = MyStr("Завершилось тестирование", "John")
# print(event)
# На выходе:
# Завершилось тестирование (Автор: John, Время создания: [ в формате '%Y-%m-%d %H:%M'])

# На входе:
# my_string = MyStr("Пример текста", "Иван")
# print(my_string)
# На выходе:
# Пример текста (Автор: Иван, Время создания: 2023-10-10 15:56)

# На входе:
# my_string = MyStr("Мама мыла раму", "Маршак")
# print(repr(my_string))
# На выходе:
# MyStr('Мама мыла раму', 'Маршак')

import time
from datetime import datetime
import logging
import argparse

class MyStr(str):
    """
    Класс для создания строки с информацией об авторе и времени создания.
    Атрибуты:
    value (str): строковое значение.
    author (str): имя автора.
    Dunder методы:
    __new__(cls, value, author): создает новый объект класса.
    __str__(): возвращает строковое представление объекта класса.
    __repr__(): возвращает строковое представление объекта класса для отладки.
    """

    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        instance.author = author       
        # instance.time = str(datetime.now())[:-10]
        instance.time = str(time.asctime())
        return instance

    # def __init__(self, value, author):
    #     self.value = value
    #     self.author = author

    def __str__(self):
        """Attention!!! Для вывода самой строки используется вызов родительского класса str, \
а именно super().__str__()"""
        # return f'{self.value} (Автор: {self.author}, Время создания: {self.time})'
        return f'{super().__str__()} (Source: {self.author}, Время создания: {self.time})'        

    def __repr__(self):
        # return f"MyStr('{self.value}', '{self.author}')"
        return f"MyStr('{super().__str__()}', '{self.author}')"

if __name__ =="__main__":
    FORMAT = '{levelname:<6}, {asctime}, {name}, {msg}'
    logging.basicConfig(format=FORMAT, style='{', filename='GrandLogger.log', filemode='a', encoding='utf-8', level=logging.INFO)
    logger = logging.getLogger('GrandLogger')  

    event = MyStr("Завершилось тестирование", "John")
    logger.info(f'{event}')
    
    event = MyStr("Пример текста", "Иван")
    logger.info(f'{event}')

    event = MyStr("Мама мыла раму", "Маршак")
    logger.info(f'{event}')
    # print(event.__str__.__doc__)

    parser = argparse.ArgumentParser(description="Adding event info")
    parser.add_argument('-new_str', metavar='new_str', type=str, help='New entry about new event', default='New noname event')
    parser.add_argument('-athor', metavar='athor', type=str, help='Athor of event', default='SuperUser')
    args = parser.parse_args()

    event = MyStr(args.new_str, args.athor)
    logger.info(f'{event}')

