from django.db.models import fields
from django.db.models.query_utils import select_related_descend
from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

class AttendanceStatus(serializers.ModelSerializer):
    
    class Meta:
        model = models.AttendanceStatus
        fields = '__all__'

class Sex(serializers.ModelSerializer):
        
    class Meta:
        model = models.Sex
        fields = '__all__'

class MeasurementUnit(serializers.ModelSerializer):
        
    class Meta:
        model = models.MeasurementUnit
        fields = '__all__'

class Country(serializers.ModelSerializer):
        
    class Meta:
        model = models.Country
        fields = '__all__'

class Province(serializers.ModelSerializer):
        
    class Meta:
        model = models.Province
        fields = '__all__'

class City(serializers.ModelSerializer):
        
    class Meta:
        model = models.City
        fields = '__all__'

class Cities(serializers.ModelSerializer):
        
    class Meta:
        model = models.City
        fields = [
            'id',
            'name',
            'zip_code'
        ]

class Barangay(serializers.ModelSerializer):
        
    class Meta:
        model = models.Barangay
        fields = '__all__'
        
class Location(serializers.ModelSerializer):
        
    class Meta:
        model = models.Location
        fields = '__all__'
        
class Settings(serializers.ModelSerializer):
        
    class Meta:
        model = models.Settings
        fields = '__all__'
        
class Locations(serializers.ModelSerializer):
    
    barangay = Barangay(many=False, read_only=True)
    city = City(many=False, read_only=True)
    province = Province(many=False, read_only=True)
    country = Country(many=False, read_only=True)
    
    class Meta:
        model = models.Location
        fields = [
            'id',
            'blk_lot_no',
            'street',
            'subd_village',
            'barangay',
            'city',
            'province',
            'country'
        ]
        
class CivilStatus(serializers.ModelSerializer):
        
    class Meta:
        model = models.CivilStatus
        fields = '__all__'
        
class NameExtension(serializers.ModelSerializer):
        
    class Meta:
        model = models.NameExtension
        fields = '__all__'
        
class BloodType(serializers.ModelSerializer):
        
    class Meta:
        model = models.BloodType
        fields = '__all__'
        
class Citizenship(serializers.ModelSerializer):
        
    class Meta:
        model = models.Citizenship
        fields = '__all__'
        
class EmployeeType(serializers.ModelSerializer):
        
    class Meta:
        model = models.EmployeeType
        fields = '__all__'

class EmployeeStatus(serializers.ModelSerializer):
        
    class Meta:
        model = models.EmployeeStatus
        fields = '__all__'
        
class InventoryTransferStatus(serializers.ModelSerializer):
        
    class Meta:
        model = models.InventoryTransferStatus
        fields = '__all__'

class InventoryTransferMethod(serializers.ModelSerializer):
        
    class Meta:
        model = models.InventoryTransferMethod
        fields = '__all__'

class Salary(serializers.ModelSerializer):
        
    class Meta:
        model = models.Salary
        fields = '__all__'

class Position(serializers.ModelSerializer):
        
    class Meta:
        model = models.Position
        fields = '__all__'

class EmployeeName(serializers.ModelSerializer):

    name_extension = NameExtension(many=False, read_only=True)
        
    class Meta:
        model = models.Employee
        fields = ['id', 'sur_name','first_name','middle_name', 'name_extension']


class LeaveType(serializers.ModelSerializer):
        
    class Meta:
        model = models.LeaveType
        fields = '__all__'

class LeaveDetailOption(serializers.ModelSerializer):
        
    class Meta:
        model = models.LeaveDetailOption
        fields = '__all__'

class LeaveTypes(serializers.ModelSerializer):
        
    class Meta:
        model = models.LeaveType
        fields = '__all__'

class Biometrics(serializers.ModelSerializer):
        
    class Meta:
        model = models.Biometrics
        fields = '__all__'


class Employee(serializers.ModelSerializer):
        
    class Meta:
        model = models.Employee
        fields = '__all__'

