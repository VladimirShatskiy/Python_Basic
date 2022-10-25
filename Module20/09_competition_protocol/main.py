def del_players(temp):
    for del_item in range(len(list_play)):
        if temp == list_play[del_item][2]:
            list_play[del_item] = (0, 0, "")


players = [69485, "Jack", 95715, "qwerty", 95715, "Alex", 83647, "M", 197130, "qwerty",
            95715, "Jack", 93289, "Alex", 95715, "Alex", 95715, "M",2353,"Djo"]

list_winners = []
number_win = int(input("Введи количество победителей "))
put_win_list = 0
# первоначальный список, далее идем на его изменение
list_play = [(int(item / 2), players[item], players[item + 1]) for item in range(0, len(players), 2)]

while put_win_list < number_win:
    max_value = max(list_play[i][1] for i in range(len(list_play))) #каждый раз определяем список игроков с максимальными баллами
    for item in range(len(list_play)):
        if max_value == list_play[item][1]:
            if number_win > put_win_list:
                list_winners.append(list_play[item])
                put_win_list += 1
            del_players(list_play[item][2]) #Удаление игрока в случае переноса его в список победителей

print("Итоги соревнований: ")
for item in range(len(list_winners)):
    print(f"{item +1}-e место. {list_winners[item][2]} количество очков {list_winners[item][1]}")
