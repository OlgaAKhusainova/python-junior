class Tuple:

    tpl = ()
    def __init__(self, *args):
        self.tpl = args

    """
    Создает неизменяемый объект с упорядоченной структурой и методами count и index.
    При создании принимается последовательность объектов.
    """

    def count(self, value) -> int:
        """
        Возвращает количество появлений value в объекте.

        Args:
            value: количество вхождений в объекте
        """
        count = 0
        for i in self.tpl:
            if i == value:
                count += 1
        return count

    def index(self, value) -> int:
        """
        Возвращает индекс первого вхождения элемента в объекте.

        Args:
            value: индекс искомого элемента
        """
        idx = None
        for i in range(0, len(self.tpl)):
            if self.tpl[i] == value:
                idx = i
                break
        if idx is None:
            raise ValueError
        else:
            return idx
    
    def __getitem__(self, key):
        if len(self.tpl) > 0 and key in range(0, len(self.tpl)):
            return self.tpl[key]
        else:
            raise ValueError
