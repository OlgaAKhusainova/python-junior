"""
Что будет выведено после выполнения кода? Почему?
будет выведено Тest Message, потому что внутри data_transmitter нет объявления переменной message,
но она найдена на уровне transmit_to_space
далее вернется ничего, так transmit_to_space ничего не возвращает
"""


def transmit_to_space(message):
   
    def data_transmitter():        
        print(message)

    data_transmitter()


print(transmit_to_space("Test message"))
