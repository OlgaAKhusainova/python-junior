from block_1.common import (
    MyException,
)
cnt = 0
def check_value(function):
    """
    Обертка, проверяющая валидность переданного значения(неотрицательный int).
    В случае валидного значения - передает дальше в функцию,
    в противном случае - выбрасывает исключение MyException.
    """
    def wrapper(arg_1):
        if arg_1 is None or type(arg_1) != int or arg_1 < 0:
           raise MyException("Invalid type")
        else:
           result = function(arg_1)
           return result           
    return wrapper

@check_value
def factorial_function(arg):
    res = 1
    for iter in range(1, arg + 1):
        res *= iter
    return res

print(factorial_function(5))