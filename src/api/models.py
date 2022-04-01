import os
from datetime import datetime
from django.db import models
from . import date
from fernet_fields import EncryptedTextField

class Settings(models.Model):
    
    probationary_period = models.IntegerField(default=6)
    am_start_time = models.CharField(max_length=30, default="", blank = True)
    am_end_time = models.CharField(max_length=30, default="", blank = True)
    pm_start_time = models.CharField(max_length=30, default="", blank = True)
    pm_end_time = models.CharField(max_length=30, default="", blank = True)
    grace_before_start_time = models.IntegerField(default=30)
    grace_after_start_time = models.IntegerField(default=15)
    grace_before_end_time = models.IntegerField(default=15)
    grace_after_end_time = models.IntegerField(default=30)
    am_in = models.CharField(max_length=55, default="")
    am_late = models.CharField(max_length=55, default="")
    am_absent = models.CharField(max_length=55, default="")
    am_undertime = models.CharField(max_length=55, default= "")
    am_out = models.CharField(max_length=55, default= "")
    pm_in = models.CharField(max_length=55, default="")
    pm_late = models.CharField(max_length=55, default="")
    pm_absent = models.CharField(max_length=55, default="")
    pm_undertime = models.CharField(max_length=55, default= "")
    pm_undertime = models.CharField(max_length=55, default= "")
    pm_out = models.CharField(max_length=55, default= "")
    min_emp_age = models.IntegerField(default=18)
    max_emp_age = models.IntegerField(default=60)
    admin_email = models.CharField(max_length=100, default="")
    app_email = models.CharField(max_length=100, default="")
   
    class Meta:
        db_table = "settings"


class EmployeeStatus(models.Model):
    
    name = models.CharField(max_length=55, default="")

    class Meta:
        db_table = "employee_status"


class AttendanceStatus(models.Model):
    
    name = models.CharField(max_length=55, default="")

    class Meta:
        db_table = "attendance_status"


class InventoryTransferStatus(models.Model):
    
    name = models.CharField(max_length=55, default="")
  
    class Meta:
        db_table = "inventory_transfer_status"


class InventoryTransferMethod(models.Model):
    
    name = models.CharField(max_length=55, default="")

    class Meta:
        db_table = "inventory_transfer_method"


class Citizenship(models.Model):
    
    name = models.CharField(max_length=10, unique=True, default="")

    class Meta:
        db_table = "citizenship"


class Sex(models.Model):
    
    name = models.CharField(max_length=10, unique=True, default="")

    class Meta:
        db_table = "sex"


class BloodType(models.Model):
    
    name = models.CharField(max_length=10, unique=True, default="")

    class Meta:
        db_table = "blood_type"


class MeasurementUnit(models.Model):
    
    name = models.CharField(max_length=10, unique=True, default="")
    description = models.CharField(max_length=55, default="")

    class Meta:
        db_table = "measurement_unit"


class Country(models.Model):
    
    name = models.CharField(max_length=55, unique=True, default="")

    class Meta:
        db_table = "country"


class Province(models.Model):
    
    name = models.CharField(max_length=55, unique=True, default="")

    class Meta:
        db_table = "province"
        
class City(models.Model):
    
    zip_code = models.IntegerField(unique=True, null=True, blank=True)
    name = models.CharField(max_length=55, default="")

    class Meta:
        db_table = "city"
        
class Barangay(models.Model):
    
    name = models.CharField(max_length=55, default="")

class Meta:
    db_table = "barangay"
        
class Location(models.Model):
    
    blk_lot_no = models.CharField(max_length=55, default="", blank=True)
    street = models.CharField(max_length=33, default="", blank=True)
    subd_village = models.CharField(max_length=55, default="", blank=True)
    barangay = models.ForeignKey(
        Barangay, on_delete=models.CASCADE, null=True)
    city = models.ForeignKey(
        City, on_delete=models.CASCADE, null=True)
    province = models.ForeignKey(
        Province, on_delete=models.CASCADE, null=True)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "location"


