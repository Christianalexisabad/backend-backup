from django.db.models import Q 
from . import models
from . import serializers
from . import date

def leave(kwargs):

    department = kwargs.get('department')
    department_head = kwargs.get('department_head')
    employee = kwargs.get('employee')
    status = kwargs.get('status')
    application_date_range = kwargs.get('application_date_range')

    if application_date_range is not None:
        application_date_range = application_date_range.split(':')

    if department is not None and employee is not None and status is not None and application_date_range is not None:
        print(1) 
        return (Q(employee__position__department_id=department) & Q(employee=employee) & Q(supervisor_remarks=status) & Q(hr_remarks=status) & Q(application_date__range=application_date_range))
    elif department is not None and employee is not None and application_date_range is not None:
        print(2) 
        return (Q(employee__position__department_id=department) & Q(employee=employee) & Q(application_date__range=application_date_range))
    elif department is not None and employee is not None and status is not None:
        print(3) 
        return (Q(employee__position__department_id=department) & Q(employee=employee) & Q(supervisor_remarks=status) & Q(hr_remarks=status))
    elif department is not None and employee is not None:
        print(4) 
        return (Q(employee__position__department_id=department) & Q(employee=employee))
    elif department is not None and status is not None:
        print(5) 
        return (Q(employee__position__department_id=department) & Q(supervisor_remarks=status) & Q(hr_remarks=status))
    elif department_head is not None and employee is not None and status is not None and application_date_range is not None:
        print(6) 
        return (Q(employee__position__department__department_head_id=department_head) & Q(employee=employee) & Q(supervisor_remarks=status) & Q(hr_remarks=status) & Q(application_date__range=application_date_range))
    elif department_head is not None and employee is not None and status is not None and application_date_range is not None:
        print(7) 
        return (Q(employee__position__department__department_head_id=department_head) & Q(employee=employee) & Q(supervisor_remarks=status) & Q(hr_remarks=status) & Q(application_date__range=application_date_range))
    elif department_head is not None and employee is not None and application_date_range is not None:
        print(8) 
        return (Q(employee__position__department__department_head_id=department_head) & Q(employee=employee) & Q(application_date__range=application_date_range))
    elif department_head is not None and employee is not None and status is not None:
        print(9) 
        return (Q(employee__position__department__department_head_id=department_head) & Q(employee=employee) & Q(supervisor_remarks=status) & Q(hr_remarks=status))
    elif department_head is not None and employee is not None:
        print(10) 
        return (Q(employee__position__department__department_head_id=department_head) & Q(employee=employee))
    elif employee is not None and status is not None and application_date_range is not None:
        print(11) 
        return (Q(employee=employee) & Q(supervisor_remarks=status) & Q(hr_remarks=status) & Q(application_date__range=application_date_range))
    elif employee is not None and status is not None and application_date_range is not None:
        print(12) 
        return (Q(employee=employee) & Q(supervisor_remarks=status) & Q(hr_remarks=status) & Q(application_date__range=application_date_range))
    elif employee is not None and application_date_range is not None:
        print(13) 
        return (Q(employee=employee) & Q(application_date__range=application_date_range))
    elif employee is not None and status is not None:
        print(14) 
        return (Q(employee=employee) & Q(supervisor_remarks=status) & Q(hr_remarks=status))
    elif employee is not None:
        print(15) 
        return (Q(employee=employee))
    elif status is not None and application_date_range is not None:
        print(16) 
        return (Q(hr_remarks=status) & Q(supervisor_remarks=status) & Q(application_date__range=application_date_range))
    elif application_date_range is not None:
        print(17) 
        return (Q(application_date__range=application_date_range))
    elif department is not None:
        print(18) 
        return (Q(employee__position__department_id=department))
    elif department_head is not None:
        # print(19) 
        return (Q(employee__position__department__department_head_id=department_head))
    elif employee is not None:
        print(20) 
        return (Q(employee=employee))
    elif status is not None:
        print(21) 
        return (Q(hr_remarks=status) | Q(supervisor_remarks=status))
    else:
        print(22) 
        return ({})

