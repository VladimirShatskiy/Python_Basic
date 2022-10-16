def arr(txt1, txt2, num):
    ret_arr = []
    for i in range(1, num + 1):
        print(f"{txt1}{i}{txt2}", end="")
        ret_arr.append(input())
    return ret_arr


rolers = []#[41,40,39,42]
legs = []#[42,41,42]
on_hand = []

i_rolers = int(input("Количесво коньков "))
i_legs = int(input("Количество людей "))

rolers.extend(arr("Размер ", "-й пары: ", i_rolers))
legs.extend(arr("Размер ноги ", "-го человека: ",i_legs))

for roler in rolers:
    for leg in legs:
        if leg <= roler:
            on_hand.append(roler)
            rolers.remove(leg)
            break

print(f"\nКоличество людей колторые могут получить ролик: {len(on_hand)}, "
      f"к выдаче готовы размеры {on_hand}")