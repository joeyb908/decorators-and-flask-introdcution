# challenge:
# print the speed it takes to run the fast_function() vs the slow_function() in the
# speed_calc_decorator() function

import time


def speed_calc_decorator(function):
    def wrapper_function():
        # mark the start time of the function
        start_time = time.time()
        # run the function
        function()
        # print the function name as well as the current time subtracted from the start time
        print(f'{function.__name__} run speed: {time.time() - start_time}')

    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


# calls both functions
fast_function()
slow_function()
