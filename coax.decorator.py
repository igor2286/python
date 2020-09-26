import time
from functools import wraps


def a_decorator_passing_arguments(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        time_start = time.time()
        rez = fn(*args, **kwargs)
        print(f"function is runing for {time.time() - time_start}sec.")
        return rez
    return wrapped


