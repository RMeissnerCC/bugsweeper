from functools import wraps
import time


def measure(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            end_ = round((time.perf_counter() - start) * 1e+6, 3)
            print(f"Total execution time of {func.__name__}: {end_} us")

    return _time_it
