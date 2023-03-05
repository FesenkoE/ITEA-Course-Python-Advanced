"""
3. Реализовать класс матрицы произвольного типа. При создании экземпляра передаётся
вложенный список. Для объектов класса реализовать метод сложения и вычитания матриц,
а также умножения, деления матрицы на число и user-friendly вывода матрицы на экран.
"""


class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __add__(self, other: 'Matrix'):
        return Matrix([
            [self.matrix_list[0][0] + other.matrix_list[0][0],
             self.matrix_list[0][1] + other.matrix_list[0][1]],
            [self.matrix_list[1][0] + other.matrix_list[1][0],
             self.matrix_list[1][1] + other.matrix_list[1][1]]
        ])

    def __sub__(self, other: 'Matrix'):
        return Matrix([
            [self.matrix_list[0][0] - other.matrix_list[0][0],
             self.matrix_list[0][1] - other.matrix_list[0][1]],
            [self.matrix_list[1][0] - other.matrix_list[1][0],
             self.matrix_list[1][1] - other.matrix_list[1][1]]
        ])

    def __mul__(self, other: int):
        return Matrix([
            [self.matrix_list[0][0] * other,
             self.matrix_list[0][1] * other],
            [self.matrix_list[1][0] * other,
             self.matrix_list[1][1] * other]
        ])

    def __truediv__(self, other: int):
        return Matrix([
            [int(self.matrix_list[0][0]) / other,
             int(self.matrix_list[0][1]) / other],
            [int(self.matrix_list[1][0]) / other,
             int(self.matrix_list[1][1]) / other]
        ])

    def __str__(self):
        return f"{self.matrix_list[0]}\n{self.matrix_list[1]}"
