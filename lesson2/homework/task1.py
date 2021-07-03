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

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Car {self.name} went.")

    def stop(self):
        print(f"Car {self.name} stopped.")

    def turn(self, side):
        print(f"Car {self.name} turn {side}.")

    def show_speed(self):
        print(f"Current speed {self.name} is {self.speed}")

    def __str__(self):
        """User-friendly выыод информации об объекте"""
        return f"Car {self.name} {self.color} color is moving with {self.speed}"


class TownCar(Car):
    available_speed = 60

    def show_speed(self):
        if self.speed > self.__class__.available_speed:
            print(f'Speed is more than available {self.__class__.available_speed}')
        return self.__class__.available_speed


class SportCar(Car):
    pass


class WorkCar(Car):
    available_speed = 40

    def show_speed(self):
        if self.speed > self.__class__.available_speed:
            print(f'Speed is more than available {self.__class__.available_speed}')
        return self.__class__.available_speed


class PoliceCar(Car):
    pass


town_car = WorkCar(70, 'Blue', 'Skoda', False)
town_car.show_speed()
print(town_car.__str__())