class EmployeeNoAndName(serializers.ModelSerializer):
        
    class Meta:
        model = models.Employee
        fields = ['employee_no', 'sur_name', 'first_name']

class EmployeeNumbers(serializers.ModelSerializer):
        
    class Meta:
        model = models.Employee
        fields = ['id','employee_no']

class EmployeeContactInformation(serializers.ModelSerializer):
        
    class Meta:
        model = models.Employee
        fields = [ 'id', 'email', 'tel_no', 'mobile_no']

class UpdatePassword(serializers.ModelSerializer):
        
    class Meta:
        model = models.User
        fields = ['password']

class UpdateActiveStatus(serializers.ModelSerializer):
        
    class Meta:
        model = models.User
        fields = ['is_active']

class LeaveBalance(serializers.ModelSerializer):

    class Meta:
        model = models.LeaveBalance
        fields = '__all__'

class LeaveBalances(serializers.ModelSerializer):

    employee = Employee(many=False, read_only=True)
    leave_type = LeaveType(many=False, read_only=True)
        
    class Meta:
        model = models.LeaveBalance
        fields = [
            'id',
            'employee',
            'leave_type',
            'approved',
            'available'
        ]
        
class Children(serializers.ModelSerializer):
        
    class Meta:
        model = models.Children
        fields = '__all__'

class Attendance(serializers.ModelSerializer):
        
    class Meta:
        model = models.Attendance
        fields = '__all__'

class Attendances(serializers.ModelSerializer):
    
    employee = EmployeeNoAndName(many=False, read_only=True)
        
    class Meta:
        model = models.Attendance
        fields = [
            'id', 
            'employee', 
            'date', 
            'am_in', 
            'am_out', 
            'am_hrs', 
            'am_status',
            'pm_in', 
            'pm_out', 
            'pm_hrs', 
            'pm_status'
        ]

class Spouse(serializers.ModelSerializer):
        
    class Meta:
        model = models.Spouse
        fields = '__all__'

class Children(serializers.ModelSerializer):
        
    class Meta:
        model = models.Children
        fields = '__all__'

class Mother(serializers.ModelSerializer):
        
    class Meta:
        model = models.Mother
        fields = '__all__'

class Father(serializers.ModelSerializer):
        
    class Meta:
        model = models.Father
        fields = '__all__'

class EmployeeLeave(serializers.ModelSerializer):
        
    class Meta:
        model = models.EmployeeLeave
        fields = '__all__'

class EmployeeLeaves(serializers.ModelSerializer):
    
    leave_type = LeaveType(many=False, read_only=True)
    employee = Employee(many=False, read_only=True)
        
    class Meta:
        model = models.EmployeeLeave
        fields = [
            'id', 
            'leave_type',
            'days_applied',
            'other_details', 
            'start_date', 
            'end_date',
            'supervisor_remarks',
            'hr_remarks', 
            'application_date',
            'employee'
        ]

class GovernmentCompany(serializers.ModelSerializer):
        
    class Meta:
        model = models.GovernmentCompany
        fields = '__all__'

class GovernmentIssuedID(serializers.ModelSerializer):
        
    class Meta:
        model = models.GovernmentIssuedID
        fields = '__all__'

class ContributionDeadline(serializers.ModelSerializer):
        
    class Meta:
        model = models.ContributionDeadline
        fields = '__all__'

class Contribution(serializers.ModelSerializer):
        
    class Meta:
        model = models.Contribution
        fields = '__all__'

class Benefit(serializers.ModelSerializer):
        
    class Meta:
        model = models.Benefit
        fields = '__all__'    

class Benefits(serializers.ModelSerializer):

    employee = Employee(many=False, read_only=True)
    government_company = GovernmentCompany(many=False, read_only=True)
        
    class Meta:
        model = models.Benefit
        fields = [
            'id', 
            'government_company', 
            'employer_share',
            'employer_share_percent',
            'employee_share',
            'employee_share_percent',
            'contribution_deadline',
            'total',
            'total_percent',
            'employee'
        ]


