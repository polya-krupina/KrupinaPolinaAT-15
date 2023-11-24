import re
import doctest


def is_correct_date(date):
    """
    Функция, проверяющая корректность введенной даты
    Args:
        date (str): дата

    Returns:
        bool: корректность данных
    >>> is_correct_date('20 января 1806')
    True
    >>> is_correct_date('1924, July 25')
    True
    >>> is_correct_date('26/09/1635')
    True
    >>> is_correct_date('3.1.1506')
    True

    >>> is_correct_date('25.08-1002')
    False
    >>> is_correct_date('декабря 19, 1838')
    False
    >>> is_correct_date('8.20.1973')
    False
    >>> is_correct_date('Jun 7, -1563')
    False
    >>> is_correct_date('31 февраля 2023')
    False
    >>> is_correct_date('31 июня 2015')
    False
    """
    pattern = re.compile(
        r'^([1-9]|0[1-9]|[12][0-9]|3[01])/([1-9]|0[1-9]|1[0-2])/\d{4}$|'
        r'^([1-9]|0[1-9]|[12][0-9]|3[01])-([1-9]|0[1-9]|1[0-2])-\d{4}$|'
        r'^([1-9]|0[1-9]|[12][0-9]|3[01])\.([1-9]|0[1-9]|1[0-2])\.\d{4}$|'
        r'^(\d{4}/([1-9]|0[1-9]|1[0-2])/[1-9]|0[1-9]|[12][0-9]|3[01])$|'
        r'^(\d{4}|3[01])-([1-9]|0[1-9]|1[0-2])-[1-9]|0[1-9]|[12][0-9]$|'
        
        r'^(?:(April|June|September|November)+\.? \d[1-9]|1\d|2[0-9]|30,? \d{1,4})$|'
        r'^(?:(January|March|May|July|August|October|December)+\.? \d[1-9]|1\d|2[0-9]|3[01],? \d{1,4})$|'
        r'^(?:February+\.? \d[1-9]|1\d|2[0-9],? \d{1,4})$|'
        
        r'^(?:(Apr|Jun|Sep|Nov)+\.? \d[1-9]|1\d|2[0-9]|30,? \d{1,4})$|'
        r'^(?:(Jan|Mar|May|Jul|Aug|Oct|Dec)+\.? \d[1-9]|1\d|2[0-9]|3[01],? \d{1,4})$|'
        r'^(?:Feb+\.? \d[1-9]|1\d|2[0-9],? \d{1,4})$|'
        
        r'^(?:\d{1,4},? (April|June|September|November)+\.? \d[1-9]|1\d|2[0-9]|30)$|'
        r'^(?:\d{1,4},? (January|March|May|July|August|October|December)+\.? \d[1-9]|1\d|2[0-9]|3[01])$|'
        r'^(?:\d{1,4},? February+\.? \d[1-9]|1\d|2[0-9])$|'
        
        r'^(?:[1-9]|1\d|2[0-9]|30,? (Apr|Jun|Sep|Nov)+\.? \d{1,2})$|'
        r'^(?:[1-9]|1\d|2[0-9]|3[01],? (Jan|Mar|May|Jul|Aug|Oct|Dec)+\.? \d{1,2})$|'
        r'^(?:[1-9]|1\d|2[0-9],? Feb+\.? \d{1,2})$|'
        
        r'^(?:[1-9]|1\d|2[0-9]|30)\s+(апреля|июня|сентября|ноября)\s+(\d{1,4})|'
        r'^(?:[1-9]|1\d|2[0-9]|3[01])\s+(января|марта|мая|июля|августа|октября|декабря)\s+(\d{1,4})|'
        r'^(?:[1-9]|1\d|2[0-9])\s+февраля\s+(\d{1,4})'
    )
    return bool(re.match(pattern, date))


doctest.testmod(verbose=True)