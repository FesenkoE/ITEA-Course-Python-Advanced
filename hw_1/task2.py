# Написать функцию для вычислений очередного числа Фибоначчи (можно через цикл, можно
# через рекурсию).

f_num_1 = 1
f_num_2 = 1

# for example n = 7
n = 7
i = 1

while i < n - 1:
    f_summa = f_num_1 + f_num_2
    f_num_1 = f_num_2
    f_num_2 = f_summa

    i += 1

print('Summa fibonachi: ', f_num_2)