class LeaveType(models.Model):
    
    name = models.CharField(max_length=55, unique=True, default="")
    duration = models.CharField(max_length=30, default="")
    condition = models.CharField(max_length=55, default="")
    sex = models.ForeignKey(
        Sex, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "leave_type"


class LeaveDetailOption(models.Model):
    
    name = models.CharField(max_length=55, default="")
    leave_type = models.ForeignKey(
        LeaveType, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "leave_detail_option"
        
class CivilStatus(models.Model):
    
    name = models.CharField(max_length=55, unique=True, default="")

    class Meta:
        db_table = "civil_status"


class EmployeeType(models.Model):
    
    name = models.CharField(max_length=55, unique=True, default="")
    is_with_end_date = models.BooleanField(default=False)
    is_auto_generate_no = models.BooleanField(default=False)
    period = models.CharField(max_length=30, default="")

    class Meta:
        db_table = "employee_type"
        
        
class NameExtension(models.Model):
    
    name = models.CharField(max_length=55, unique=True, default="")
    description = models.CharField(max_length=55, default="")

    class Meta:
        db_table = "name_extension"
        

class Salary(models.Model):
    
    pay_grade = models.CharField(max_length = 5, unique=True, default="")
    amount = models.DecimalField(
        max_digits=20, decimal_places=2, default=0)

    class Meta:
        db_table = "salary"
        
class Department(models.Model):
    
    upload_to = "images/department/"
    default = "images/department/default.jpg"
    
    name = models.CharField(max_length=55, unique=True, default="")
    tel_no = models.CharField(max_length=15, default="None", blank=True) 
    email = models.CharField(max_length=100, default="None", blank=True)
    image = models.ImageField(upload_to=upload_to, default=default, null=True, blank=True, max_length=255)
    department_head_id = models.IntegerField(default=0)
    created_at = models.CharField(max_length=50, default=date.get_datetime())
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "department"
        
class Position(models.Model):
    
    title = models.CharField(max_length=55, default="")
    is_vacant = models.BooleanField(default=True, blank=True) 
    created_at = models.CharField(max_length =50, default="", blank=True)
    salary = models.ForeignKey(
        Salary, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, null=True)  

    class Meta:
        db_table = "position"
        
class Employee(models.Model):
    
    employee_no = models.CharField(max_length = 15, unique=True, default="")
    sur_name = models.CharField(max_length=55, default="")
    first_name = models.CharField(max_length=55, default="")
    middle_name = models.CharField(max_length=55, default="", blank=True)
    birthdate = models.CharField(max_length=11, default="", blank=True)
    age = models.IntegerField(default=0)
    height = models.IntegerField(default=0, blank=True)
    weight = models.IntegerField(default=0, blank=True)
    email = models.CharField(max_length=100, blank=True)
    mobile_no = models.CharField(max_length=15, default="", blank=True)
    tel_no = models.CharField(max_length=15, default="", blank=True)
    date_hired = models.CharField(max_length=50, default="", blank=True)  
    start_date = models.CharField(max_length=30, default="", blank=True)  
    end_date = models.CharField(max_length=30, default="", blank=True)  
    is_archived = models.BooleanField(default=False)
    image = models.ImageField(
        upload_to="images/employee/", 
        default="images/employee/default.png", 
        null=True, 
        blank=True, 
        max_length=255
    )
    employee_type = models.ForeignKey(
        EmployeeType, on_delete=models.CASCADE, null=True)  
    name_extension = models.ForeignKey(
        NameExtension, on_delete=models.CASCADE, null=True) 
    sex = models.ForeignKey(
        Sex, on_delete=models.CASCADE, null=True)
    birthplace = models.ForeignKey(
        City, on_delete=models.CASCADE, null=True, blank=True) 
    blood_type = models.ForeignKey(
        BloodType, on_delete=models.CASCADE, null=True, blank=True) 
    citizenship = models.ForeignKey(
        Citizenship, on_delete=models.CASCADE, null=True, blank=True) 
    civil_status = models.ForeignKey(
        CivilStatus, on_delete=models.CASCADE, null=True, blank=True) 
    position = models.ForeignKey(
        Position, on_delete=models.CASCADE, null=True) 
    employee_status = models.ForeignKey(
        EmployeeStatus, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "employee"


class EmployeeStatusHistory(models.Model):
    
    reason = models.CharField(max_length=100, default="New Hire", blank=True)
    comments = models.TextField(default="Welcome!")
    effective_date = models.CharField(max_length=30, default="", blank=True)
    modified_by = models.IntegerField(default=0)
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True)
    status = models.ForeignKey(
        EmployeeStatus, on_delete=models.CASCADE, null=True, default=1)

    class Meta:
        db_table = "employee_status_history"
                
class UserType(models.Model):
    
    type = models.CharField(max_length=30, default="")

    class Meta:
        db_table = "user_type"


class Role(models.Model):
    
    title = models.CharField(max_length=30, default="")
    user_type = models.ForeignKey(
        UserType, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = "role"


class Group(models.Model):
    
    name = models.CharField(max_length=55, default="")
        
    class Meta:
        db_table = "group"


class ReportType(models.Model):
    
    name = models.CharField(max_length=55, unique=True, default="")
    role = models.ForeignKey(
        Role, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = "report_type"
        
class User(models.Model):
    
    username = models.CharField(max_length=16, unique=True, default="")
    email = models.CharField(max_length=100, default="", blank=True)
    password = models.TextField(default="")
    sur_name = models.CharField(max_length=55, default="")
    first_name = models.CharField(max_length=55, default="")
    is_active = models.BooleanField(default=False)
    department = models.IntegerField(default=0, null=True)
    created_at = models.CharField(max_length=50, default="")
    is_archived = models.BooleanField(default=False)
    department_head_id = models.IntegerField(default=0)
    is_deactivated = models.BooleanField(default=False)
    image = models.ImageField(upload_to="images/user/", default="images/user/default.jpg", null=True, blank=True, max_length=255)
    role = models.ForeignKey(
        Role, on_delete=models.CASCADE, null=True, blank=True)
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        self.employee

    class Meta:
        db_table = "user"
        
class Conversation(models.Model):
    
    sender = models.IntegerField(default=0)
    reciever = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='conversation'

class ConversationReply(models.Model):
    
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField(max_length=255, default="", blank=True)
    is_seen = models.BooleanField(default=False)
    date_sent = models.DateTimeField(auto_now_add=True)
    visible_to = models.CharField(max_length=100, default="", blank=True)

    class Meta:
        db_table='conversation_reply'


def get_file_path(request, filename):
    nowTime = datetime.now().strftime('%Y%m%d%H:%M:%S')
    return os.path.join('media/departments', "%s%s" % (nowTime, filename))


class JobHistory(models.Model):
    
    date_hired = models.CharField(max_length=30, default="", blank=True)
    start_date = models.CharField(max_length=30, default="", blank=True)
    end_date = models.CharField(max_length=30, default="", blank=True)
    created_at = models.CharField(max_length=50, default="", blank=True)
    department_head_id = models.IntegerField(default=0)  
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True, blank=True)
    position = models.ForeignKey(
        Position, on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, null=True)
    
    class Meta:
        db_table = "job_history"


class Attendance(models.Model):
    
    date = models.CharField(max_length=12, default="")
    am_in = models.CharField(max_length=30, default="", blank = True)
    am_out = models.CharField(max_length=30, default="", blank = True)
    am_status = models.IntegerField(default=0)
    am_hrs = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    pm_in = models.CharField(max_length=30, default="", blank = True)
    pm_out = models.CharField(max_length=30, default="", blank = True)
    pm_hrs = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    pm_status = models.IntegerField(default=0)
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "attendance"


class PermanentAddress(models.Model):
    
    house_blk_lot_no = models.CharField(max_length=55, default="", blank=True)
    street = models.CharField(max_length=30, default="", blank=True)
    subd_village = models.CharField(max_length=55, default="", blank=True)
    barangay = models.CharField(max_length=55, default="", blank=True)
    city = models.CharField(max_length=55, default="", blank=True)
    province = models.CharField(max_length=55, default="", blank=True)
    country = models.CharField(max_length=55, default="", blank=True)
    created_at = models.CharField(max_length=30, default="", blank=True)
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        db_table = "permanent_address"
        
class ResidentialAddress(models.Model):
    
    house_blk_lot_no = models.CharField(max_length=55, default="", blank=True)
    street = models.CharField(max_length=30, default="", blank=True)
    subd_village = models.CharField(max_length=55, default="", blank=True)
    barangay = models.CharField(max_length=55, default="", blank=True)
    city = models.CharField(max_length=55, default="", blank=True)
    province = models.CharField(max_length=55, default="", blank=True)
    country = models.CharField(max_length=55, default="", blank=True)
    is_permanent = models.BooleanField(default=True)
    created_at = models.CharField(max_length=30, default="", blank=True)
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = "residential_address"


class Spouse(models.Model):
    
    sur_name = models.CharField(max_length=15, default="", blank=True)
    first_name = models.CharField(max_length=15, default="", blank=True)
    middle_name = models.CharField(max_length=55, default="", blank=True)
    occupation = models.CharField(max_length=55, default="", blank=True)
    emp_bus_name = models.CharField(max_length=55, default="", blank=True)
    emp_bus_addr = models.CharField(max_length=55, default="", blank=True)
    emp_tel_no = models.CharField(max_length=55, default="", blank=True)
    created_at = models.CharField(max_length=50, default="", blank=True)
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True, blank=True)
    name_extension = models.ForeignKey(
        NameExtension, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "spouse"


class Children(models.Model):
    
    full_name = models.CharField(max_length=55, default="")
    birthdate = models.CharField(max_length=15, default="")
    created_at = models.CharField(max_length=50, default="")
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "children"


class Father(models.Model):
    
    sur_name = models.CharField(max_length=55, default="", blank=True)
    first_name = models.CharField(max_length=55, default="", blank=True)
    middle_name = models.CharField(max_length=55, default="")
    created_at = models.CharField(max_length=50, default="", blank=True)
    name_extension = models.ForeignKey(
        NameExtension, on_delete=models.CASCADE, null=True)
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "father"
        
        
class Mother(models.Model):
    
    sur_name = models.CharField(max_length=55, default="", blank=True)
    first_name = models.CharField(max_length=55, default="", blank=True)
    middle_name = models.CharField(max_length=55, default="")
    created_at = models.CharField(max_length=50, default="", blank=True)
    name_extension = models.ForeignKey(
        NameExtension, on_delete=models.CASCADE, null=True)
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "mother"


class EducationalBackground(models.Model):
    
    level = models.CharField(max_length=15, default="", blank=True)
    school_name = models.CharField(max_length=15, default="", blank=True)
    course = models.CharField(max_length=15, default="", blank=True)
    year_from = models.CharField(max_length = 5, default="", blank=True)
    year_to = models.CharField(max_length = 5, default="", blank=True)
    units_earned = models.IntegerField(default=0)
    date_graduated = models.CharField(max_length=15, default="", blank=True)
    created_at = models.CharField(max_length=50, default="", blank=True)
    employee = models.ForeignKey(
        Employee, on_delete =models.CASCADE, null=True)

    class Meta:
        db_table = "educational_background"


class ScholarshipAcadHonorsReceived(models.Model):
    
    name = models.CharField(max_length=15, default="")
    created_at = models.CharField(max_length=50, default="")
    educational_background = models.ForeignKey(
        EducationalBackground, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "scholarship_and_honors_received"


class CivilServiceEligibility(models.Model):
    
    title = models.CharField(max_length=55, default="")
    rating = models.CharField(max_length=15, default="")
    exam_date = models.CharField(max_length=15, default="")
    exam_place = models.CharField(max_length=15, default="")
    license_number = models.CharField(max_length=15, default="")
    license_validity_date = models.CharField(max_length=15, default="")
    created_at = models.CharField(max_length=50, default="")
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "civil_service_eligibility"


class WorkExperience(models.Model):
    
    inclusive_from = models.CharField(max_length=11, default="")
    inclusive_to = models.CharField(max_length=11, default="")
    position_title = models.CharField(max_length=15, default="")
    dept_agency_comp = models.CharField(max_length=55, default="")
    monthly_salary = models.CharField(max_length=30, default="")
    salary_pay_grade = models.CharField(max_length = 5, default="")
    appointment_status = models.CharField(max_length=15, default="")
    govt_service = models.CharField(max_length = 1, default="")
    created_at = models.CharField(max_length=50, default="")
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "work_experience"

    
class VoluntaryWork(models.Model):
    
    org_name = models.CharField(max_length=55, default="")
    org_address = models.TextField(max_length=255, default="")
    inclusive_from = models.CharField(max_length=11, default="")
    inclusive_to = models.CharField(max_length=11, default="")
    num_of_hours = models.IntegerField(default=0)
    position_work = models.CharField(max_length=30, default="")
    created_at = models.CharField(max_length=50, default="")
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "voluntary_work"


class LearningDevelopment(models.Model):
    
    title = models.CharField(max_length=55, unique=True, default="")
    inclusive_from = models.CharField(max_length=11, default="")
    inclusive_to = models.CharField(max_length=11, default="")
    num_of_hours = models.IntegerField(default=0)
    type_of_ld = models.CharField(max_length=30, default="")
    sponsored_by = models.CharField(max_length=55, default="")
    created_at = models.CharField(max_length=50, default="")
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True)
        
    class Meta:
        db_table = "learning_and_development"


class NonAcademicDistinction(models.Model):
    
    description = models.CharField(max_length=55, unique=True, default="")
    created_at = models.CharField(max_length=50, default="")
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "non_academic_distiction"


class Signature(models.Model):
    
    date = models.CharField(max_length=11, default="")
    date_signed = models.CharField(max_length=25, default="")
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True)
    attachement = models.ImageField(
        upload_to="images/signatures/%Y/%m/%d/", max_length=255)

    class Meta:
        db_table = "signature"


class Consanguity(models.Model):
    
    is_third_degree = models.BooleanField(default=False)
    is_fourth_degree = models.BooleanField(default=False)
    details = models.TextField(max_length=255, default="")
    created_at = models.CharField(max_length=50, default="")

    class Meta:
        db_table = "consanguity"


class AdministrativeOffense(models.Model):
    
    is_guilty = models.BooleanField(default=False)
    details = models.TextField(max_length=255, default="")
    created_at = models.CharField(max_length=50, default="")
    
    class Meta:
        db_table = "administrative_offense"


class CriminalCharge(models.Model):
    
    is_charged = models.BooleanField(default=False)
    details = models.TextField(max_length=255, default="")
    created_at = models.CharField(max_length=50, default="")
    
    class Meta:
        db_table = "criminal_charge"


class Conviction(models.Model):
    
    is_convicted = models.BooleanField(default=False)
    details = models.TextField(max_length=255, default="")
    created_at = models.CharField(max_length=50, default="")
    
    class Meta:
        db_table = "conviction"


class SeparatedFromService(models.Model):
    
    is_separated = models.BooleanField(default=False)
    details = models.TextField(max_length=255, default="")
    created_at = models.CharField(max_length=50, default="")
    
    class Meta:
        db_table = "separated_from_service"


class ElectionCandidate(models.Model):
    
    is_candidate = models.BooleanField(default=False)
    details = models.TextField(max_length=255, default="")
    created_at = models.CharField(max_length=50, default="")
    
    class Meta:
        db_table = "election_candidate"


class ResignedFromGovernmentService(models.Model):
    
    is_resigned = models.BooleanField(default=False)
    details = models.TextField(max_length=255, default="")
    created_at = models.CharField(max_length=50, default="")
    
    class Meta:
        db_table = "resigned_from_government_service"


class AcquiredResidentStatus(models.Model):
    
    is_acquired = models.BooleanField(default=False)
    details = models.TextField(max_length=255, default="")
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "acquired_resident_status"


class IndigenousGroup(models.Model):
    
    is_member = models.BooleanField(default=False)
    id_number = models.TextField(max_length=255, default="")
    created_at = models.CharField(max_length=50, default="")
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "indigenous_group"


class PersonWithDisability(models.Model):
    
    is_disabled = models.BooleanField(default=False)
    id_number = models.TextField(max_length=255, default="")
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True)
    created_at = models.CharField(max_length=50, default="")

    class Meta:
        db_table = "person_with_disability"


class SolorParent(models.Model):
    
    is_solo_parent = models.BooleanField(default=False)
    id_number = models.TextField(max_length=255, default="")
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True)
    created_at = models.CharField(max_length=50, default="")

    class Meta:
        db_table = "solo_parent"


