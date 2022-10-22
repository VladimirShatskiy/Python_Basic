order_num = {
    1: "Первый",
    2: "Второй",
    3: "Третий",
    4: "Четвертый",
    5: "Пятый",
    6: "Шестой",
    7: "Седьмой",
    8: "Восьмой"
            }
order_list = dict()

order_i = int(input("Введи количество заказов "))

for i in range(1, order_i + 1):
    name, pizza, price = input(f"{order_num[i]} заказ: ").split()
    price = int(price)

    if not name in order_list:
        order_list[name] = {pizza: price}
    else:
        if pizza in order_list[name]:
            order_list[name][pizza] += price
        else:
            order_list[name][pizza] = price

print()
for i in order_list:
    print(f"{i} :")
    for x in order_list[i]:
        print(f"        {x} : {order_list[i][x]}")