class Department(serializers.ModelSerializer):

    class Meta:
        model = models.Department
        fields = '__all__'
        
class Departments(serializers.ModelSerializer):
    
    location = Locations(many=False, read_only=True)
        
    class Meta:
        model = models.Department
        fields = [
            'id',
            'name',
            'location',
            'department_head_id',
            'email',
            'tel_no',
            'image',
            'created_at',
        ]
        
class DepartmentName(serializers.ModelSerializer):
        
    class Meta:
        model = models.Department
        fields = ['name']

class ContentType(serializers.ModelSerializer):
        
    class Meta:
        model = models.ContentType
        fields = '__all__'

class ContentTypes(serializers.ModelSerializer):
        
    class Meta:
        model = models.ContentType
        fields = ['content_type']

class Report(serializers.ModelSerializer):
        
    class Meta:
        model = models.Report
        fields = '__all__'

class UserType(serializers.ModelSerializer):
        
    class Meta:
        model = models.UserType
        fields = '__all__'

class Role(serializers.ModelSerializer):
        
    class Meta:
        model = models.Role
        fields = '__all__'

class Roles(serializers.ModelSerializer):

    user_type = UserType(many=False, read_only=True)

    class Meta:
        model = models.Role
        fields = [
            'id',
            'title',
            'user_type'
        ]

class ReportType(serializers.ModelSerializer):
        
    class Meta:
        model = models.ReportType
        fields = '__all__'

class User(serializers.ModelSerializer):
        
    class Meta:
        model = models.User
        fields = '__all__'

class Users(serializers.ModelSerializer):
    role = Roles(many=False, read_only=True)

    class Meta:
        model = models.User
        fields = [
            'id', 
            'username', 
            'first_name', 
            'sur_name', 
            'email', 
            'password', 
            'role', 
            'is_active', 
            'image', 
            'employee', 
            'created_at', 
            'is_deactivated'
        ]

class Permission(serializers.ModelSerializer):
        
    class Meta:
        model = models.Permission
        fields = '__all__'

class Permissions(serializers.ModelSerializer):
    
    content_type = ContentType(many=False, read_only=True)
        
    class Meta:
        model = models.Permission
        fields = [
            'id', 
            'description', 
            'code_name', 
            'content_type'
        ]

class Group(serializers.ModelSerializer):
        
    class Meta:
        model = models.Group
        fields = '__all__'

class GroupPermission(serializers.ModelSerializer):
        
    class Meta:
        model = models.GroupPermissions
        fields = '__all__'

class GroupPermissions(serializers.ModelSerializer):

    group = Group(many=False, read_only=True)
    permission = Permission(many=False, read_only=True)
        
    class Meta:
        model = models.GroupPermissions
        fields = ['id', 'group', 'permission']

class UserGroup(serializers.ModelSerializer):
        
    class Meta:
        model = models.UserGroup
        fields = '__all__'

class UserGroups(serializers.ModelSerializer):

    group = Group(many=False, read_only=True)
    user = User(many=False, read_only=True)
        
    class Meta:
        model = models.UserGroup
        fields = ['id', 'group', 'user']

class EmployeeEmails(serializers.ModelSerializer):
        
    class Meta:
        model = models.Employee
        fields = ['id','email']

class UserEmails(serializers.ModelSerializer):
        
    class Meta:
        model = models.User
        fields = ['id','email']
        
class Positions(serializers.ModelSerializer):

    department = Department(many=False, read_only=True)
    salary = Salary(many=False, read_only=True)
        
    class Meta:
        model = models.Position
        fields = [
            'id',
            'title', 
            'department',
            'salary', 
            'is_vacant',
            'created_at'
        ]
        
class EmployeeNames(serializers.ModelSerializer):
    
    class Meta:
        model = models.Employee
        fields = [
            'id',
            'first_name',
            'middle_name',
            'sur_name',
        ]

        
