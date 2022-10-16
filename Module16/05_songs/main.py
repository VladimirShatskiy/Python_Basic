def find_song(songs, find):
    for song in violator_songs:
        if song[0] == find:
            return song[1]
    return 0


violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

quantuty = int(input("Сколько песен вбрать? "))
all_minute = 0

for i_quantity in range(1, quantuty + 1):
    print(f"Название {i_quantity}-й песни ", end="")
    choice = input()
    all_minute += find_song(violator_songs, choice)

print(f"Общее время звучания песен: {all_minute} минут")
