import math

point_x = float(input(f"Введите координаты монетки \nX: "))
point_y = float(input(f"Y: "))
radius = int(input(f"Введите радиус: "))
length = math.sqrt(point_x ** 2 + point_y ** 2)
if length > radius:
    print("\nМонеки в области нет")
else:
    print("\nМонетка где то рядом")