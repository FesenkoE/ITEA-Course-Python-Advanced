# Написать функцию для вычислений очередного числа Фибоначчи (можно через цикл, можно
# через рекурсию).


def main():
    def fib_number(n):
        afp = 0
        bfn = 1
        i = 1
        fib = 1
        while i < n:
            fib = afp + bfn
            afp = bfn
            bfn = fib
            i += 1

        return fib

    print(fib_number(6))


if __name__ == '__main__':
    main()
