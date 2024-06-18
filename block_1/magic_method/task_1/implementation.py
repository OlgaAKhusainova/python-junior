from block_1.common import (
    MyException,
)
class Multiplier:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def __add__(self, obj):
        if isinstance(obj, Multiplier):
            return Multiplier(self.value + obj.value)
        else:
            raise MyException
        
    def __sub__(self, obj):
        if isinstance(obj, Multiplier):
            return Multiplier(self.value - obj.value)
        else:
            raise MyException
    
    def __mul__(self, obj):
        if isinstance(obj, Multiplier):
            return Multiplier(self.value * obj.value)
        else:
            raise MyException
        
    def __truediv__(self, obj):
        if isinstance(obj, Multiplier):
            return Multiplier(self.value / obj.value)
        else:
            raise MyException
        


class Hundred(Multiplier):
    """Множитель на 100"""
    def __init__(self, value):
        self.value = value * 100


class Thousand(Multiplier):
    """Множитель на 1 000"""
    def __init__(self, value):
        self.value = value * 1000


class Million(Multiplier):
    """Множитель на 1 000 000"""
    def __init__(self, value):
        self.value = value * 1000000



