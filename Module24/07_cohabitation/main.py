import random


class Man:

    def __init__(self, home, name='Артем', eat_level=50):
        self.name = name
        self.home = home
        self.eat_level = eat_level

    def prn(self):
        print(f'имя :{self.name} уровень сытости :{self.eat_level} еды дома :{self.home.fridge} денег дома :{self.home.money}')

    def eat(self, eat=20):
        self.eat_level += eat
        self.home.add_eat(-eat)
        print(f'{self.name} поел')

    def work(self, money=30, eat=20):
        self.eat_level -= eat
        self.home.add_money(money)
        print(f'{self.name} поработал')

    def game(self, eat=20):
        self.eat_level -= eat
        print(f'{self.name} поиграл')

    def shop(self, money=30, eat=20):
        self.home.add_money(-eat)
        self.home.add_eat(eat)
        print(f'{self.name} сходил в магазин')


class Home:

    def __init__(self, money=0, fridge=50):
        self.money = money
        self.fridge = fridge

    def add_money(self, money=20):
        self.money += money

    def add_eat(self, eat):
        self.fridge += eat


mens = []
is_home = Home()
man1 = Man(is_home)
man2 = Man(is_home, 'Петр')
mens.append(man1)
mens.append(man2)

for _ in range(365):
    for i in range(len(mens)):
        cube = random.randint(1, 6)

        if mens[i].eat_level < 20:
            mens[i].eat()
        elif mens[i].home.fridge < 10:
            mens[i].shop()
        elif mens[i].home.money < 50:
            mens[i].work()
        elif cube == 1:
            mens[i].work()
        elif cube == 2:
            mens[i].eat()
        else:
            mens[i].game()

        mens[i].prn()
        if mens[i].eat_level < 0:
            print(f'Умер от голода {mens[i].name}')
            break