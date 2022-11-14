import random


class KillError(Exception):
    def __str__(self):
        return f'Exception: KillError'


class DrunkError(Exception):
    def __str__(self):
        return 'Exception: DrunkError'


class CarCrashError(Exception):
    def __str__(self):
        return 'Exception: CarCrashError'


class GluttonyError(Exception):
    def __str__(self):
        return 'Exception: GluttonyError'


class DepressionError(Exception):
    def __str__(self):
        return 'Exception: DepressionError'


def one_day():

    try:
        if random.randint(1, 10) == 5:
            error = random.choice(exception)
            raise error
    except error as err_str:
        with open('karma.log', 'a') as log_file:
            log_file.write(f'Произошла ошибка на {count} дне, ошибка {err_str} \n')
    finally:
        return random.randint(1, 7)
class Buddha:

    def __init__(self, name):
        self.name = name
        self.__point = 0

    def set_point(self, point):
        self.__point += point

    def get_point(self):
        return self.__point

count = 0
exception = [KillError, DrunkError, CarCrashError,
             GluttonyError, DepressionError]

student = Buddha('Иван')

while student.get_point() < 500:
    student.set_point(one_day())
    count += 1


