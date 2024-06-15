from block_1.common import (
    MyException,
)
class ClassFather:
    registered_list = []
    _name = 'Class Father name'

    @classmethod
    def register(cls):
        if issubclass(cls, ClassFather) and cls._name != 'Class Father name':
            cls.registered_list.append(cls._name)
        else:
            raise MyException

    @classmethod
    def get_name(cls):
        if issubclass(cls, ClassFather) and cls._name in cls.registered_list:
            return cls._name
        else:
            raise MyException

class User1(ClassFather):
    _name = 'User1 name'


class User2(ClassFather):
    _name = 'User2 name'
