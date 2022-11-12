import random

class Warrior:
    def __init__(self, name, level=100):
        self.name = name
        self.level = level

    def demage(self):
        self.level -= 20


unit1 = Warrior('Воин Иван')
unit2 = Warrior('Воин Дима')
company = {1: unit1, 2: unit2}

while True:
    attac = company[random.randint(1, 2)]
    defend = (unit2 if attac == unit1 else unit1)
    defend.demage()
    print(f'нападающий {attac.name} нанес удар в 20 пунктов по {defend.name}')
    if defend.level <= 0:
        print(f'защищающийся {defend.name} погиб смертью непонятной\n'
              f'от рук {attac.name}, у последнего осталось жизни {attac.level}')
        break