class SkillAndHobby(models.Model):
    
    description = models.CharField(max_length=55, unique=True, default="")
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True)
    created_at = models.CharField(max_length=50, default="")

    class Meta:
        db_table = "skill_and_hobby"
        

class Reference(models.Model):
    
    name = models.CharField(max_length=55, default="")
    address = models.TextField(max_length=255, default="")
    tel_no = models.CharField(max_length=11, default="")
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True)
    created_at = models.CharField(max_length=50, default="")

    class Meta:
        db_table = "reference"


class Oath(models.Model):
    
    signature = models.CharField(max_length=30, default="")
    date_accomplished = models.TextField(max_length=15, default="")
    right_thumbmark = models.ImageField(upload_to="folders/righ_thumbmarks/images/", max_length=255)
    person_administiring_oath = models.CharField(max_length=55, default="")
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "oath"


class Biometrics(models.Model):
    
    signature = models.CharField(max_length=30, default="")
    issuance_date = models.CharField(max_length=11, default="")
    issuance_place = models.CharField(max_length=30, default="")
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "biometrics"


class EmployeeLeave(models.Model):
    
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True)
    leave_type = models.ForeignKey(
        LeaveType, on_delete=models.CASCADE, null=True)
    other_details = models.CharField(max_length=100, default="", blank=True)
    days_applied = models.IntegerField(default=0)
    start_date = models.CharField(max_length=30, default="")
    end_date = models.CharField(max_length=30, default="")
    supervisor_remarks = models.IntegerField(default=0)
    supervisor_approval_date = models.CharField(max_length=30, default="")
    hr_remarks = models.IntegerField(default=0)
    hr_approval_date = models.CharField(max_length=30, default="")
    is_commutation_requested = models.BooleanField(default=False)
    application_date = models.CharField(max_length=30, default="")
    
    class Meta:
        db_table = "employee_leave"


