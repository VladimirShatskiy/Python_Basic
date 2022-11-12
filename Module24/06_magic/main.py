class Water:
    title = 'Вода'
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Land):
            return Dirt()
        else:
            return None

class Air:
    title = 'Воздух'
    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Land):
            return Dust()
        else:
            return None
class Fire:
    title = 'Огонь'
    def __add__(self, other):
        if isinstance(other, Land):
            return Lava()
        else:
            return None

class Lava:
    title = 'Лава'
class Dust:
    title = 'Пыль'
class Lightning:
    title = 'Молния'
class Land:
    title = 'Земля'
class Storm:
    title = 'Шторм'
class Dirt:
    title = 'Грязь'
class Steam:
    title = 'Пар'

f = Fire()
a = Land()
s = f + a

if s != None:
    print(f"Смешиваем '{f.title}' c '{a.title}' и получаем '{s.title}'")
else:
    print("Такой состав мне не известен")
