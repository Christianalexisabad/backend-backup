from datetime import datetime, timedelta
from dateutil.relativedelta import *

DATE = datetime.now()

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S %p"
DATE_FORMAT = "%Y-%m-%d"
DATE_FORMAT1 = "%Y-%m"
TIME_FORMAT = "%H:%M:%S %p"

def get_datetime():
    return DATE.strftime(DATETIME_FORMAT)

def get_current_date(): 
    return str(datetime.today().strftime("%Y-%m-%d")).split(" ")[0]

def get_current_time(): 
    return str(datetime.today().strftime(TIME_FORMAT)).split(" ")[0]

def get_expiry():
    return (DATE + timedelta(days=1)).strftime(DATETIME_FORMAT)

def get_year_and_month():
    return str(datetime.now().strftime("%Y-%m"))

def get_year(*args):
    if args:
        return datetime.strptime(args[0], "%Y-%m-%d").year
    return str(datetime.now().strftime("%Y"))
    
def get_day(*args):
    if args:
        return datetime.strptime(args[0], "%Y-%m-%d").day
    return str(datetime.now().strftime("%Y"))

def get_time(*args):
    if args:
        time = datetime.strptime(args[0], DATETIME_FORMAT)
        return time
    return str(datetime.now().strftime(TIME_FORMAT))


def get_period(*args):
    if args:
        return DATE.strftime("%p")
    return DATE.strftime("%p")

def years_between(start_date, end_date):
    start_date = datetime.strptime(start_date, DATE_FORMAT)
    end_date = datetime.strptime(end_date, DATE_FORMAT)
    return relativedelta(end_date, start_date).years

def months_between(start_date, end_date):
    start_date = datetime.strptime(start_date, DATE_FORMAT1)
    end_date = datetime.strptime(end_date, DATE_FORMAT1)
    return abs(end_date, start_date).months

def days_between(start_date, end_date):
    start_date = datetime.strptime(start_date, DATE_FORMAT)
    end_date = datetime.strptime(end_date, DATE_FORMAT)
    return abs((start_date - end_date).days)

def mins_between(start_date, end_date):
    start_date = datetime.strptime(start_date, DATETIME_FORMAT)
    end_date = datetime.strptime(end_date, DATETIME_FORMAT)
    return relativedelta(end_date, start_date).days

def last_month(date, value):
    today_date = datetime.now().date()
    last_month = today_date + relativedelta(months=value)
    return last_month