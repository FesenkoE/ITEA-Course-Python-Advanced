"""
1. Реализовать функцию, которая на вход принимает целое положительное число n и возвращает при вызове
 объект-генератор, который по запросу будет возвращать значение факториала всех чисел от 0 до n.
"""


def generator_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
        yield fact


fact_num = generator_factorial(5)
print(next(fact_num))
print(next(fact_num))
print(next(fact_num))
print(next(fact_num))
print(next(fact_num))
