country = {
    "Россия": ["Москва", "Петербург", "Новгород"],
    "Германия": ["Берлин", "Лейпциг", "Мюнхен"]
        }

for _ in range(3):
    city = input("Введи название города: ")
    is_city = False
    for i_country in country:
        for i_city in country[i_country]:
            if i_city == city:
                print(f"Город {i_city} расположен в стране {i_country}\n")
                is_city = True
                break
    if not is_city:
        print(f"По городу {city} нет данных\n")