class LeaveBalance(models.Model):
    
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True, blank=True)
    leave_type = models.ForeignKey(
        LeaveType, on_delete=models.CASCADE, null=True, blank=True)
    approved = models.IntegerField(default=0, blank=True)
    available = models.IntegerField(default=0, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    class Meta:
        db_table = "leave_balance"


class GovernmentCompany(models.Model):
    
    name = models.CharField(max_length=55, default="")

    class Meta:
        db_table = "government_company"


class GovernmentIssuedID(models.Model):
    
    company = models.ForeignKey(
        GovernmentCompany, on_delete=models.CASCADE, null=True)
    id_number = models.CharField(max_length=30, default="")
    issuance_date = models.CharField(max_length=11, default="")
    issuance_place = models.CharField(max_length=30, default="")
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True)
    created_at = models.CharField(max_length=50, default="")

    class Meta:
        db_table = "government_issued_id"


class ContributionDeadline(models.Model):
    
               
    government_company = models.ForeignKey(
        GovernmentCompany, on_delete=models.CASCADE, null=True)
    title=models.CharField(max_length=55, default="")
    description=models.CharField(max_length=100, default="")

    class Meta: 
        db_table = "contribution_deadline"


class Contribution(models.Model):
    
    government_company = models.ForeignKey(
        GovernmentCompany, on_delete=models.CASCADE, null=True)
    min_salary = models.DecimalField(
        max_digits=20, decimal_places=2, default=0)
    max_salary = models.DecimalField(
        max_digits=20, decimal_places=2, default=0)
    employer_share = models.DecimalField(
        max_digits=20, decimal_places=2, default=0)
    employee_share = models.DecimalField(
        max_digits=20, decimal_places=2, default=0)
    created_at = models.CharField(max_length=30, default="")

    class Meta:
        db_table = "contribution"


