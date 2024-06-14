from block_1.common import (
    MyException,
)
import time
def decorator_maker(times, delay):
    """
    Обертка, которая повторяет вызов функции times раз с паузой delay секунд
    Args:
        times: количество повторений
        delay: задержка (с)

    Returns:
        валидное значение (при вызове bool() -> True)
    """
    def decorator_maker_function(function):
        def wrapper():
            for counter in range(1, times + 1):
                try:
                    res = function()
                    return res
                except Exception:
                    if counter < times:
                        time.sleep(delay)
                    else:
                        raise MyException(Exception)
        return wrapper
    return decorator_maker_function
