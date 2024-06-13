cnt = 0
def counter(function):
    """
    Обертка для подсчёта количества вызовов обернутой функции.

    Returns:
        int - количество вызовов функции.
    """
    def wrapper():
        global cnt
        res = function()
        cnt += 1
        return cnt
    return wrapper
    raise NotImplementedError