def attendance(kwargs):

    period = kwargs.get('period')
    department = kwargs.get('department')
    department_head = kwargs.get('department_head')
    employee = kwargs.get('employee')
    status = kwargs.get('status')
    date_range = kwargs.get('date_range')

    if date_range is not None:
        date_range = date_range.split(':')

    if department is not None and employee is not None and status is not None and date_range is not None:
        print(1)
        if period == "AM":
            return (Q(employee__position__department_id=department) & Q(employee=employee) & Q(am_status=status) & Q(date__range=date_range))
        else:
            return (Q(employee__position__department_id=department) & Q(employee=employee) & Q(pm_status=status) & Q(date__range=date_range))
    elif department is not None and employee is not None and date_range is not None:
        print(2) 
        return (Q(employee__position__department_id=department) & Q(employee=employee) & Q(date__range=date_range))
    elif department is not None and employee is not None and status is not None:
        print(3) 
        if period == "AM":
            return (Q(employee__position__department_id=department) & Q(employee=employee) & Q(am_status=status))
        else:
            return (Q(employee__position__department_id=department) & Q(employee=employee) & Q(pm_status=status))
    elif department is not None and employee is not None:
        print(4) 
        return (Q(employee__position__department_id=department) & Q(employee=employee))
    elif department is not None and status is not None:
        print(5) 
        if period == "AM":
            return (Q(employee__position__department_id=department) & Q(am_status=status))
        else:
            return (Q(employee__position__department_id=department) & Q(pm_status=status))
    elif department is not None and date_range is not None:
        print(5) 
        return (Q(employee__position__department_id=department) & Q(date__range=date_range))
    elif department_head is not None and employee is not None and status is not None and date_range is not None:
        print(6) 
        if period == "AM":
            return (Q(employee__position__department__department_head_id=department_head) & Q(employee=employee) & Q(am_status=status) & Q(date__range=date_range))
        else:
            return (Q(employee__position__department__department_head_id=department_head) & Q(employee=employee) & Q(pm_status=status) & Q(date__range=date_range))
    elif department_head is not None and employee is not None and status is not None and date_range is not None:
        print(7) 
        if period == "AM":
            return (Q(employee__position__department__department_head_id=department_head) & Q(employee=employee) & Q(am_status=status) & Q(date__range=date_range))
        else:
            return (Q(employee__position__department__department_head_id=department_head) & Q(employee=employee) & Q(pm_status=status) & Q(date__range=date_range))
    elif department_head is not None and employee is not None and date_range is not None:
        print(8) 
        return (Q(employee__position__department__department_head_id=department_head) & Q(employee=employee) & Q(date__range=date_range))
    elif department_head is not None and employee is not None and status is not None:
        print(9) 
        if period == "AM":
            return (Q(employee__position__department__department_head_id=department_head) & Q(employee=employee) & Q(am_status=status))
        else:
            return (Q(employee__position__department__department_head_id=department_head) & Q(employee=employee) & Q(pm_status=status))
    elif department_head is not None and employee is not None:
        print(10) 
        return (Q(employee__position__department__department_head_id=department_head) & Q(employee=employee))
    elif department_head is not None and status is not None:
        print(11) 
        if period == "AM":
            return (Q(employee__position__department__department_head_id=department_head) & Q(am_status=status))
        else:
            return (Q(employee__position__department__department_head_id=department_head) & Q(pm_status=status))
    elif employee is not None and status is not None and date_range is not None:
        print(12) 
        if period == "AM":
            return (Q(employee=employee) & Q(am_status=status) & Q(date__range=date_range))
        else:
            return (Q(employee=employee) & Q(pm_status=status) & Q(date__range=date_range))
    elif employee is not None and date_range is not None:
        print(13) 
        return (Q(employee=employee) & Q(date__range=date_range))
    elif employee is not None and status is not None:
        print(14) 
        if period == "AM":
            return (Q(employee=employee) & Q(am_status=status))
        else:
            return (Q(employee=employee) & Q(pm_status=status))
    elif employee is not None:
        print(15) 
        return (Q(employee=employee))
    elif status is not None and date_range is not None:
        print(16) 
        if period == "AM":
            return (Q(am_status=status) & Q(date__range=date_range))
        else:
            return (Q(pm_status=status) & Q(date__range=date_range))
    elif date_range is not None:
        print(17) 
        return (Q(date__range=date_range))
    elif department is not None:
        print(18) 
        return (Q(employee__position__department_id=department))
    elif department_head is not None:
        # print(19) 
        return (Q(employee__position__department__department_head_id=department_head))
    elif employee is not None:
        print(20) 
        return (Q(employee=employee))
    elif status is not None:
        print(21) 
        if period == "AM":
            return (Q(am_status=status))
        elif period == "PM":
            return (Q(pm_status=status))
        else:
            return (Q(am_status=status) | Q(pm_status=status))

