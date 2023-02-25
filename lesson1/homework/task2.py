"""
Написать функцию для вычислений очередного числа Фибоначчи
(можно через цикл, можно через рекурсию).
"""


def main():
    def fib_number(n):
        before_num = 0
        after_num = 1
        cnt = 1
        fib = 1

        while cnt < n:
            fib = before_num + after_num
            before_num = after_num
            after_num = fib
            i += 1

        return fib

    print(fib_number(6))


if __name__ == '__main__':
    main()
