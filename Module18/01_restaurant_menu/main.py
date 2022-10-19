input_menu ="утиное филе;фланк-стейк;банановый пирог;плов"
menu = input_menu.split(";")
menu_end = ", ".join(menu)
print(f"Доступное меню: {input_menu}\n"
f"На данный момент в меню есть: {menu_end}")