class Benefit(models.Model):
    
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True)
    government_company = models.ForeignKey(
        GovernmentCompany, on_delete=models.CASCADE, null=True)
    employer_share = models.DecimalField(
        max_digits=20, decimal_places=2, default=0)
    employer_share_percent = models.CharField(max_length=10, default="")
    employee_share = models.DecimalField(
        max_digits=20, decimal_places=2, default=0)
    employee_share_percent = models.CharField(max_length=10, default="")
    total = models.DecimalField(
        max_digits=20, decimal_places=2, default=0) 
    total_percent = models.CharField(max_length=10, default="")
    contribution_deadline = models.CharField(max_length=30, default="")
    date_added = models.CharField(max_length=30, default="")
    
    class Meta:
        db_table = "benefit"


class ContentType(models.Model):
    
    content_type = models.CharField(max_length=55, unique=True, default="")

    class Meta:
        db_table = "content_type"


class Permission(models.Model):
    
    description = models.CharField(max_length=55, unique=True, default="")
    code_name = models.CharField(max_length=55, unique=True, default="")
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "permission"


class GroupPermissions(models.Model):
    
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, null=True)
    permission = models.ForeignKey(
        Permission, on_delete=models.CASCADE, null=True)
    
    class Meta:
        db_table = "group_permissions"


