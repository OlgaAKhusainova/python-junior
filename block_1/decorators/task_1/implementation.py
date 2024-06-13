import time
def time_execution_decorator(function):
    """
    Обертка, печатающая время выполнения функции.
    """
    def wrapper(arg_1):
        if arg_1 >= 0 and type(arg_1) == int:
           time_start = time.time()
           result = function(arg_1)
           txt = str(time_start - time.time()) + 's'
        else:
           txt = 'invalid type'
        return txt
    return wrapper

@time_execution_decorator
def factorial_function(arg):
    res = 1
    for iter in range(1, arg + 1):
        res *= iter
    return res

print(factorial_function(5))