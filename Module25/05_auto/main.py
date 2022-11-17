import math


class BasicCar:
    def __init__(self, x_position=0, y_position=0, angle=0):
        self.x_position = x_position
        self.y_position = y_position
        self.angle = angle
        self.total_distance = 0

    def set_distance(self, distance):
        """
        :param distance:Передвижение транспорта на указанное расстояние от текущих координат
        :return: none
        """
        self.x_position += distance * math.cos(math.radians(self.angle))
        self.y_position += distance * math.sin(math.radians(self.angle))
        self.total_distance += distance

    def set_angle_change(self, angle):
        """
        :param angle: Внесение корректировки в угол движения транспорта
        :return:
        """
        self.angle += angle

    def __str__(self):
        return f'Текущая позиция {self.x_position: .2f} : {self.y_position : .2f}, угол направления {self.angle}' \
               f' пройденная дистанция {self.total_distance}'


class Car(BasicCar):

    def __init__(self, x_position, y_position, angle, model="lada"):
        super().__init__(x_position, y_position, angle)
        self.model = model


class Bus(BasicCar):

    def __init__(self, x_position, y_position, angle, model='Paz'):
        super().__init__(x_position, y_position, angle)
        self.model = model
        self.passengers = []
        self.money = 0
        self.price = 5

    def entered_bus(self, passenger):
        print(f'Стоимость одного километра 5 рублей {passenger} вошел на {self.total_distance} км')
        self.passengers.append(passenger)
        passenger.set_start_point(self.total_distance)

    def out_bus(self, passenger):
        dist = self.total_distance - passenger.get_start_point()
        print(f'Пассaжир {passenger} проехал {dist} км, заплатил {dist * self.price} рублей')
        self.passengers.remove(passenger)
        self.money += dist * self.price


class Passenger():

    def __init__(self, name='people'):
        self.name = name
        self.start_point = 0

    def __str__(self):
        return f'{self.name}'

    def set_start_point(self, point):
        self.start_point = point

    def get_start_point(self):
        return self.start_point


bus1 = Bus(0, 0, 90)
ivan = Passenger('Иван')
van = Passenger('Ван')
bus1.set_distance(5)
bus1.set_angle_change(45)
bus1.entered_bus(ivan)
bus1.set_distance(10)
bus1.entered_bus(van)
bus1.set_distance(10)
bus1.out_bus(van)
bus1.out_bus(ivan)

print(f'{bus1} Всего заработал на маршруте {bus1.money}')



