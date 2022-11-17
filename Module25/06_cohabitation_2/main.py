import random


class Home:

    def __init__(self):
        self.money = 100
        self.eat_in_fridge = 50
        self.eat_cat = 30
        self.dirt = 0
        self.total_money = 0
        self.total_eat = 0

    def __str__(self):
        return f'денег:{self.money : .2f} еды:{self.eat_in_fridge :.2f} еды для кота:{self.eat_cat :.2f} грязи:{self.dirt}'

    def set_dirt(self, dirt):
        self.dirt = (self.dirt + dirt if self.dirt + dirt > 0 else 0)

    def cat_eats(self, eat):
        self.eat_cat -= eat



class People:
    def __init__(self, name, home):
        self.name = name
        self.satiety = 30
        self.happiness = 100
        self.home = home

    def play_cat(self):
        self.satiety -= 10
        self.happiness += 5

    def eats(self, food_value=30):
        eat = random.randint(1, food_value)
        if self.home.eat_in_fridge - eat > 0:
            self.satiety += eat
            self.home.eat_in_fridge -= eat
        else:
            self.satiety += self.home.eat_in_fridge
            self.home.eat_in_fridge = 0

    def __str__(self):
        return f'Имя:{self.name} сытость:{self.satiety} счастье:{self.happiness}'


class Cat:

    def rand(self):
        if self.satiety < 10:
            self.eat()
        else:
            random.choice([self.damage_everything, self.sleep, self.eat])()

    def __init__(self, name, home):
        self.name = name
        self.satiety = 30
        self.home = home

    def eat(self):
        eat = random.randint(1, 10)
        if self.home.eat_cat - eat < 0:
            self.home.eat_cat = 0
        else:
            self.home.cat_eats(eat)
        self.satiety += eat * 2

    def sleep(self):
        self.satiety -= 10

    def __str__(self):
        return f'{self.name} сытость:{self.satiety} '

    def damage_everything(self):
        self.satiety -= 10
        self.home.set_dirt(30)
        pass


class Man(People):

    def __init__(self, name, home):
        super().__init__(name, home)

    def rand(self):
        if not happy:
            self.happiness -= 10

        if self.happiness < 10:
            random.choice([self.gaming, self.play_cat])()
        elif self.satiety < 10:
            self.eats()
        else:
            random.choice([self.gaming, self.works, self.eats,self.play_cat])()


    def gaming(self):
        self.satiety -= 10
        self.happiness += 20

    def works(self):
        self.satiety -= 10
        self.home.money += 150
        self.home.total_money += 150


class Woman(People):

    def __init__(self, name, home):
        super().__init__(name, home)
        self.count_coat = 0

    def rand(self):
        if self.satiety < 10:
            self.eats()
        elif self.happiness < 10:
            random.choice([self.coat, self.play_cat])()
        elif self.home.eat_in_fridge < 10:
            self.shop()
        elif self.home.dirt > 100:
            self.clean()
        else:
            random.choice([self.shop, self.clean, self.eats, self.coat, self.play_cat])()
        if not happy:
            self.happiness -= 10

    def shop(self):
        self.satiety -= 10
        money_eat = int(self.home.money * 0.6)
        money_eat_cat = int(self.home.money * 0.1)
        self.home.money -= (money_eat + money_eat_cat)
        self.home.eat_cat += money_eat_cat
        self.home.eat_in_fridge += money_eat
        self.home.total_eat += money_eat

    def clean(self):
        self.satiety -= 10
        if self.home.dirt < 100:
            self.home.dirt = 0
        else:
            self.home.dirt -= 100

    def coat(self):
        self.satiety -= 10
        if self.home.money > 350:
            self.home.money -= 350
            self.happiness += 60
            self.count_coat += 1


count_eat, count_money, count_coat = 0, 0, 0
ishome = Home()
wife = Woman(name='Настя', home=ishome)
husband = Man(name='Владимир', home=ishome)
vaska = Cat('Васька', ishome)

for _ in range(365):
    ishome.set_dirt(5)
    happy = (True if ishome.dirt < 90 else False)
    wife.rand()
    husband.rand()
    vaska.rand()

print(wife)
print(husband)
print(ishome)
print(vaska)
print(f'Всего заработано денег {ishome.total_money} \nВсего съедено еды людьми {ishome.total_eat}'
      f'\nКуплено шуб женой {wife.count_coat}')