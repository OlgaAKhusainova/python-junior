"""
Что будет выведено после выполнения кода? Почему?
2 раза выведется 3, тк внутри printer объявлена на уровне nonlocal переменная number, 
поэтому значение на уровне внешней функции print_msg будет так же 3
"""
def print_msg(number):

    def printer():
        nonlocal number
        number=3
        print(number)

    printer()
    print(number)


print_msg(9)