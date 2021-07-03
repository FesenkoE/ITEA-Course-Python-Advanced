"""
3. Реализовать класс матрицы произвольного типа. При создании экземпляра передаётся вложенный список. Для объектов
класса реализовать метод сложения и вычитания матриц, а также умножения, деления матрицы на число и user-friendly вывода
матрицы на экран.
"""


class Matrix:

    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        new_data = []

        for i in range(len(self.data)):
            new_data.append([])
            for j in range(len(self.data[0])):
                new_data[i].append(self.data[i][j] + other.data[i][j])

        return Matrix(new_data)

    def __sub__(self, other):
        new_data = []

        for i in range(len(self.data)):
            new_data.append([])
            for j in range(len(self.data[0])):
                new_data[i].append(self.data[i][j] - other.data[i][j])

        return Matrix(new_data)

    def __mul__(self, other):
        new_data = []

        for i in range(len(self.data)):
            new_data.append([])
            for j in range(len(self.data[0])):
                new_data[i].append(self.data[i][j] * other)

        return Matrix(new_data)

    def __truediv__(self, other):
        new_data = []

        for i in range(len(self.data)):
            new_data.append([])
            for j in range(len(self.data[0])):
                new_data[i].append(self.data[i][j] / other)

        return Matrix(new_data)

    def __str__(self):
        list_str = ''
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                list_str += f'{self.data[i][j]}' + ' '
            list_str += '\n'

        return list_str
