#
#

class Property:
    def __init__(self, worth=1000):
        self.worth = worth
        self.vat_pay = self.worth * self.vat


class Apartment(Property):
    vat = 1 / 1000


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)
        self.__vat = 1/200
    vat = 1 / 200

class CountryHouse(Property):
    vat = 1 / 500

count_vat = 0
item = {'Car': 0, 'CountryHouse': 0, 'Apartment': 0}
item_val = {}
for key in item:
    print(f'Введи стоимость имущетсва {key} ', end='')
    item[key] = int(input())

    if key == 'Car':
        item_val[key] = Car(item[key]).vat_pay
    elif key == 'CountryHouse':
        item_val[key] = CountryHouse(item[key]).vat_pay
    elif key == 'Apartment':
        item_val[key] = Car(item[key]).vat_pay
    else:
        print('Не знаю такого имущества')

    count_vat += item[key]
print(f'налог по каждому имуществу \n{item_val} \n'
      f'Общая сумма {count_vat}\n'
      f'Надеюсь у тебя есть искомая суммау')