class UserGroup(models.Model):
    
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True)
    
    class Meta:
        db_table = "user_group"


class File(models.Model):
    
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=155, default="", blank=True)
    description = models.TextField(default="", blank=True)
    size = models.IntegerField(default=0, blank=True)
    type = models.CharField(max_length=55, default="", blank=True)
    path = models.FileField(upload_to="files/user/", default="", null=True, blank=True, max_length=255)
    date_uploaded = models.CharField(max_length=25, default="", blank=True)

    class Meta:
        db_table = "file"


class DepartmentFile(models.Model):
    
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=155, default="", blank=True)
    description = models.TextField(default="", blank=True)
    size = models.IntegerField(default=0, blank=True)
    type = models.CharField(max_length=55, default="", blank=True)
    path = models.FileField(upload_to="files/department/", default="", null=True, blank=True, max_length=255)
    date_uploaded = models.CharField(max_length=25, default="", blank=True)

    class Meta:
        db_table = "department_file"


class OfficeSupplyType(models.Model):
    
    name = models.CharField(max_length=55, default="")
        
    class Meta:
        db_table="office_supply_type"


class OfficeSupplyArticle(models.Model):
    
    name = models.CharField(max_length=55, default="")
    type = models.ForeignKey(    
        OfficeSupplyType, on_delete=models.CASCADE, null=True)
        
    class Meta:
        db_table="office_supply_article"