def benefit(kwargs):

    department = kwargs.get('department')
    employee = kwargs.get('employee')
    deadline = kwargs.get('deadline')

    if department is not None and employee is not None and deadline is not None:
        print(1) 
        return (Q(employee__position__department_id=department) & Q(employee=employee) & Q(contribution_deadline=deadline))
    elif department is not None and employee is not None:
        print(4) 
        return (Q(employee__position__department_id=department) & Q(employee=employee))
    elif employee is not None and deadline is not None:
        print(11) 
        return (Q(employee=employee) & Q(contribution_deadline=deadline))
    elif employee is not None :
        print(14) 
        return (Q(employee=employee))
    elif deadline is not None:
        print(17) 
        return (Q(contribution_deadline=deadline))
    elif department is not None:
        print(18) 
        return (Q(employee__position__department_id=department))
    else:
        print(22) 
        return ({})

def employee(kwargs):

    department = kwargs.get('department')
    employee_type = kwargs.get('employee_type')
    employee_status = kwargs.get('employee_status')
    sur_name = kwargs.get('sur_name')
    birthdate = kwargs.get('birthdate')
    birthplace = kwargs.get('birthplace')
    height = kwargs.get('height')
    height_range = kwargs.get('height_range')
    weight = kwargs.get('weight')
    weight_range = kwargs.get('weight_range')
    sex = kwargs.get('sex')
    date_hired = kwargs.get('date_hired')
    date_hired_range = kwargs.get('date_hired_range')
    search = kwargs.get('search')

    if height_range is not None:
        height_range = height_range.split(':')

    if weight_range is not None:
        weight_range = weight_range.split(':')

    if date_hired_range is not None:
        date_hired_range = date_hired_range.split(':')
        
    if department is not None and employee_type is not None and employee_status is not None and sur_name is not None and sex is not None and date_hired_range is not None:
        return (Q(position__department_id=department) & Q(employee_type=employee_type) & Q(employee_status=employee_status) & Q(sur_name__icontains=sur_name) & Q(sex=sex) & Q(date_hired__range=date_hired_range))
    elif department is not None and employee_type is not None and employee_status is not None and sur_name is not None and sex is not None:
        print(1) 
        return (Q(position__department_id=department) & Q(employee_type=employee_type) & Q(employee_status=employee_status) & Q(sur_name__icontains=sur_name) & Q(sex=sex))
    elif department is not None and employee_type is not None and employee_status is not None and sex is not None:
        print(1) 
        return (Q(position__department_id=department) & Q(employee_type=employee_type) & Q(employee_status=employee_status) & Q(sex=sex))
    elif department is not None and employee_type is not None and employee_status is not None:
        print(2) 
        return (Q(position__department_id=department) & Q(employee_type=employee_type) & Q(employee_status=employee_status))
    elif department is not None and employee_type is not None:
        print(3) 
        return (Q(position__department_id=department) & Q(employee_type=employee_type))
    elif department is not None and employee_status is not None and sur_name is not None:
        print(4) 
        return (Q(position__department_id=department) & Q(employee_status=employee_status) & Q(sur_name__icontains=sur_name))
    elif department is not None and employee_status is not None and sex is not None:
        print(4) 
        return (Q(position__department_id=department) & Q(employee_status=employee_status) & Q(sex=sex))
    elif department is not None and employee_status is not None:
        print(4) 
        return (Q(position__department_id=department) & Q(employee_status=employee_status))
    elif department is not None and sex is not None:
        print(4) 
        return (Q(position__department_id=department) & Q(sex=sex))
    elif department is not None and date_hired_range is not None:
        print(100) 
        return (Q(position__department_id=department) & Q(date_hired__range=date_hired_range))
    elif department is not None:
        print(5) 
        return (Q(position__department_id=department))
    elif employee_type is not None and employee_status is not None:
        print(7) 
        return (Q(employee_type=employee_type) & Q(employee_status=employee_status))
    elif employee_type is not None and sex is not None:
        print(8) 
        return (Q(employee_type=employee_type) & Q(sex=sex))
    elif employee_type is not None:
        print(9) 
        return (Q(employee_type=employee_type))
    elif employee_status is not None and sur_name is not None and sex is not None:
        print(10) 
        return (Q(employee_status=employee_status) & Q(sur_name__icontains=sur_name) & Q(sex=sex))
    elif employee_status is not None and sex is not None:
        print(11) 
        return (Q(employee_status=employee_status) & Q(sex=sex))
    elif employee_status is not None:
        print(12) 
        return (Q(employee_status=employee_status))
    elif sur_name is not None and sex is not None:
        print(9) 
        return (Q(sur_name__icontains=sur_name) & Q(sex=sex))
    elif sur_name is not None:
        print(9) 
        return (Q(sur_name__icontains=sur_name))
    elif birthdate is not None:
        print(10) 
        return (Q(birthdate=birthdate))
    elif birthplace is not None:
        print(11) 
        return (Q(birthplace=birthplace))
    elif sex is not None:
        print(12) 
        return (Q(sex=sex))
    elif height is not None:
        print(13) 
        return (Q(height=height))
    elif height_range is not None:
        print(14)
        return (Q(height__range=height_range))
    elif weight is not None:
        print(15) 
        return (Q(weight=weight))
    elif weight_range is not None:
        print(16)
        return (Q(weight__range=weight_range))
    elif date_hired is not None:
        print(17) 
        return (Q(date_hired=date_hired))
    elif date_hired_range is not None:
        print(18) 
        return (Q(date_hired__range=date_hired_range))
    elif search is not None:
        return ((
                Q(id=search_int(search)) |
                Q(employee_no__icontains=search) |
                Q(employee_type=search_employee_type(search)) |
                Q(employee_status=search_employee_status(search)) |
                Q(birthdate__icontains=search) |
                Q(birthplace=search_birthplace(search)) |
                Q(position=search_position(search)) |
                Q(position__department=search_dept(search)) |
                Q(sex=search_int(search)) |
                Q(date_hired__icontains=search) |
                Q(email__icontains=search) 
            ) | (
                search_full_name(search)
            )
        ) 
    else:
        return (Q(employee_status=1))


