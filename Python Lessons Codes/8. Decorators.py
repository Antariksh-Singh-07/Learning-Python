from time import perf_counter, sleep
from functools import wraps

def time_calc(func):
    
    @wraps(func) # with this proper output of dunder name, docs, etc are thrown
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        func(*args, **kwargs)
        time = perf_counter() - start_time
        print(f"took {time:.2f} seconds to run")
    
    return wrapper


@time_calc # Decorator
def does_something():
    for i in range(100_000_000):
        pass
    
does_something()
