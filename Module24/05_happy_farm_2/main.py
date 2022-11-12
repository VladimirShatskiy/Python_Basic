import random

class Gargener:
# Убирает картошку в случае созревания и сажает на ее место новую
    def __init__(self, name, potatoes):
        self.name = name
        self.row = potatoes
        self.harv = []

    def prn(self):
        print(f'{self.name} {self.row}')
    def harvesting(self):
        for i_row in self.row.potatoes:
            if i_row.stage == 3:
                self.harv.append(i_row.number)
                print(f'Собрал картошку с куста {i_row.number}')
                i_row.stage = 0
        # print(self.harv)

class Potato:
     # 0- посадка, 1 росток, 2 созревание 3 созрела
    def __init__(self, number, stage=0):
        self.number = number
        self.stage = stage

    def growth(self): # картошка растет по разному +0 или +1 стадия
        if self.stage < 3:
            self.stage += random.randint(0, 1)

    def prn(self):
        # print(f'Номер кортошки на грядке {self.number}, стадия зрелости {self.stage}')
        print(f'{self.number}-{self.stage}', end=' ')

class Row:

    def __init__(self, number):
        self.potatoes = [Potato(i) for i in range(number)]

    def prn(self):
        print()
        for i_potato in self.potatoes:
            i_potato.prn()

    def growth(self):
        for i_potato in self.potatoes:
            i_potato.growth()


rw = Row(10) #сеим грядку из 10 картшек
gardman = Gargener('Иван', rw)
count = 1

print(f'Дачник засеиват картошкой одну грядку из 10 клубней.\n'
      f'картошка имеет стадии роста 0 посеяна, 1 росток, 2 созревание 3 можно собирать\n'
      f'поливать картошку,при поливе она может подрасти, а может и нет\n'
      f'и как только картошкасозреет, собрать ее и посадить на ее место новую\n'
      f'Введи количество картошки которую долен собрать дачник: ', end='')
n_potato = int(input())

while len(gardman.harv) <= n_potato:
    rw.growth()
    gardman.harvesting()
    count += 1

print(f'Для сбора {n_potato} картошек  потребовалось {count} раз полить картошку')
print(f'Список плодоносных кустов {gardman.harv}')