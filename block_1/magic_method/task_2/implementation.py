from datetime import datetime, timedelta
from block_1.common import (
    MyException,
)

class MathClock:
    def __init__(self):
        self._time = datetime(2000, 1, 1, 0, 0)
        
    def get_time(self):
        return self._time.strftime("%H:%M")
    
    def __add__(self, min):
        try:
            result = self._time + timedelta(minutes=min)
            self._time = result
        except:
            raise MyException
        
        return self._time
        
    def __mul__(self, hrs):
        try:
            result = self._time + timedelta(hours = hrs)
            self._time = result
        except:
            raise MyException
        return self._time
    
    def __sub__(self, min):
        try:
            result = self._time - timedelta(minutes= min)
            self._time = result
        except:
            raise MyException
        return self._time
    
    def __truediv__(self, hrs):
        try:
            result = self._time - timedelta(hours = hrs)
            self._time = result
        except:
            raise MyException
        return self._time


