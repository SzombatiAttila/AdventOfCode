import time
from typing import Callable


def measure_time_sync(function: Callable, *args, **kwargs):
    def wrapper_function(*args, **kwargs):
        start_time = time.time()
        function(*args, **kwargs)
        end_time = time.time()
        print(f'The time taken to finish the function: {end_time - start_time}')

    return wrapper_function