# Helper Functions

def search_int(value):
    try:
        return int(value)
    except:
        return 0

def search_full_name(search):
    for name in search.split():
        return (
            Q(sur_name__icontains = name) |
            Q(first_name__icontains = name) |
            Q(middle_name__icontains = name) |
            Q(name_extension = search_name_extension(name)) 
        )

def search_employee_type(search):
    data = models.EmployeeType.objects.filter(name__icontains = search)
    serializer = serializers.EmployeeType(data, many=True)
    if len(serializer.data) > 0:
        return serializer.data[0]['id']
    else:
        return 0 

def search_employee_status(search):
    data = models.EmployeeStatus.objects.filter(name__icontains = search)
    serializer = serializers.EmployeeStatus(data, many=True)
    if len(serializer.data) > 0:
        return serializer.data[0]['id']
    else:
        return 0 

def search_name_extension(search):
    data = models.NameExtension.objects.filter(name__icontains = search)
    serializer = serializers.NameExtension(data, many=True)
    if len(serializer.data) > 0:
        return serializer.data[0]['id']
    else:
        return 0 

def search_birthplace(search):
    data = models.City.objects.filter(name__icontains=search)
    serializer = serializers.City(data, many=True)
    if len(serializer.data) > 0:
        return serializer.data[0]['id']
    else:
        return 0
        
def search_position(search):
    data = models.Position.objects.filter(title__icontains=search)
    serializer = serializers.Position(data, many=True)
    if len(serializer.data) > 0:
        return serializer.data[0]['id']
    else:
        return 0
        
def search_dept(search):
    data = models.Position.objects.filter(department__name__icontains=search)
    serializer = serializers.Position(data, many=True)
    if len(serializer.data) > 0:
        return serializer.data[0]['department']
    else:
        return 0