class OfficeSupply(models.Model):
    
    type = models.ForeignKey(    
        OfficeSupplyType, on_delete=models.CASCADE, null=True)
    fund_name_code = models.CharField(max_length=55, default="")
    article = models.ForeignKey(    
        OfficeSupplyArticle, on_delete=models.CASCADE, null=True, blank=True)
    accountable_officer = models.ForeignKey(    
        Employee, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(max_length=255, default="")
    stock_number = models.CharField(max_length=55, default="", unique=True)
    measurement_unit = models.ForeignKey(    
        MeasurementUnit, on_delete=models.CASCADE, null=True, blank=True)
    unit_value = models.DecimalField(
        max_digits=20, decimal_places=2, default=0)
    balance_per_card = models.IntegerField(default=0, blank=True)
    on_hand_per_count = models.IntegerField(default=0, blank=True)
    total = models.DecimalField(
        max_digits=20, decimal_places=2, default=0)
    shortage = models.IntegerField(default=0, blank=True)
    overage = models.IntegerField(default=0, blank=True)
    remarks = models.CharField(max_length=100, default="")
    image = models.ImageField(upload_to="images/inventory/office_supply/", default="images/office_supply/item_image/default.jpg", null=True, blank=True, max_length=255)
    receipt = models.FileField(upload_to="files/inventory/receipt/office_supply/", default="", null=True, blank=True, max_length=255)
    created_at = models.CharField(max_length=30, default="")

    class Meta:
        db_table = "office_supply"


class OfficeSupplyStock(models.Model):
    
    type = models.ForeignKey(    
        OfficeSupplyType, on_delete=models.CASCADE, null=True)
    article = models.ForeignKey(    
        OfficeSupplyArticle, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(max_length=255, default="")
    measurement_unit = models.ForeignKey(    
        MeasurementUnit, on_delete=models.CASCADE, null=True, blank=True)
    unit_value = models.DecimalField(
        max_digits=20, decimal_places=2, default=0)
    quantity = models.IntegerField(default=0, blank=True)
    last_modified = models.CharField(max_length=30, default="")
    modified_by = models.IntegerField(default=0)

    class Meta:
        db_table = "office_supply_stock"
        
        
class OfficeSupplyRequest(models.Model):
    
    stock = models.ForeignKey(    
        OfficeSupplyStock, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=0)
    date_needed = models.CharField(max_length=30, default="")
    requested_by = models.IntegerField(default=0, blank=True)
    request_date = models.CharField(max_length=30, default="")
    is_approved = models.IntegerField(default=0)
    approved_by = models.IntegerField(default=0, blank=True)
    approved_date = models.CharField(max_length=30, default="")
    
    class Meta:
        db_table = "office_supply_request"


class OfficeSupplyTransfer(models.Model):
    
    stock = models.ForeignKey(    
        OfficeSupplyStock, on_delete=models.CASCADE, null=True, blank=True)
    request = models.ForeignKey(    
        OfficeSupplyRequest, on_delete=models.CASCADE, null=True, blank=True)
    method = models.ForeignKey(    
        InventoryTransferMethod, on_delete=models.CASCADE, null=True, blank=True)
    status = models.ForeignKey(    
        InventoryTransferStatus, on_delete=models.CASCADE, null=True, blank=True)
    is_recieved = models.BooleanField(default=False)
    date_recieved = models.CharField(max_length=30, default="")
    recieved_by = models.IntegerField(default=0)
    created_at = models.CharField(max_length=30, default="")

    class Meta:
        db_table = "office_supply_transfer"
        
class EquipmentType(models.Model):
    
    name = models.CharField(max_length=55, default="")
    
    class Meta:
        db_table = "equipment_type"


class EquipmentArticle(models.Model):
    
    name = models.CharField(max_length=55, default="")
    type = models.ForeignKey(    
        EquipmentType, on_delete=models.CASCADE, null=True)
        
    class Meta:
        db_table="equipment_article"


class Equipment(models.Model):
    
    type = models.ForeignKey(    
        EquipmentType, on_delete=models.CASCADE, null=True)
    article = models.ForeignKey(    
        EquipmentArticle, on_delete=models.CASCADE, null=True)
    fund_name_code = models.CharField(max_length=55, default="")
    property_number = models.CharField(max_length=55, default="", unique=True)
    accountable_officer = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=255, default="")
    cost = models.DecimalField(
        max_digits=20, decimal_places=2, default=0)
    location = models.TextField(max_length=255, default="")
    condition = models.CharField(max_length=100, default="")
    remarks = models.CharField(max_length=100, default="")
    image = models.ImageField(upload_to="images/equipment/item_image", default="images/equipment/item_image/default.jpg", null=True, blank=True, max_length=255)
    receipt = models.FileField(upload_to="files/inventory/receipt/equipment/", default="images/equipment/item_receipt/default.jpg", null=True, blank=True, max_length=255)
    created_at = models.CharField(max_length=50, default="") 

    class Meta:
        db_table = "equipment"
        
class EquipmentTransfer(models.Model):
    
    type = models.ForeignKey(    
        EquipmentType, on_delete=models.CASCADE, null=True)
    article = models.ForeignKey(    
        EquipmentArticle, on_delete=models.CASCADE, null=True)
    fund_name_code = models.CharField(max_length=55, default="")
    property_number = models.CharField(max_length=55, default="", unique=True)
    accountable_officer = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=255, default="")
    cost = models.DecimalField(
        max_digits=20, decimal_places=2, default=0)
    location = models.TextField(max_length=255, default="")
    condition = models.CharField(max_length=100, default="")
    remarks = models.CharField(max_length=100, default="")
    image = models.ImageField(upload_to="images/equipment/item_image", default="images/equipment/item_image/default.jpg", null=True, blank=True, max_length=255)
    receipt = models.FileField(upload_to="files/inventory/receipt/equipment/", default="images/equipment/item_receipt/default.jpg", null=True, blank=True, max_length=255)
    created_at = models.CharField(max_length=50, default="") 

    class Meta:
        db_table = "equipment_transfer"
        
