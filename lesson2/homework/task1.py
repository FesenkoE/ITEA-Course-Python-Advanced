"""
1. Реализуйте базовый класс Car.
У класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
40 (WorkCar) должно выводиться сообщение о превышении скорости.
Реализовать метод для user-friendly вывода информации об автомобиле.
"""


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'The car {id(self)} has been moved')

    def stop(self):
        print(f'The car {id(self)} has been stopped')

    def turn(self, direction):
        print(f'The car {id(self)} turn {direction}')

    def show_speed(self):
        return self.speed

    def __str__(self):
        return f'Current car {id(self)}\nColor: {self.color}\nSpeed: {self.speed}'


class TownCar(Car):
    speed_limit = 60

    def show_speed(self):
        current_speed = super().show_speed()
        if current_speed > self.__class__.speed_limit:
            print('Over speed')

        return current_speed


class SportCar(Car):
    pass


class WorkCar(Car):
    speed_limit = 40

    def show_speed(self):
        current_speed = super().show_speed()
        if current_speed > self.__class__.speed_limit:
            print('Over speed')

        return current_speed


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


print(PoliceCar(100, 'blue', 'Ford'))
