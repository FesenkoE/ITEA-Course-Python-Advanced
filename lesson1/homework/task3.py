"""
Реализовать функцию, которая принимает три позиционных
аргумента и возвращает сумму наибольших двух из них.
"""


def main():
    def sum_max_num(a, b, c):
        sorted_list = sorted([a, b, c])

        return sorted_list[len(sorted_list) - 1] + sorted_list[len(sorted_list) - 2]

    print(sum_max_num(-1, -3, 5))


if __name__ == '__main__':
    main()
