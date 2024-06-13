from datetime import timedelta

def get_next_date(some_date):
    """Возвращает следующую дату для заданной

    Args:
        some_date: определенная исходная дата

    Returns: следующая дата
    """
    try:
      new_date = some_date + timedelta(days=1)
      print(new_date)
      return new_date
    except TypeError :
       return 'Некорректная дата'
    raise NotImplementedError
