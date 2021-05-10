# -*- Mode: Python -*-

from datetime import datetime
from dateutil import relativedelta

TODAY = datetime.today()
TODAY_YEAR = TODAY.year
TODAY_YEAR_SHORT = TODAY.year % 100
TODAY_CENTURY = TODAY_YEAR - TODAY_YEAR_SHORT
EPOCH = datetime(1970, 1, 1)

def datetime_to_timestamp(dt):
    return (dt - EPOCH).total_seconds()

def next_month(prev=TODAY):
    return prev + relativedelta.relativedelta(months=1)

def interpret_year(year):
    if year <= TODAY_YEAR_SHORT:
        return year + TODAY_CENTURY
    elif year < 100:
        return year + TODAY_CENTURY - 100
    else:
        return year

def file_date_to_datetime(year, month, day):
    if not day:
        day = 28
    return datetime(interpret_year(year), month, day, 23, 59, 59)
