num_sim = {
    1: "первая",
    2: "вторая",
    3: "третья",
    4: "четвертая",
    5: "пятая",
    6: "шестая",
    7: "седьма",
    8: "восьмая",
    9: "девятая"
        }
i_people = int(input("Введите количество человек: "))
list_tree = {}
level = {}

for i in range(1, i_people):
    kid, parent = input(f"{num_sim[i]} пара: ").split()
    list_tree[kid] = parent
    level[parent] = 0
    level[kid] = 0

for i in list_tree:
    people = i
    while people in list_tree:
        people = list_tree[people]
        level[i] += 1

print(f"\n«Высота» каждого члена семьи:")
for i in sorted(level):
    print(i, level[i])
