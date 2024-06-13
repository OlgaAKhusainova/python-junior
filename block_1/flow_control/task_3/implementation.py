def get_days_count_by_month(month):
    """Возвращает количество дней по месяцу

    Args:
        month: название месяца

    Returns: количество дней
    """
    dict = {'январь': 31,
            'март': 31,
            'май': 31,
            'июль': 31,
            'август': 31,
            'октябрь': 31,
            'декабрь': 31,
            'апрель': 30,
            'июнь': 30,
            'сентябрь': 30,
            'ноябрь': 30,
            'февраль': 28}
    res = dict.get(month.lower(), 0)
    return res
    raise NotImplementedError