class Employees(serializers.ModelSerializer):
  
    employee_type = EmployeeType(many=False, read_only=True)
    name_extension = NameExtension(many=False, read_only=True)
    birthplace = City(many=False, read_only=True)
    citizenship = Citizenship(many=False, read_only=True)
    civil_status = CivilStatus(many=False, read_only=True)
    blood_type = BloodType(many=False, read_only=True)
    position = Positions(many=False, read_only=True)
    
        
    class Meta:
        model = models.Employee
        fields = [
            'id', 
            'employee_no', 
            'employee_type',
            'sur_name', 
            'first_name', 
            'middle_name',
            'name_extension', 
            'sex', 
            'birthdate', 
            'birthplace', 
            'height', 
            'weight', 
            'blood_type', 
            'civil_status', 
            'citizenship', 
            'email',
            'mobile_no',
            'tel_no',
            'image',
            'position',
            'employee_status',
            'start_date', 
            'end_date',
            'date_hired'
        ]

class GetWorkInfo(serializers.ModelSerializer):
 
    position = Positions(many=False, read_only=True)
    
    class Meta:
        model = models.Employee
        fields = [
            'id', 
            'employee_type',
            'position',
            'start_date',
            'end_date',
            'date_hired'
        ]

class EmployeeStatusHistory(serializers.ModelSerializer):
        
    class Meta:
        model = models.EmployeeStatusHistory
        fields = '__all__'
        
class EmployeeID(serializers.ModelSerializer):
        
    class Meta:
        model = models.Employee
        fields = 'id'  
        
class LoginHistory(serializers.ModelSerializer):
        
    class Meta:
        model = models.LoginHistory
        fields = '__all__'  

class LoginHistories(serializers.ModelSerializer):

    user = Users(many=False, read_only=True)

    class Meta:
        model = models.LoginHistory
        fields = [
            'id', 
            'user', 
            'login', 
            'logout', 
            'duration', 
            'browser', 
            'ip_address', 
            'device'
        ]

class UpdateLoginHistory(serializers.ModelSerializer):
        
    class Meta:
        model = models.LoginHistory
        fields = ['logout', 'duration'] 

class UpdateDuration(serializers.ModelSerializer):
        
    class Meta:
        model = models.LoginHistory
        fields = ['duration']


class UserActivity(serializers.ModelSerializer):

    class Meta:
        model = models.UserActivity
        fields = '__all__'

class UserActivities(serializers.ModelSerializer):

    user = User(many=False, read_only=True)

    class Meta:
        model = models.UserActivity
        fields = [
            'id', 
            'user', 
            'type', 
            'action', 
            'description', 
            'ip_address', 
            'date',
        ]

class UserPermission(serializers.ModelSerializer):
 
    class Meta:
        model = models.UserPermissions
        fields = '__all__'

class UserPermissions(serializers.ModelSerializer):

    permission = Permission(many=False, read_only=True)
    user = User(many=False, read_only=True)
    
    class Meta:
        model = models.UserPermissions
        fields = ['id', 'user', 'permission']

class JobHistory(serializers.ModelSerializer):
        
    class Meta:
        model =  models.JobHistory
        fields = '__all__'

class JobHistories(serializers.ModelSerializer):

    position = Position(many=False, read_only=True)
    department = Department(many=False, read_only=True)
        
    class Meta:
        model =  models.JobHistory
        fields = [
            'id', 
            'start_date', 
            'end_date', 
            'created_at', 
            'department_head_id', 
            'position', 
            'department'
        ]

class EmployeeByDepartment(serializers.ModelSerializer):

    employee = Employee(many=False, read_only=True)
        
    class Meta:
        model =  models.JobHistory
        fields = ['id', 'employee']

class JobHistories(serializers.ModelSerializer):
  
    employee = Employee(many=False, read_only=True)
    department = Department(many=False, read_only=True)
        
    class Meta:
        model =  models.JobHistory
        fields = [ 
            'id', 
            'employee', 
            'position', 
            'department', 
            'start_date', 
            'end_date', 
            'created_at'
        ]

