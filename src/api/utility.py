from datetime import datetime
from datetime import timedelta
import re

def adjusted_date(date, value):
    date = datetime.strptime(date, '%Y-%m-%d')
    return str(date + timedelta(days=value)).split(' ')[0]

def get_full_name(data):
  
    if not data['middle_name'] and not data['name_extension']:
        return data['first_name'] + data['sur_name'] 
    elif data['middle_name'] == "":
        return data['first_name'] + data['sur_name'] + ", " + data['name_extension']
    elif data['name_extension'] == "":
        return data['first_name'] + " " +  data['middle_name'] + " " + data['sur_name']
    else:
        return data['first_name'] + " " +  data['middle_name'] + " " + data['sur_name'] + ", " + data['name_extension']

def get_name(data):
    return data['first_name'] + " " + data['sur_name']

def get_device(request): 
  
    if request.user_agent.is_pc == True:
        return "PC"
    elif request.user_agent.is_mobile == True:
        return "Mobile"
    elif request.user_agent.is_tablet == True:
        return "Tablet"
    elif request.user_agent.is_touch_capable == True:
        return "Touch Capable"
    elif request.user_agent.is_bot == True:
        return "Bot"
    else:
        return "Other"

def db_value(str):
    
    try:
        return str.replace("-", "/")
    except:
        return str

def db_column(column):
   
    if column == 'position': 
        column += "__title__icontains"
    elif column == 'office': 
        column += "__name__icontains"
    elif column == 'date_created': 
        column += '__range'
    else: 
        column += "__exact"

    return column

def entry(kwargs):
    return kwargs.get('entry')
    
def order_list(order):

    if order is None: 
        return ['id']

    elif order == 'name': 
        return [
            "sur_name", 
            "first_name"
        ]

    elif order == '-name': 
        return [
            "-sur_name", 
            "-first_name"
        ]

    elif order == 'employee__name': 
        return [
            "employee__sur_name", 
            "employee__first_name"
        ]

    elif order == '-employee__name': 
        return [
            "-employee__sur_name", 
            "-employee__first_name"
        ]

    elif order == 'leave_status': 
        return [
            "hr_remarks", 
            "supervisor_remarks"
        ]

    elif order == '-leave_status': 
        return [
            "-hr_remarks", 
            "-supervisor_remarks"
        ]

    elif order == 'employee__employee_no': 
        return ["employee__employee_no"]

    elif order == '-employee__employee_no': 
        return ["-employee__employee_no"]

    else: 
        return [order]    

def is_username_valid(username):
    
    if re.match("^[a-zA-Z0-9]+([a-zA-Z0-9](_|-| )[a-zA-Z0-9])*[a-zA-Z0-9]+$", username) == None:
        return True
    
    return False

def is_password_valid(password):
    
    if re.match("^[a-zA-Z0-9]+([a-zA-Z0-9](_|-| )[a-zA-Z0-9])*[a-zA-Z0-9]+$", password) == None:
        return True
    
    return False

def has_illegal_chars(str):
   
    if re.match("^[a-zA-Z0-9]+([a-zA-Z0-9](_|-| )[a-zA-Z0-9])*[a-zA-Z0-9]+$", str):
        return False
   
    return True


def get_duration(login, logout):
   
    loginTimestamp = datetime.timestamp(datetime.strptime(login,'%Y-%m-%d %H:%M:%S %p'))
    logoutTimestamp = datetime.timestamp(datetime.strptime(logout, '%Y-%m-%d %H:%M:%S %p'))
    duration = (logoutTimestamp - loginTimestamp)

    if duration < 60:
        return str(round(duration)) + " sec(s)"
    
    elif duration >= 60 and duration < 3600:
        return str(round(duration / 60)) + " min(s)"
    
    elif duration >= 3600:
        return str(round(duration / 3600)) + " hr(s)"

    
def password_length_valid(password):
    
    if len(password) < 8 or len(password) > 16:
        return False
    
    return True
        
def starts_with_capital_letter(str):
    return str[0].isupper()

def capitalize(str):
    return str.capitalize().replace('_', ' ')

