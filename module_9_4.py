# Module_9_4
#
# Домашнее задание по теме "Создание функций на лету"

import random

# Ваша задача:
# Цель: освоить на практике замыкание, объекты-функторы и lambda-функции.
#
# Задача "Функциональное разнообразие":
#
# Lambda-функция:
# Даны 2 строки:

first = 'Мама мыла раму'
second = 'Рамена мало было'

# Необходимо составить lambda-функцию для следующего выражения - list(map(?, first, second)).
# Здесь ? - место написания lambda-функции.
# Результатом должен быть список совпадения букв в той же позиции:
# [False, True, True, False, False, False, False, False, True, False, False, False, False, False]
# Где True - совпало, False - не совпало.

print(list(map(lambda x, y: x == y, first, second)))


# Замыкание:
# Напишите функцию get_advanced_writer(file_name), принимающую название файла для записи.

def get_advanced_writer(file_name):
# Внутри этой функции, напишите ещё одну - write_everything(*data_set), где *data_set - параметр принимающий
# неограниченное количество данных любого типа.

    def write_everything(*data_set):
# Логика write_everything заключается в добавлении в файл file_name всех данных из data_set в том же виде.

        with open(file_name, 'a', encoding='utf8') as file:
            for i in data_set:
                file.write(str(i) + '\n')

# Функция get_advanced_writer возвращает функцию write_everything.

    return write_everything


# Данный код:
# Запишет данные в файл в таком виде.

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

#
# Метод __call__:
# Создайте класс MysticBall, объекты которого обладают атрибутом words хранящий коллекцию строк.
# В этом классе также определите метод __call__ который будет случайным образом выбирать слово из words и возвращать
# его. Для случайного выбора с одинаковой вероятностью для каждого данного в коллекции можете использовать функцию
# choice из модуля random.
# Ваш код (количество слов для случайного выбора может быть другое):
# from random import choice
# Ваш класс здесь

from random import choice


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())

# Примерный результат (может отличаться из-за случайности выбора):
# Да
# Да
# Наверное
#
# Примечания:
# Все задания пишутся в одном модуле.
# Передаваемые данные в функции и объекты можете использовать свои, главное, чтобы ваш код полноценно демонстрировал
# логику написанного.
