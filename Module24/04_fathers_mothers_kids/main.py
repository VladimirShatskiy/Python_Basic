class Children:

    def __init__(self, name, age, relax=False, hunger=True):
        self.name = name
        self.age = age
        self.relax = relax
        self.hunger = hunger

    def hangry(self, hunger):
        self.hunger = hunger

    def relax(self, relax):
        self.relax = relax

    def Children_prt(self):
        print(f'Имя {self.name}, возраст {self.age}, состояние голода {self.hunger}, состояние покоя {self.relax}')


class Parents:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.children = []

    def add_children(self, kid):
        self.children.append(kid)

    def parents_prn(self):
        print(f'Меня зовут {self.name}, мне {self.age} лет.')




masha = Children('Маша', 10)
petiy = Children('Петя', 17)
papa = Parents('Ваня', 45)
papa.add_children(masha)
papa.add_children(petiy)

print(f'\nИнформация о родителе ')
papa.parents_prn()

print(f'Первоначальное состояние детей')
for kid in papa.children:
    kid.Children_prt()

print(f'\nКормим ребенка {masha.name}')
masha.hunger = False
masha.Children_prt()
print(f'\nУспакаиваем ребенка {petiy.name}')
petiy.relax = True
petiy.Children_prt()