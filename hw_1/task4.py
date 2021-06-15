"""
Написать программу, которая запрашивает у пользователя строку чисел, разделённых пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделённых пробелом
и снова нажать Enter. Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
ранее сумме и после этого завершить программу.
"""
total = 0
quit_symbol = '='
exit_value = True

while exit_value:
    numbers = input('Enter numbers with space: ')
    list_numbers = numbers.split(' ')

    for num in range(0, len(list_numbers)):
        if list_numbers[num] != quit_symbol:
            total = total + int(list_numbers[num])
        else:
            exit_value = False
            break

    print(total)


