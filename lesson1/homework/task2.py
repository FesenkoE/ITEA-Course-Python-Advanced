# Написать функцию для вычислений очередного числа Фибоначчи (можно через цикл, можно
# через рекурсию).


def fib_sum(num):
    f_num_1 = 1
    f_num_2 = 1
    i = 1

    while i < num - 1:
        f_summa = f_num_1 + f_num_2
        f_num_1 = f_num_2
        f_num_2 = f_summa
        i += 1

    return f_num_2


print(fib_sum(7))
