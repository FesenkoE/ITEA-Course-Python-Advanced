"""
Написать программу, которая запрашивает у пользователя строку чисел, разделённых пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет добавляться к
уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы
завершается. Если специальный символ введён после нескольких чисел, то вначале нужно добавить
сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


def main():
    numbers = input('Enter numbers with SPACE: ')
    check_symbol = is_symbol_true(numbers)

    while check_symbol:
        numbers_list = numbers.split()
        int_numbers_list = [int(x) for x in numbers_list]
        sum_list = sum(int_numbers_list)


def is_symbol_true(some_list):
    for x in some_list:
        if not x.isdigit():
            return False

    return True


if __name__ == '__main__':
    main()
