class Children:

    def __init__(self, name, age, relax=False, hangry=True):
        self.name = name
        self.age = age
        self.relax = relax
        self.hangry = hangry
    def Children_prt(self):
        print(f'Имя {self.name}, возраст {self.age}, состояние голода {self.hangry}, состояние покоя {self.relax}')
class Parents:

    def __init__(self, name, age, children):
        self.name = name
        self.age = age
        self.children = children

    def parents_prn(self):
        print(f'меня зовут {self.name}, мне {self.age} лет.')
        print(f'у меня есть дети {self.children.name}')

    def parents_eat(self):
        self.children.hangry = False


masha=Children('Маша', 10)
papa=Parents('Ваня', 45, masha)

print(f'Первоначальное состояние ребенка ')
masha.Children_prt()
print(f'\nИнформация о родителе ')
papa.parents_prn()
print('\nКормим ребенка')
papa.children.hangry = False
masha.Children_prt()
print('\nУспакаиваем ребенка')
papa.children.relax = True
masha.Children_prt()