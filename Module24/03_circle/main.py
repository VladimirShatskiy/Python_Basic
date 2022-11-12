class Circle:

    def __init__(self, x_point=0, y_point=0, radius=1):
        self.x_point = x_point
        self.y_point = y_point
        self.radius = radius

    def sq_circle(self):
        return 3.14 * self.radius ** 2

    def pir_circle(self):
        return 2 * 3.14 * self.radius

    def resize_circle(self, increase):
        self.radius = (3.14 * self.radius ** 2 * increase / 3.14) ** (1/2)

    def prn_circle(self):
        print(f'x:{self.x_point} y:{self.y_point} радиус {self.radius}')

    def intersection(self, circle):
        x = abs(self.x_point - circle.x_point)
        y = abs(self.y_point - circle.y_point)
        summ_r = self.radius + circle.radius

        if (x ** 2 + y ** 2) ** (1/2) <= summ_r:
            return True
        else:
            return False

cir1 = Circle(2,3,1)
cir2 = Circle(3,10,7)

