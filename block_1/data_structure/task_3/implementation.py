import copy

def copy_dict(origin_dict: dict) -> dict:
    """
    Функция возвращает копию словаря.
    """
    new_dict = {}
    for key, value in origin_dict.items():
        if type(value) in [dict, list, tuple, set]:
            new_dict.update({key: value.copy()})
        else:
            new_dict.update({key:value})
    return new_dict
    raise NotImplementedError