class PermanentAddress(serializers.ModelSerializer):
        
    class Meta:
        model = models.PermanentAddress
        fields = '__all__'

class ResidentialAddress(serializers.ModelSerializer):
        
    class Meta:
        model = models.ResidentialAddress
        fields = '__all__'

class EducationalBackground(serializers.ModelSerializer):
        
    class Meta:
        model = models.EducationalBackground
        fields = '__all__'

class CivilServiceEligibility(serializers.ModelSerializer):
        
    class Meta:
        model = models.CivilServiceEligibility
        fields = [ 
            'title', 
            'rating', 
            'exam_date', 
            'exam_place', 
            'license_number', 
            'license_validity_date'
        ]

class DepartmentFile(serializers.ModelSerializer):
        
    class Meta:
        model = models.DepartmentFile
        fields = '__all__'

class File(serializers.ModelSerializer):
        
    class Meta:
        model = models.File
        fields = '__all__'

class Announcement(serializers.ModelSerializer):
        
    class Meta:
        model = models.Announcement
        fields = '__all__'

class OfficeSupplyType(serializers.ModelSerializer):
  
    class Meta:
        model = models.OfficeSupplyType
        fields = '__all__'

class OfficeSupplyTransfer(serializers.ModelSerializer):
  
    class Meta:
        model = models.OfficeSupplyTransfer
        fields = '__all__'

class OfficeSupplyArticle(serializers.ModelSerializer):
        
    class Meta:
        model = models.OfficeSupplyArticle
        fields = '__all__'

class OfficeSupply(serializers.ModelSerializer):
  
    class Meta:
        model = models.OfficeSupply
        fields = '__all__'

class OfficeSupplyStock(serializers.ModelSerializer):
        
    class Meta:
        model = models.OfficeSupplyStock
        fields = '__all__'

class OfficeSupplyStocks(serializers.ModelSerializer):
        
    class Meta:
        model = models.OfficeSupplyStock
        fields = [
            'type',
            'article',
            'description',
            'measurement_unit',
            'unit_value',
            'quantity'
        ]
        
class OfficeSupplyRequest(serializers.ModelSerializer):
  
    class Meta:
        model = models.OfficeSupplyRequest
        fields = '__all__'

class EquipmentType(serializers.ModelSerializer):
        
    class Meta:
        model = models.EquipmentType
        fields = '__all__'

class EquipmentArticle(serializers.ModelSerializer):
        
    class Meta:
        model = models.EquipmentArticle
        fields = '__all__'

class Equipment(serializers.ModelSerializer):
        
    class Meta:
        model = models.Equipment
        fields = '__all__'
        
class Equipments(serializers.ModelSerializer):
   
    article = EquipmentArticle(many=False, read_only=True)
    type = EquipmentType(many=False, read_only=True)
    accountable_officer = Employee(many=False, read_only=True)

    class Meta:
        model = models.Equipment
        fields = [
            'id',
            'type',
            'fund_name_code',
            'accountable_officer',
            'article',
            'description',
            'property_number',
            'cost',
            'condition',
            'location',
            'remarks',
            'image',
            'receipt',
            'created_at',
        ]

class EquipmentRequest(serializers.ModelSerializer):
        
    class Meta:
        model = models.EquipmentRequest
        fields = '__all__'

class EquipmentTransfer(serializers.ModelSerializer):
        
    class Meta:
        model = models.EquipmentTransfer
        fields = '__all__'

class Session(serializers.ModelSerializer):
        
    class Meta:
        model = models.Session
        fields = '__all__'

class UpdateVisitedPages(serializers.ModelSerializer):
        
    class Meta:
        model = models.Session
        fields = ['visited_pages']
        
class Notification(serializers.ModelSerializer):
        
    class Meta:
        model = models.Notification
        fields = '__all__'

class Conversation(serializers.ModelSerializer):
        
    class Meta:
        model = models.Conversation
        fields = '__all__'
        
class ConversationReply(serializers.ModelSerializer):
        
    class Meta:
        model = models.ConversationReply
        fields = '__all__'