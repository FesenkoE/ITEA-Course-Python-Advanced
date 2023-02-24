# 1. Написать декоратор, который будет печатать на экран время работы функции.
import time


def main():

    def function_duration(func):
        def inner():
            start_time = time.time()
            func()
            end_time = time.time()
            print(f'Time execution function is {end_time - start_time}')
        return inner

    @function_duration
    def some_function():
        print('Hello World')

    some_function()


if __name__ == '__main__':
    main()