class EquipmentRequest(models.Model):
    
    requested_by = models.IntegerField(default=0, blank=True)
    department = models.ForeignKey(    
        Department, on_delete=models.CASCADE, null=True, blank=True)
    request_date = models.DateTimeField(auto_now_add=True)
    equipment = models.ForeignKey(    
        Equipment, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=0)
    is_approved = models.BooleanField(default=False)
    approved_by = models.IntegerField(default=0, blank=True)
    approved_date = models.DateTimeField(auto_now_add=False, null=True)
    date_needed = models.CharField(max_length=30, default="")
    
    class Meta:
        db_table = "equipment_request"
        
    
class Report(models.Model):
    
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True)
    report_type = models.ForeignKey(
        ReportType, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    attachement = models.FileField(upload_to="files/reports/", default="", null=True, blank=True, max_length=255)
    is_archived = models.BooleanField(default=False)
    
    class Meta:
        db_table = "report"


class Announcement(models.Model):
    
    title = models.CharField(max_length=55, default="")
    description = models.TextField(max_length=255, default="")
    created_at = models.CharField(max_length=30, default="")

    class Meta:
        db_table = "announcement"


class UserPermissions(models.Model):
    
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    permission = models.ForeignKey(
        Permission, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = "user_permissions"


class LoginHistory(models.Model):
    
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True)
    browser = models.CharField(max_length=30, default="")
    device = models.CharField(max_length=30, default="")
    ip_address = models.CharField(max_length= 20, default="")
    login = models.CharField(max_length=30, default="")
    logout = models.CharField(max_length=30, default="--")
    duration = models.CharField(max_length=30, default="--")

    class Meta:
        db_table = "login_history"


class UserAction(models.Model):
    
    name = models.CharField(max_length=30, default="")

    class Meta:
        db_table = "user_action"


class UserActivity(models.Model):
    
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=100, default="")
    action = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=100, default="")
    ip_address = models.CharField(max_length = 20, default="")
    date = models.CharField(max_length=30, default="")

    class Meta:
        db_table = "user_activity"


class Session(models.Model):
    
    session_id = models.CharField(max_length = 80, primary_key=True)
    session_data = EncryptedTextField()
    
    class Meta:
        db_table = "session"
        
class Notification(models.Model):
    
    visible_to = models.TextField(default="")
    message = models.TextField(default="")
    date = models.CharField(max_length=30, default="")

    class Meta:
        db_table = "notification"
