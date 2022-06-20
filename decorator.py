# lesson

import time


def delay_decorator(function):
    def wrapper_function():
        # do something before
        time.sleep(2)
        function()
        # can run multiple times
        function()
        # do something after

    return wrapper_function


@delay_decorator
def say_hello():
    print('Hello')


@delay_decorator
def say_bye():
    print('Bye')


def say_greeting():
    print('How are you?')
