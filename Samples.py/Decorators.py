import time

def timer(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args , **kwargs)
        end = time.time()
        print(f"{function.__name__} ran in {end-start} time") 
        
        return result
    return wrapper 
@timer
def example_function(n):
    time.sleep(n)
example_function(1)
def debug(function):
    def wrapper(*args, **kwargs):

        args_value = ','.join(str(arg) for arg in args)
        kwargs_value = ','.join(f"{k}={v}" for k, v in kwargs.items())
        print(f"calling: {function.__name__} with args {args_value} and kwargs {kwargs_value}")
        return function(*args, **kwargs)

    return wrapper
@debug
def hello():
    print("hello")
hello()

@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")
hello()
greet("chai", greeting="hanji")





import time

def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result

        return result
    return wrapper
@cache
def long_running_time(a,b):
    time.sleep(3)
    
    return a + b

print(long_running_time(2,3))
print(long_running_time(2,3))
