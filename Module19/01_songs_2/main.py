violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}
n_song = int(input("Сколько песен: "))
sum_time = 0

for _ in range(n_song):
    song = input("Название песни: ")
    sum_time += violator_songs.get(song)

print(f"Общее время звучания: {sum_time}")