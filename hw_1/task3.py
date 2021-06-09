# Реализовать функцию, которая принимает три позиционных аргумента и возвращает сумму наибольших
# двух из них.

def sum_two_max_numbers(num1, num2, num3):
    num_list = [num1, num2, num3]
    max_num_1 = max(num_list)
    num_list.remove(max_num_1)
    max_num_2 = max(num_list)

    return max_num_1 + max_num_2


print(sum_two_max_numbers(7, 2, 3))
