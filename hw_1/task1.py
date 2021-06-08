# 1. Написать декоратор, который будет печатать на экран время работы функции.
from datetime import datetime
import time


def func_executing(func):

    def inner(*args, **kwargs):
        start_time = datetime.now()
        print('Start time', start_time)
        func(*args, **kwargs)
        end_time = datetime.now()
        print('End time', end_time)
        print('Executing time', end_time - start_time)

    return inner


@func_executing
def say(name, surname):
    print('Hello', name, surname)


say('Vasil', 'Ivanov')
