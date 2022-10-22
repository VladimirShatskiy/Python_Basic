goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}


for code in goods:
    count, count_price = 0, 0
    for item in store[goods[code]]:
        count += item["quantity"]
        count_price += item["quantity"] * item["price"]
    print(f"{code} - {count}  штук{'и' if count % 10 < 5 else ''},"
          f" стоимость {count_price:,d} руб{'ля' if count_price % 10 == 2 or count_price % 10 == 4 else 'лей'}" )
