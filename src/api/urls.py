from django.urls import path
from . import views

urlpatterns = [

  # functions
  path('is-new-email-available/<str:email>/', views.is_new_email_available, name='create-announcement'),

  # attendance status view 
  path('attendance-statuses/new/', views.AttendanceStatusView.post, name='create-attendance-status'),  
  path('attendance-statuses/', views.AttendanceStatusView.list, name='attendance-statuses'),  
  path('attendance-statuses/get/<int:id>/', views.AttendanceStatusView.get, name ='retrieve-attendance-status'),  
  path('attendance-statuses/search=<str:search>/', views.AttendanceStatusView.list, name ='attendance-statuses-by-search-term'),  
  path('attendance-statuses/entry=<int:entry>/', views.AttendanceStatusView.list, name ='total-attendance-statuses'),  
  path('attendance-statuses/total/', views.AttendanceStatusView.total, name ='total-attendance-statuses'),  
  path('attendance-statuses/update/<int:id>/', views.AttendanceStatusView.update, name ='update-attendance-status'),  

  # account request view
  path('account-requests/new/', views.AccountRequestView.post, name='request-account'),
  path('account-requests/', views.AccountRequestView.list, name='account-requests'),
  path('account-requests/approve/<int:id>/', views.AccountRequestView.approve_account, name='approve-account-request'),
  path('account-requests/decline/<int:id>/', views.AccountRequestView.decline_account, name='decline-account-request'),
  path('account-requests/update/<int:id>/', views.AccountRequestView.update, name='update-request'),
  
  # announcement view
  path('announcements/new/', views.AnnouncementView.post, name='create-announcement'),
  path('announcements/total/', views.AnnouncementView.total, name='total-announcement'),
  path('announcements/', views.AnnouncementView.list, name='announcments'), 
  path('announcements/update/<int:id>/', views.AnnouncementView.update, name='update-announcment'), 
  path('announcements/delete/<int:id>/', views.AnnouncementView.delete, name='delete-announcment'), 
  
  # attendance view
  path('attendances/new/', views.AttendanceView.post, name='create-attendance'),
  path('attendances/total/<int:employee>/', views.AttendanceView.total, name='total-attendances'),
  path('attendances/get-attendance/<int:employee>/<str:status>/', views.AttendanceView.get_attendance, name='get-days-present'),
  path('attendances/get/<int:employee>/<str:date>/', views.AttendanceView.get, name='retrieve attendance'),
  path('attendances/<int:employee>/<str:date>/', views.AttendanceView.list, name='retrieve-employee-attendance'),
  path('attendances/count/<str:status>/', views.AttendanceView.count_attendance, name='count-attendances'),
  path('attendances/update/<int:id>/', views.AttendanceView.update, name='update-attendance'),
  path('attendances/delete/', views.AttendanceView.delete, name='delete-attendances'),
  
  # by department and employee  
  path('attendances/department=<int:department>/employee=<int:employee>/status=<int:status>/date_range=<str:date_range>/order=<str:order>/', views.AttendanceView.list, name='attendances'),
  path('attendances/department=<int:department>/employee=<int:employee>/status=<int:status>/date_range=<str:date_range>/', views.AttendanceView.list, name='attendances'),
  path('attendances/department=<int:department>/employee=<int:employee>/date_range=<str:date_range>/order=<str:order>/', views.AttendanceView.list, name='attendances'),
  path('attendances/department=<int:department>/employee=<int:employee>/date_range=<str:date_range>/', views.AttendanceView.list, name='attendances'),
  path('attendances/department=<int:department>/employee=<int:employee>/status=<int:status>/order=<str:order>/', views.AttendanceView.list, name='retrieve-department-attendance'),
  path('attendances/department=<int:department>/employee=<int:employee>/status=<int:status>/', views.AttendanceView.list, name='retrieve-department-attendance'),
  path('attendances/department=<int:department>/employee=<int:employee>/order=<str:order>/', views.AttendanceView.list, name='retrieve-department-attendance'),
  path('attendances/department=<int:department>/employee=<int:employee>/', views.AttendanceView.list, name='retrieve-department-attendance'),
  
  # by department
  path('attendances/department=<int:department>/status=<int:status>/date_range=<str:date_range>/order=<str:order>/', views.AttendanceView.list, name='attendances'),
  path('attendances/department=<int:department>/status=<int:status>/date_range=<str:date_range>/', views.AttendanceView.list, name='attendances'),
  path('attendances/department=<int:department>/date_range=<str:date_range>/order=<str:order>/', views.AttendanceView.list, name='retrieve-department-attendance'),
  path('attendances/department=<int:department>/date_range=<str:date_range>/', views.AttendanceView.list, name='retrieve-department-attendance'),
  path('attendances/department=<int:department>/status=<int:status>/order=<str:order>/', views.AttendanceView.list, name='retrieve-department-attendance'),
  path('attendances/department=<int:department>/status=<int:status>/', views.AttendanceView.list, name='retrieve-department-attendance'),
  path('attendances/department=<int:department>/order=<str:order>/', views.AttendanceView.list, name='retrieve-department-attendance'),
  path('attendances/department=<int:department>/', views.AttendanceView.list, name='retrieve-department-attendance'),
  
  # leaves by department head and employee
  path('attendances/department_head=<int:department_head>/employee=<int:employee>/status=<int:status>/date_range=<str:date_range>/order=<str:order>/', views.AttendanceView.list, name='retrieve-department_head-attendance'),
  path('attendances/department_head=<int:department_head>/employee=<int:employee>/status=<int:status>/date_range=<str:date_range>/', views.AttendanceView.list, name='retrieve-department_head-attendance'),
  path('attendances/department_head=<int:department_head>/employee=<int:employee>/date_range=<str:date_range>/order=<str:order>/', views.AttendanceView.list, name='retrieve-department_head-attendance'),
  path('attendances/department_head=<int:department_head>/employee=<int:employee>/date_range=<str:date_range>/', views.AttendanceView.list, name='retrieve-department_head-attendance'),
  path('attendances/department_head=<int:department_head>/employee=<int:employee>/status=<int:status>/order=<str:order>/', views.AttendanceView.list, name='retrieve-department_head-attendance'),
  path('attendances/department_head=<int:department_head>/employee=<int:employee>/status=<int:status>/', views.AttendanceView.list, name='retrieve-department_head-attendance'),
  path('attendances/department_head=<int:department_head>/employee=<int:employee>/order=<str:order>/', views.AttendanceView.list, name='retrieve-department_head-attendance'),
  path('attendances/department_head=<int:department_head>/employee=<int:employee>/', views.AttendanceView.list, name='retrieve-department_head-attendance'),
  
  # leaves by department head
  path('attendances/department_head=<int:department_head>/status=<int:status>/date_range=<str:date_range>/order=<str:order>/', views.AttendanceView.list, name='attendances'),
  path('attendances/department_head=<int:department_head>/status=<int:status>/date_range=<str:date_range>/', views.AttendanceView.list, name='attendances'),
  path('attendances/department_head=<int:department_head>/date_range=<str:date_range>/order=<str:order>/', views.AttendanceView.list, name='retrieve-department_head-attendance'),
  path('attendances/department_head=<int:department_head>/date_range=<str:date_range>/', views.AttendanceView.list, name='retrieve-department_head-attendance'),
  path('attendances/department_head=<int:department_head>/status=<int:status>/order=<str:order>/', views.AttendanceView.list, name='retrieve-department_head-attendance'),
  path('attendances/department_head=<int:department_head>/status=<int:status>/', views.AttendanceView.list, name='retrieve-department_head-attendance'),
  path('attendances/department_head=<int:department_head>/order=<str:order>/', views.AttendanceView.list, name='retrieve-department-attendance'),
  path('attendances/department_head=<int:department_head>/', views.AttendanceView.list, name='retrieve-department-attendance'),

  # leaves by employee
  path('attendances/employee=<int:employee>/status=<int:status>/date_range=<str:date_range>/order=<str:order>/', views.AttendanceView.list, name='attendances'),
  path('attendances/employee=<int:employee>/status=<int:status>/date_range=<str:date_range>/', views.AttendanceView.list, name='attendances'),
  path('attendances/employee=<int:employee>/date_range=<str:date_range>/order=<str:order>/', views.AttendanceView.list, name='attendances'),
  path('attendances/employee=<int:employee>/date_range=<str:date_range>/', views.AttendanceView.list, name='attendances'),
  path('attendances/employee=<int:employee>/status=<int:status>/order=<str:order>/', views.AttendanceView.list, name='attendances'),
  path('attendances/employee=<int:employee>/status=<int:status>/', views.AttendanceView.list, name='attendances'),
  path('attendances/employee=<int:employee>/order=<str:order>/', views.AttendanceView.list, name='attendances'),
  path('attendances/employee=<int:employee>/', views.AttendanceView.list, name='attendances'),
  
  # default
  path('attendances/status=<int:status>/date_range=<str:date_range>/order=<str:order>/', views.AttendanceView.list, name='attendances'),
  path('attendances/status=<int:status>/date_range=<str:date_range>/', views.AttendanceView.list, name='attendances'),
  path('attendances/date_range=<str:date_range>/order=<str:order>/', views.AttendanceView.list, name='attendances'),
  path('attendances/date_range=<str:date_range>/', views.AttendanceView.list, name='attendances'),
  path('attendances/status=<int:status>/period=<int:period>/order=<str:order>/', views.AttendanceView.list, name='attendances'),
  path('attendances/status=<int:status>/period=<int:period>/', views.AttendanceView.list, name='attendances'),
  path('attendances/status=<int:status>/order=<str:order>/', views.AttendanceView.list, name='attendances'),
  path('attendances/status=<int:status>/', views.AttendanceView.list, name='attendances'),
  path('attendances/order=<str:order>/', views.AttendanceView.list, name='attendances'),
  path('attendances/', views.AttendanceView.list, name='attendances'),
  
  # contribution view 
  path('contributions/new/', views.ContributionView.post, name='create-contribution'),  
  path('contributions/', views.ContributionView.list, name='contributions'),  
  path('contributions/get/<int:id>/', views.ContributionView.get, name ='retrieve-contribution'),  
  path('contributions/search=<str:search>/', views.ContributionView.list, name ='contributions-by-search-term'),  
  path('contributions/entry=<int:entry>/', views.ContributionView.list, name ='total-contributions'),  
  path('contributions/update/<int:id>/', views.ContributionView.update, name ='update-contribution'),  
  path('contributions/delete/<int:id>/', views.ContributionView.delete, name='delete-contribution'),
  
  # contribution deadline view 
  path('contribution-deadlines/new/', views.ContributionDeadlineView.post, name='create-contribution-deadline'),  
  path('contribution-deadlines/', views.ContributionDeadlineView.list, name='contribution-deadlines'),  
  path('contribution-deadlines/get/<int:id>/', views.ContributionDeadlineView.get, name ='retrieve-contribution-deadline'),  
  path('contribution-deadlines/search=<str:search>/', views.ContributionDeadlineView.list, name ='contribution-deadlines-by-search-term'),  
  path('contribution-deadlines/entry=<int:entry>/', views.ContributionDeadlineView.list, name ='total-contribution-deadlines'),  
  path('contribution-deadlines/total/', views.ContributionDeadlineView.total, name ='total-contribution-deadlines'),  
  path('contribution-deadlines/update/<int:id>/', views.ContributionDeadlineView.update, name ='update-contribution-deadline'),  
  path('contribution-deadlines/delete/<int:id>/', views.ContributionDeadlineView.delete, name='delete-contribution-deadline'),
  
  # blood type view
  path('blood-types/new/', views.BloodTypeView.post, name='create-blood-type'),  
  path('blood-types/', views.BloodTypeView.list, name='blood-types'),  
  path('blood-types/search=<str:search>/', views.BloodTypeView.list, name ='blood-types-by-search-term'),  
  path('blood-types/entry=<int:entry>/', views.BloodTypeView.list, name ='total-blood-type'),  
  path('blood-types/total/', views.BloodTypeView.total, name ='total-blood-type'),  
  path('blood-types/get/<int:id>/', views.BloodTypeView.get , name ='retrieve-blood-type'),  
  path('blood-types/update/<int:id>/', views.BloodTypeView.update, name ='update-blood-type'),  
  path('blood-types/delete/<int:id>/', views.BloodTypeView.delete, name='delete-blood-type'),
  
  # benefit view
  path('benefits/new/', views.BenefitView.post, name='create-task'),
  path('benefits/search=<str:search>/', views.BenefitView.list, name='benefits-by-search'),    
  path('benefits/order=<str:order>/', views.BenefitView.list, name='benefits-by-order'),
  path('benefits/entry=<int:entry>/', views.BenefitView.list, name='benefits-by-entry'),
  path('benefits/total/', views.BenefitView.total, name='total-benefits'),
  path('benefits/<int:employee>/total/', views.BenefitView.total, name='total-benefits'),
  path('benefits/get/<int:employee>/', views.BenefitView.get, name='retrieve-employee-benefits'),
  path('benefits/get/<int:employee>/order=<str:order>/', views.BenefitView.get, name='retrieve-employee-benefits-by-order'),
  path('benefits/get/<int:employee>/entry=<str:entry>/', views.BenefitView.get, name='retrieve-employee-benefits-by-entry'),
  path('benefits/update/<int:id>/', views.BenefitView.update, name='update task'), 
  path('benefits/delete/<int:id>/', views.BenefitView.delete, name='delete task'),
  
  # by department and employee  
  path('benefits/department=<int:department>/employee=<int:employee>/deadline=<str:deadline>/order=<str:order>/', views.BenefitView.list, name='benefits'),
  path('benefits/department=<int:department>/employee=<int:employee>/deadline=<str:deadline>/', views.BenefitView.list, name='benefits'),
  path('benefits/department=<int:department>/employee=<int:employee>/order=<str:order>/', views.BenefitView.list, name='retrieve-department-benefit'),
  path('benefits/department=<int:department>/employee=<int:employee>/', views.BenefitView.list, name='retrieve-department-benefit'),
  
  # by department
  path('benefits/department=<int:department>/deadline=<str:deadline>/order=<str:order>/', views.BenefitView.list, name='benefits'),
  path('benefits/department=<int:department>/deadline=<str:deadline>/', views.BenefitView.list, name='retrieve-department-benefit'),
  path('benefits/department=<int:department>/order=<str:order>/', views.BenefitView.list, name='retrieve-department-benefit'),
  path('benefits/department=<int:department>/', views.BenefitView.list, name='retrieve-department-benefit'),
  
  # leaves by department head and employee
  path('benefits/department_head=<int:department_head>/employee=<int:employee>/deadline=<str:deadline>/order=<str:order>/', views.BenefitView.list, name='retrieve-department_head-benefit'),
  path('benefits/department_head=<int:department_head>/employee=<int:employee>/deadline=<str:deadline>/', views.BenefitView.list, name='retrieve-department_head-benefit'),
  path('benefits/department_head=<int:department_head>/employee=<int:employee>/order=<str:order>/', views.BenefitView.list, name='retrieve-department_head-benefit'),
  path('benefits/department_head=<int:department_head>/employee=<int:employee>/', views.BenefitView.list, name='retrieve-department_head-benefit'),
  
  # leaves by department head 
  path('benefits/department_head=<int:department_head>/deadline=<str:deadline>/order=<str:order>/', views.BenefitView.list, name='benefits'),
  path('benefits/department_head=<int:department_head>/deadline=<str:deadline>/', views.BenefitView.list, name='benefits'),
  path('benefits/department_head=<int:department_head>/order=<str:order>/', views.BenefitView.list, name='retrieve-department_head-benefit'),
  path('benefits/department_head=<int:department_head>/', views.BenefitView.list, name='retrieve-department_head-benefit'),
  
  # leaves by employee
  path('benefits/employee=<int:employee>/deadline=<str:deadline>/order=<str:order>/', views.BenefitView.list, name='benefits'),
  path('benefits/employee=<int:employee>/deadline=<str:deadline>/', views.BenefitView.list, name='benefits'),
  path('benefits/employee=<int:employee>/order=<str:order>/', views.BenefitView.list, name='benefits'),
  path('benefits/employee=<int:employee>/', views.BenefitView.list, name='benefits'),
  
  # default
  path('benefits/deadline=<str:deadline>/order=<str:order>/', views.BenefitView.list, name='benefits'),
  path('benefits/deadline=<str:deadline>/', views.BenefitView.list, name='benefits'),
  path('benefits/order=<str:order>/', views.BenefitView.list, name='benefits'),
  path('benefits/', views.BenefitView.list, name='benefits'),
  
  # barangay view 
  path('barangays/new/', views.BarangayView.post, name='create-barangay'),  
  path('barangays/', views.BarangayView.list, name='barangays'),  
  path('barangays/search=<str:search>/', views.BarangayView.list, name ='barangay-by-search-term'),  
  path('barangays/entry=<int:entry>/', views.BarangayView.list, name ='total-barangays'),  
  path('barangays/total/', views.BarangayView.total, name ='total-barangays'),  
  path('barangays/get/<int:id>/', views.BarangayView.get, name ='retrieve-barangay'),  
  path('barangays/update/<int:id>/', views.BarangayView.update, name ='update-barangay'),  
  path('barangays/delete/<int:id>/', views.BarangayView.delete, name ='delete-barangay'),
  
  # citizenship view 
  path('citizenships/new/', views.CitizenshipView.post, name='create-citizenship'),  
  path('citizenships/', views.CitizenshipView.list, name='citizenships'),  
  path('citizenships/search=<str:search>/', views.CitizenshipView.list, name ='citizenship-by-search-term'),  
  path('citizenships/entry=<int:entry>/', views.CitizenshipView.list, name ='total-citizenships'),  
  path('citizenships/total/', views.CitizenshipView.total, name ='total-citizenships'),  
  path('citizenships/get/<int:id>/', views.CitizenshipView.get, name ='retrieve-citizenship'),  
  path('citizenships/update/<int:id>/', views.CitizenshipView.update, name ='update-citizenship'),  
  path('citizenships/delete/<int:id>/', views.CitizenshipView.delete, name ='delete-citizenship'),  
  
  # city view 
  path('cities/new/', views.CityView.post, name='create-city'),  
  path('cities/', views.CityView.list, name='cities'),  
  path('cities/search=<str:search>/', views.CityView.list, name ='city-by-search-term'),  
  path('cities/entry=<int:entry>/', views.CityView.list, name ='total-cities'),  
  path('cities/total/', views.CityView.total, name ='total-cities'),  
  path('cities/get/<int:id>/', views.CityView.get, name ='retrieve-city'),  
  path('cities/update/<int:id>/', views.CityView.update, name ='update-city'),  
  path('cities/delete/<int:id>/', views.CityView.delete, name ='delete-city'),  
  
  # country view 
  path('countries/new/', views.CountryView.post, name='create-country'),  
  path('countries/', views.CountryView.list, name='countries'),  
  path('countries/search=<str:search>/', views.CountryView.list, name ='country-by-search-term'),  
  path('countries/entry=<int:entry>/', views.CountryView.list, name ='total-countries'),  
  path('countries/total/', views.CountryView.total, name ='total-countries'),  
  path('countries/get/<int:id>/', views.CountryView.get, name ='retrieve-country'),  
  path('countries/update/<int:id>/', views.CountryView.update, name ='update-country'),  
  path('countries/delete/<int:id>/', views.CountryView.delete, name ='delete-country'),  
  
  # civil status view 
  path('civil-statuses/new/', views.CivilStatusView.post, name='create-civil-status'),  
  path('civil-statuses/', views.CivilStatusView.list, name='civil-statuses'),  
  path('civil-statuses/get/<int:id>/', views.CivilStatusView.get, name ='retrieve-civil-status'),  
  path('civil-statuses/search=<str:search>/', views.CivilStatusView.list, name ='civil-statuses-by-search-term'),  
  path('civil-statuses/entry=<int:entry>/', views.CivilStatusView.list, name ='total-civil-statuses'),  
  path('civil-statuses/total/', views.CivilStatusView.total, name ='total-civil-statuses'),  
  path('civil-statuses/update/<int:id>/', views.CivilStatusView.update, name ='update-civil-status'),  
  path('civil-statuses/delete/<int:id>/', views.CivilStatusView.delete, name='delete-civil-status'),
  
  # conversation view
  path('conversations/new/', views.ConversationView.post, name='create-conversation'),
  path('conversations/<int:user>/', views.ConversationView.list, name='create-conversation'),
  path('conversations/get/<int:sender>/<int:reciever>/', views.ConversationView.get, name='check-conversation-existince'),
  
  # conversationReply view
  path('conversation-replies/new/', views.ConversationReplyView.post, name='create-conversation-reply'),
  
  # children view
  path('childrens/new/', views.ChildrenView.post, name='create-children'),
  path('childrens/get/<int:id>/', views.ChildrenView.get, name='retrieve-childrens'),
  path('childrens/<int:employee>/', views.ChildrenView.list, name='childrens'),
  path('childrens/update/<int:id>/', views.ChildrenView.update, name='update-childrens'),
  
  # content type view 
  path('content-types/new/', views.ContentTypeView.post, name='create-content-type'),  
  path('content-types/', views.ContentTypeView.list, name='content-types'),  
  path('content-types/entry=<int:entry>/', views.ContentTypeView.list, name ='total-content-types'),  
  path('content-types/total/', views.ContentTypeView.total, name ='total-content-types'),  
  path('content-types/update/<int:id>/', views.ContentTypeView.update, name ='update-content-type'),  

  # hr dashboard
  path('dashboard/employee-types/', views.DashboardView.employee_types, name='employee-types'),
  path('dashboard/employee-sex/', views.DashboardView.employee_sex, name='employee-sex'),
  path('dashboard/employee-age-ratio/', views.DashboardView.employee_age_ratio, name='employee-age-ratio'),
  path('dashboard/daily-attendance/<str:date_range>/', views.DashboardView.daily_attendance, name='daily_attendance'),
  path('dashboard/employee-monthly-attendance/<int:employee>/<str:start_date>/<str:end_date>/', views.DashboardView.daily_attendance, name='daily_attendance'),
  path('dashboard/super-admin/', views.DashboardView.super_admin_dashboard, name='super-admin-dashboard'),
  path('dashboard/admin/', views.DashboardView.admin_dashboard, name='admin-dashboard'),
  path('dashboard/hr/', views.DashboardView.hr_dashboard, name='hr-dashboard'),
  path('dashboard/inventory/', views.DashboardView.inventory_dashboard, name='inventory-dashboard'),
  path('dashboard/employee/<int:employee>/', views.DashboardView.employee_dashboard, name='employee-dashboard'),

  # report type view 
  path('report-types/new/', views.ReportTypeView.post, name='create-report-type'),  
  path('report-types/', views.ReportTypeView.list, name='report-types'),  
  path('report-types/get/<int:id>/', views.ReportTypeView.get, name ='retrieve-report-type'),  
  path('report-types/search=<str:search>/', views.ReportTypeView.list, name ='report-types-by-search-term'),  
  path('report-types/entry=<int:entry>/', views.ReportTypeView.list, name ='total-report-types'),  
  path('report-types/total/', views.ReportTypeView.total, name ='total-report-types'),  
  path('report-types/update/<int:id>/', views.ReportTypeView.update, name ='update-report-type'),  
  path('report-types/delete/<int:id>/', views.ReportTypeView.delete, name='delete-employee-type'),
  
  # employee type view 
  path('employee-types/new/', views.EmployeeTypeView.post, name='create-employee-type'),  
  path('employee-types/', views.EmployeeTypeView.list, name='employee-types'),  
  path('employee-types/get/<int:id>/', views.EmployeeTypeView.get, name ='retrieve-employee-type'),  
  path('employee-types/search=<str:search>/', views.EmployeeTypeView.list, name ='employee-types-by-search-term'),  
  path('employee-types/entry=<int:entry>/', views.EmployeeTypeView.list, name ='total-employee-types'),  
  path('employee-types/total/', views.EmployeeTypeView.total, name ='total-employee-types'),  
  path('employee-types/update/<int:id>/', views.EmployeeTypeView.update, name ='update-employee-type'),  
  path('employee-types/delete/<int:id>/', views.EmployeeTypeView.delete, name='delete-employee-type'),
  
  # inventory transfer status view 
  path('inventory-transfer-statuses/new/', views.InventoryTransferStatusView.post, name='create-inventory-transfer-status'),  
  path('inventory-transfer-statuses/', views.InventoryTransferStatusView.list, name='inventory-transfer-statuses'),  
  path('inventory-transfer-statuses/get/<int:id>/', views.InventoryTransferStatusView.get, name ='retrieve-inventory-transfer-status'),  
  path('inventory-transfer-statuses/search=<str:search>/', views.InventoryTransferStatusView.list, name ='inventory-transfer-statuses-by-search-term'),  
  path('inventory-transfer-statuses/entry=<int:entry>/', views.InventoryTransferStatusView.list, name ='total-inventory-transfer-statuses'),  
  path('inventory-transfer-statuses/total/', views.InventoryTransferStatusView.total, name ='total-inventory-transfer-statuses'),  
  path('inventory-transfer-statuses/update/<int:id>/', views.InventoryTransferStatusView.update, name ='update-inventory-transfer-status'), 
  
  # inventory transfer method view 
  path('inventory-transfer-methods/new/', views.InventoryTransferMethodView.post, name='create-inventory-transfer-method'),  
  path('inventory-transfer-methods/', views.InventoryTransferMethodView.list, name='inventory-transfer-methods'),  
  path('inventory-transfer-methods/get/<int:id>/', views.InventoryTransferMethodView.get, name ='retrieve-inventory-transfer-method'),  
  path('inventory-transfer-methods/search=<str:search>/', views.InventoryTransferMethodView.list, name ='inventory-transfer-methods-by-search-term'),  
  path('inventory-transfer-methods/entry=<int:entry>/', views.InventoryTransferMethodView.list, name ='total-inventory-transfer-methods'),  
  path('inventory-transfer-methods/total/', views.InventoryTransferMethodView.total, name ='total-inventory-transfer-methods'),  
  path('inventory-transfer-methods/update/<int:id>/', views.InventoryTransferMethodView.update, name ='update-inventory-transfer-method'),
  
  # employee status view 
  path('employee-statuses/new/', views.EmployeeStatusView.post, name='create-employee-status'),  
  path('employee-statuses/', views.EmployeeStatusView.list, name='employee-statuses'),  
  path('employee-statuses/get/<int:id>/', views.EmployeeStatusView.get, name ='retrieve-employee-status'),  
  path('employee-statuses/search=<str:search>/', views.EmployeeStatusView.list, name ='employee-statuses-by-search-term'),  
  path('employee-statuses/entry=<int:entry>/', views.EmployeeStatusView.list, name ='total-employee-statuses'),  
  path('employee-statuses/total/', views.EmployeeStatusView.total, name ='total-employee-statuses'),  
  path('employee-statuses/update/<int:id>/', views.EmployeeStatusView.update, name ='update-employee-status'), 
  
  # employee status history view 
  path('employee-status-histories/new/', views.EmployeeStatusHistoryView.post, name='create-employee-status-history'),  
  path('employee-status-histories/', views.EmployeeStatusHistoryView.list, name='employee-status-histories'),  
  path('employee-status-histories/get/<int:id>/', views.EmployeeStatusHistoryView.get, name ='retrieve-employee-status-history'),  
  path('employee-status-histories/search=<str:search>/', views.EmployeeStatusHistoryView.list, name ='employee-status-histories-by-search-term'),  
  path('employee-status-histories/entry=<int:entry>/', views.EmployeeStatusHistoryView.list, name ='total-employee-status-histories'),  
  path('employee-status-histories/total/', views.EmployeeStatusHistoryView.total, name ='total-employee-status-histories'),  
  path('employee-status-histories/update/<int:id>/', views.EmployeeStatusHistoryView.update, name ='update-employee-status-history'),   
  path('employee-status-histories/<int:employee>/', views.EmployeeStatusHistoryView.employee_status_history_list, name='employee-status-histories'),  
  
  # employee view
  path('employees/new/', views.EmployeeView.post, name='create-employee'),
  path('employees/names/', views.EmployeeView.employee_names, name='create-employee'),
  path('employees/by-year/<int:start_year>/<int:end_year>/', views.EmployeeView.employees_by_year, name='create-employee'),
  path('employees/generate-no/', views.EmployeeView.generated_employee_no, name='generate-employee-no'),
  path('employees/employee-numbers/', views.EmployeeView.employee_numbers, name='employee-numbers'),
  path('employees/total/', views.EmployeeView.total, name='total-employees'),
  path('employees/total/column=<str:column>/', views.EmployeeView.total, name='count-employees-by-search-term'),
  path('employees/search=<str:search>/', views.EmployeeView.list, name='employees-by-search-term'),
  path('employees/order=<str:order>/', views.EmployeeView.list, name='employees-by-order'),
  path('employees/entry=<int:entry>/', views.EmployeeView.list, name='employees-by-entry'),
  path('employees/<int:employee>/', views.EmployeeView.get, name='retrieve-employee'),
  path('employees/<int:employee>/work-info/', views.EmployeeView.work_info, name='retrieve-employee-work-info'),
  path('employees/<int:employee>/contact-info/', views.EmployeeView.contact_info, name='retrieve-employee-contact-info'),
  path('employees/get-employee-no/<int:id>/', views.EmployeeView.get_employee_no, name='get-employee-no'),
  path('employees/get-department-id/<int:id>/', views.EmployeeView.get_department_id, name='get-department-id'),
  path('employees/get-position-id/<int:id>/', views.EmployeeView.get_position_id, name='get-position-id'),
  path('employees/get-employee-status/<int:id>/', views.EmployeeView.get_employee_status, name='get-employee-status'),
  path('employees/validate/', views.EmployeeView.validate, name='validate'),
  path('employees/validate-employee-no/<str:employee_no>/', views.EmployeeView.validate_employee_no, name='validate-employee-no'),
  path('employees/validate-email/<int:employee>/<str:email>/', views.EmployeeView.validate_email, name='validate-email'),
  path('employees/update/<int:id>/', views.EmployeeView.update, name='update-enployee'),
  path('employees/clear/', views.EmployeeView.clear, name='clear-employees'),
  path('employees/generate-report/<str:column>/<str:value>/<str:start_date>/<str:end_date>/', views.EmployeeView.generate_report, name='generate-employee-report'),
  path('employees/on-leave/', views.EmployeeView.on_leave, name='on-leave'),
  
  # employee list
  path('employees/order=<str:order>/', views.EmployeeView.list, name='employees'),
  path('employees/', views.EmployeeView.list, name='employees'),
  
  # by department, type, status, , date hired range and sex
  path('employees/department=<int:department>/employee_type=<int:employee_type>/employee_status=<int:employee_status>/sex=<int:sex>/date_hired_range=<str:date_hired_range>/order=<str:order>/', views.EmployeeView.list, name='employees-by-department'),
  path('employees/department=<int:department>/employee_type=<int:employee_type>/employee_status=<int:employee_status>/sex=<int:sex>/date_hired_range=<str:date_hired_range>/', views.EmployeeView.list, name='employees-by-department'),
  
  # by department, type, status and sex
  path('employees/department=<int:department>/employee_type=<int:employee_type>/employee_status=<int:employee_status>/sex=<int:sex>/order=<str:order>/', views.EmployeeView.list, name='employees-by-department'),
  path('employees/department=<int:department>/employee_type=<int:employee_type>/employee_status=<int:employee_status>/sex=<int:sex>/', views.EmployeeView.list, name='employees-by-department'),
  
  # by department, type and status
  path('employees/department=<int:department>/employee_type=<int:employee_type>/employee_status=<int:employee_status>/order=<str:order>/', views.EmployeeView.list, name='employees-by-department'),
  path('employees/department=<int:department>/employee_type=<int:employee_type>/employee_status=<int:employee_status>/', views.EmployeeView.list, name='employees-by-department'),
  
  # by department and type
  path('employees/department=<int:department>/employee_type=<int:employee_type>/order=<str:order>/', views.EmployeeView.list, name='employees-by-department'),
  path('employees/department=<int:department>/employee_type=<int:employee_type>/', views.EmployeeView.list, name='employees-by-department'),
  
  # by department, status and sex
  path('employees/department=<int:department>/employee_status=<int:employee_status>/sex=<int:sex>/order=<str:order>/', views.EmployeeView.list, name='employees-by-department'),
  path('employees/department=<int:department>/employee_status=<int:employee_status>/sex=<int:sex>/', views.EmployeeView.list, name='employees-by-department'),
  
  # by department and status
  path('employees/department=<int:department>/employee_status=<int:employee_status>/order=<str:order>/', views.EmployeeView.list, name='employees-by-department'),
  path('employees/department=<int:department>/employee_status=<int:employee_status>/', views.EmployeeView.list, name='employees-by-department'),
  
  # by department and sex
  path('employees/department=<int:department>/sex=<int:sex>/order=<str:order>/', views.EmployeeView.list, name='employees-by-department'),
  path('employees/department=<int:department>/sex=<int:sex>/', views.EmployeeView.list, name='employees-by-department'),
  
  # by department and date hired
  path('employees/department=<int:department>/date_hired_range=<str:date_hired_range>/order=<str:order>/', views.EmployeeView.list, name='employees-by-department'),
  path('employees/department=<int:department>/date_hired_range=<str:date_hired_range>/', views.EmployeeView.list, name='employees-by-department'),
  
  # by department
  path('employees/department=<int:department>/order=<str:order>/', views.EmployeeView.list, name='employees-by-department'),
  path('employees/department=<int:department>/', views.EmployeeView.list, name='employees-by-department'),
  
  # by type and status
  path('employees/employee_type=<int:employee_type>/employee_status=<int:employee_status>/order=<str:order>/', views.EmployeeView.list, name='employees-by-sex'),
  path('employees/employee_type=<int:employee_type>/employee_status=<int:employee_status>/', views.EmployeeView.list, name='employees-by-sex'),
  
  # by type and sex
  path('employees/employee_type=<int:employee_type>/sex=<int:sex>/order=<str:order>/', views.EmployeeView.list, name='employees-by-sex'),
  path('employees/employee_type=<int:employee_type>/sex=<int:sex>/', views.EmployeeView.list, name='employees-by-sex'),
  
  # by type
  path('employees/employee_type=<int:employee_type>/order=<str:order>/', views.EmployeeView.list, name='employees-by-sex'),
  path('employees/employee_type=<int:employee_type>/', views.EmployeeView.list, name='employees-by-sex'),
  
  # by status and sex
  path('employees/employee_status=<int:employee_status>/sex=<str:sex>/order=<str:order>/', views.EmployeeView.list, name='employees-by-sex'),
  path('employees/employee_status=<int:employee_status>/sex=<int:sex>/', views.EmployeeView.list, name='employees-by-sex'),
  
  # by status
  path('employees/employee_status=<int:employee_status>/order=<str:order>/', views.EmployeeView.list, name='employees-by-sex'),
  path('employees/employee_status=<int:employee_status>/', views.EmployeeView.list, name='employees-by-sex'),
  
  # birthdate
  path('employees/birthdate=<str:birthdate>/order=<str:order>/', views.EmployeeView.list, name='employees-by-birthdate'),
  path('employees/birthdate=<str:birthdate>/', views.EmployeeView.list, name='employees-by-department'),
  
  # by birthplace
  path('employees/birthplace=<int:birthplace>/order=<str:order>/', views.EmployeeView.list, name='employees-by-birthplace'),
  path('employees/birthplace=<int:birthplace>/', views.EmployeeView.list, name='employees-by-department'),
  
  # by sex
  path('employees/sex=<int:sex>/order=<str:order>/', views.EmployeeView.list, name='employees-by-sex'),
  path('employees/sex=<int:sex>/', views.EmployeeView.list, name='employees-by-sex'),
  
  # by height
  path('employees/height=<int:height>/', views.EmployeeView.list, name='employees-by-sex'),
  path('employees/height_range=<str:height_range>/', views.EmployeeView.list, name='employees-by-sex'),
  
  # by weight
  path('employees/weight=<int:weight>/', views.EmployeeView.list, name='employees-by-sex'),
  path('employees/weight_range=<str:weight_range>/', views.EmployeeView.list, name='employees-by-sex'),
  
  # by date hired
  path('employees/date_hired_range=<str:date_hired_range>/', views.EmployeeView.list, name='employees-by-sex'),
  
  # equipment request view
  path('equipment-requests/new/', views.EquipmentRequestView.post, name='create-equipment-request'),  
  path('equipment-requests/', views.EquipmentRequestView.list, name='equipment-requests'),  
  path('equipment-requests/search=<str:search>/', views.EquipmentRequestView.list, name ='equipment-requests-by-search-term'),  
  path('equipment-requests/entry=<int:entry>/', views.EquipmentRequestView.list, name ='total-equipment-request'),  
  
  # path('equipment-requests/total/', views.EquipmentRequestView.total, name ='total-equipment-request'),  
  path('equipment-requests/get/<int:id>/', views.EquipmentRequestView.get, name ='update-equipment-request'),
  
  # equipment type view
  path('equipment-types/new/', views.EquipmentTypeView.post, name='create-equipment-type'),  
  path('equipment-types/', views.EquipmentTypeView.list, name='equipment-types'),  
  path('equipment-types/search=<str:search>/', views.EquipmentTypeView.list, name ='equipment-types-by-search-term'),  
  path('equipment-types/entry=<int:entry>/', views.EquipmentTypeView.list, name ='total-equipment-type'),  
  path('equipment-types/total/', views.EquipmentTypeView.total, name ='total-equipment-type'),  
  path('equipment-types/get/<int:id>/', views.EquipmentTypeView.get , name ='retrieve-equipment-type'),  
  path('equipment-types/update/<int:id>/', views.EquipmentTypeView.update, name ='update-equipment-type'),  
  path('equipment-types/delete/<int:id>/', views.EquipmentTypeView.delete, name='delete-equipment-type'),
  
  # equipment article view
  path('equipment-articles/new/', views.EquipmentArticleView.post, name='create-equipment-article'),  
  path('equipment-articles/', views.EquipmentArticleView.list, name='equipment-articles'),  
  path('equipment-articles/search=<str:search>/', views.EquipmentArticleView.list, name ='equipment-articles-by-search-term'),  
  path('equipment-articles/entry=<int:entry>/', views.EquipmentArticleView.list, name ='total-equipment-article'),  
  path('equipment-articles/total/', views.EquipmentArticleView.total, name ='total-equipment-article'),  
  path('equipment-articles/get/<int:id>/', views.EquipmentArticleView.get, name ='retrieve-equipment-article'),  
  path('equipment-articles/update/<int:id>/', views.EquipmentArticleView.update, name ='update-equipment-article'),  
  path('equipment-articles/delete/<int:id>/', views.EquipmentArticleView.delete, name='delete-equipment-article'),
  
  # equipment view
  path('equipments/new/', views.EquipmentView.post, name='create-equipment'),
  path('equipments/total/', views.EquipmentView.total, name='total-equipments'),
  path('equipments/', views.EquipmentView.list, name='equipments'),
  path('equipments/property-number/', views.EquipmentView.property_number, name='property-number'),
  path('equipments/search=<str:search>/', views.EquipmentView.list, name='equipments-by-search-term'),
  path('equipments/order=<str:order>/', views.EquipmentView.list, name='equipments-by-order'),
  path('equipments/entry=<int:entry>/', views.EquipmentView.list, name='equipments-by-entry'),
  path('equipments/update/<int:id>/', views.EquipmentView.update, name='update-equipment'),
  
  # government company view 
  path('government-companies/new/', views.GovernmentCompanyView.post, name='create-government-company'),  
  path('government-companies/', views.GovernmentCompanyView.list, name='government-companies'),  
  path('government-companies/get/<int:id>/', views.GovernmentCompanyView.get, name ='retrieve-government-company'),  
  path('government-companies/search=<str:search>/', views.GovernmentCompanyView.list, name ='government-companies-by-search-term'),  
  path('government-companies/entry=<int:entry>/', views.GovernmentCompanyView.list, name ='total-government-companies'),  
  path('government-companies/total/', views.GovernmentCompanyView.total, name ='total-government-companies'),  
  path('government-companies/update/<int:id>/', views.GovernmentCompanyView.update, name ='update-government-company'),  
  path('government-companies/delete/<int:id>/', views.GovernmentCompanyView.delete, name='delete-government-company'),
  
  # government issued id view 
  path('government-issued-ids/new/', views.GovernmentIssuedIDView.post, name='create-government-issued id'),  
  path('government-issued-ids/', views.GovernmentIssuedIDView.list, name='government-issued-ids'),  
  path('government-issued-ids/get/<int:id>/', views.GovernmentIssuedIDView.get, name ='retrieve-government-issued id'),  
  path('government-issued-ids/search=<str:search>/', views.GovernmentIssuedIDView.list, name ='government-issued-ids-by-search-term'),  
  path('government-issued-ids/entry=<int:entry>/', views.GovernmentIssuedIDView.list, name ='total-government-issued-ids'),  
  path('government-issued-ids/total/', views.GovernmentIssuedIDView.total, name ='total-government-issued-ids'),  
  path('government-issued-ids/update/<int:id>/', views.GovernmentIssuedIDView.update, name ='update-government-issued id'),  
  path('government-issued-ids/delete/<int:id>/', views.GovernmentIssuedIDView.delete, name='delete-government-issued id'),
  
  # group view 
  path('groups/new/', views.GroupView.post, name='create-group'),  
  path('groups/', views.GroupView.list, name='groups'),  
  path('groups/search=<str:search>/', views.GroupView.list, name ='group-by-search-term'),  
  path('groups/entry=<int:entry>/', views.GroupView.list, name ='total-groups'),  
  path('groups/total/', views.GroupView.total, name ='total-groups'),  
  path('groups/get/<int:id>/', views.GroupView.get, name ='retrieve-group'),  
  path('groups/update/<int:id>/', views.GroupView.update, name ='update-group'),  
  path('groups/delete/<int:id>/', views.GroupView.delete, name ='delete-group'),  
  
  # group permissions view
  path('group-permissions/new/', views.GroupPermissionsView.post, name='create-group-permission'),
  path('group-permissions/total/', views.GroupPermissionsView.total, name='total-group-permissions'),
  path('group-permissions/', views.GroupPermissionsView.list, name='group-permissions'),
  path('group-permissions/<int:user>/', views.GroupPermissionsView.list, name='group-permissions-by-user'),
  path('group-permissions/search=<str:search>/', views.GroupPermissionsView.list, name='group-permissions-by-searh-term'),
  path('group-permissions/entry=<int:entry>/', views.GroupPermissionsView.list, name='group-permissions-by-entry'),
  path('group-permissions/order=<str:order>/', views.GroupPermissionsView.list, name='group-permissions-by-order'),
  path('group-permissions/get/<int:id>/', views.GroupPermissionsView.get, name='get-group-permissions'),
  path('group-permissions/get/username=<str:username>/', views.GroupPermissionsView.get, name='get-group-permissions'),
  path('group-permissions/update/<int:id>/', views.GroupPermissionsView.update, name='update-group-permissions'),
  path('group-permissions/delete/<int:id>/', views.GroupPermissionsView.delete, name='delete-group-permissions'),
  
  # job history view  
  path('job-histories/new/', views.JobHistoryView.post, name='create-job-history'),
  path('job-histories/', views.JobHistoryView.list, name='job-history'),
  path('job-histories/total/', views.JobHistoryView.total, name='total-job-history'),
  path('job-histories/employees/supervisor=<int:supervisor>/', views.JobHistoryView.employees_by_supervisor, name='job-history'),
  path('job-histories/municipal-officials/', views.JobHistoryView.municipal_officials, name='municipal-officials'),
  path('job-histories/get/<int:id>/', views.JobHistoryView.get, name='retrieve-job-history'),
  path('job-histories/get/employee_no=<str:employee_no>/', views.JobHistoryView.get, name='retrieve-job-history'),
  path('job-histories/retrieve-job-title/<int:employee>/', views.JobHistoryView.retrieve_position_title, name='retrieve-job-title'),
  path('job-histories/employees/<str:username>/', views.JobHistoryView.employees_by_office, name='employees-by-office'),
  path('job-histories/get-employee-id/<int:job_id>/', views.JobHistoryView.employee_id, name='retrieve-employee-id'),
  path('job-histories/update/<int:id>/', views.JobHistoryView.update, name='update-job-history-by-id'),
  
  # leave balance view
  path('leave-balances/new/', views.LeaveBalanceView.post, name='create-leave-balance'),  
  path('leave-balances/', views.LeaveBalanceView.list, name='leave-balances'),  
  path('leave-balances/search=<str:search>/', views.LeaveBalanceView.list, name ='leave-balance-by-search-term'),  
  path('leave-balances/entry=<int:entry>/', views.LeaveBalanceView.list, name ='total-leave-balances'),  
  path('leave-balances/total/', views.LeaveBalanceView.total, name ='total-leave-balances'),  
  path('leave-balances/get/<int:id>/', views.LeaveBalanceView.get, name ='retrieve-leave-balance'),  
  path('leave-balances/get/employee=<int:employee>/leave_type=<int:leave_type>/', views.LeaveBalanceView.available_leave, name ='retrieve-leave-balance'),  
  path('leave-balances/update/<int:id>/', views.LeaveBalanceView.update, name ='update-leave-balance'),  
  path('leave-balances/delete/<int:id>/', views.LeaveBalanceView.delete, name ='delete-leave-balance'),
  
  # leave type view
  path('leave-types/new/', views.LeaveTypeView.post, name='create-leave-type'),
  path('leave-types/verify/<str:name>/', views.LeaveTypeView.verify, name='verify-leave-type'),
  path('leave-types/', views.LeaveTypeView.list, name='leave-types'),
  path('leave-types/sex=<int:sex>/', views.LeaveTypeView.list, name='leave-types'),
  path('leave-types/total/', views.LeaveTypeView.total, name='total-leave-types'),
  path('leave-types/get/<int:id>/', views.LeaveTypeView.get, name='update-leave-type'),
  path('leave-types/update/<int:id>/', views.LeaveTypeView.update, name='update-leave-type'),
  
  # leave detail option view
  path('leave-detail-options/new/', views.LeaveDetailOptionView.post, name='create-leave-detail-option'),
  path('leave-detail-options/verify/<str:name>/', views.LeaveDetailOptionView.verify, name='verify-leave-detail-option'),
  path('leave-detail-options/', views.LeaveDetailOptionView.list, name='leave-detail-options'),
  path('leave-detail-options/total/', views.LeaveDetailOptionView.total, name='total-leave-detail-options'),
  path('leave-detail-options/get/<int:id>/', views.LeaveDetailOptionView.get, name='update-leave-detail-option'),
  path('leave-detail-options/update/<int:id>/', views.LeaveDetailOptionView.update, name='update-leave-detail-option'),
  
  # employee leave view
  path('employee-leaves/new/', views.EmployeeLeaveView.post, name='create-employee-leaves'),
  path('employee-leaves/get/<int:id>/', views.EmployeeLeaveView.get, name='retrieve-employee-leave'),
  path('employee-leaves/approve/<int:id>/', views.EmployeeLeaveView.approve, name='approve-employee-leave'),
  path('employee-leaves/decline/<int:id>/', views.EmployeeLeaveView.decline, name='decline-employee-leave'),
  path('employee-leaves/delete/<int:id>/', views.EmployeeLeaveView.delete, name='delete-employee-leave'),
  path('employee-leaves/update/<int:id>/', views.EmployeeLeaveView.update, name='update-employee-leave'),
  path('employee-leaves/days-on-leave/<int:employee>/', views.EmployeeLeaveView.days_on_leave, name='days-on-leave'),
  
  # by department and employee  
  path('employee-leaves/department=<int:department>/employee=<int:employee>/status=<int:status>/application_date_range=<str:application_date_range>/order=<str:order>/', views.EmployeeLeaveView.list, name='employee-leaves'),
  path('employee-leaves/department=<int:department>/employee=<int:employee>/status=<int:status>/application_date_range=<str:application_date_range>/', views.EmployeeLeaveView.list, name='employee-leaves'),
  path('employee-leaves/department=<int:department>/employee=<int:employee>/application_date_range=<str:application_date_range>/order=<str:order>/', views.EmployeeLeaveView.list, name='employee-leaves'),
  path('employee-leaves/department=<int:department>/employee=<int:employee>/application_date_range=<str:application_date_range>/', views.EmployeeLeaveView.list, name='employee-leaves'),
  path('employee-leaves/department=<int:department>/employee=<int:employee>/status=<int:status>/order=<str:order>/', views.EmployeeLeaveView.list, name='retrieve-department-employee-leave'),
  path('employee-leaves/department=<int:department>/employee=<int:employee>/status=<int:status>/', views.EmployeeLeaveView.list, name='retrieve-department-employee-leave'),
  path('employee-leaves/department=<int:department>/employee=<int:employee>/order=<str:order>/', views.EmployeeLeaveView.list, name='retrieve-department-employee-leave'),
  path('employee-leaves/department=<int:department>/employee=<int:employee>/', views.EmployeeLeaveView.list, name='retrieve-department-employee-leave'),
  
  # by department
  path('employee-leaves/department=<int:department>/status=<int:status>/application_date_range=<str:application_date_range>/order=<str:order>/', views.EmployeeLeaveView.list, name='employee-leaves'),
  path('employee-leaves/department=<int:department>/status=<int:status>/application_date_range=<str:application_date_range>/', views.EmployeeLeaveView.list, name='employee-leaves'),
  path('employee-leaves/department=<int:department>/application_date_range=<str:application_date_range>/order=<str:order>/', views.EmployeeLeaveView.list, name='retrieve-department-employee-leave'),
  path('employee-leaves/department=<int:department>/application_date_range=<str:application_date_range>/', views.EmployeeLeaveView.list, name='retrieve-department-employee-leave'),
  path('employee-leaves/department=<int:department>/status=<int:status>/order=<str:order>/', views.EmployeeLeaveView.list, name='retrieve-department-employee-leave'),
  path('employee-leaves/department=<int:department>/status=<int:status>/', views.EmployeeLeaveView.list, name='retrieve-department-employee-leave'),
  path('employee-leaves/department=<int:department>/order=<str:order>/', views.EmployeeLeaveView.list, name='retrieve-department-employee-leave'),
  path('employee-leaves/department=<int:department>/', views.EmployeeLeaveView.list, name='retrieve-department-employee-leave'),
  
  # leaves by department head and employee
  path('employee-leaves/department_head=<int:department_head>/employee=<int:employee>/status=<int:status>/application_date_range=<str:application_date_range>/order=<str:order>/', views.EmployeeLeaveView.list, name='retrieve-department_head-employee-leave'),
  path('employee-leaves/department_head=<int:department_head>/employee=<int:employee>/status=<int:status>/application_date_range=<str:application_date_range>/', views.EmployeeLeaveView.list, name='retrieve-department_head-employee-leave'),
  path('employee-leaves/department_head=<int:department_head>/employee=<int:employee>/application_date_range=<str:application_date_range>/order=<str:order>/', views.EmployeeLeaveView.list, name='retrieve-department_head-employee-leave'),
  path('employee-leaves/department_head=<int:department_head>/employee=<int:employee>/application_date_range=<str:application_date_range>/', views.EmployeeLeaveView.list, name='retrieve-department_head-employee-leave'),
  path('employee-leaves/department_head=<int:department_head>/employee=<int:employee>/status=<int:status>/order=<str:order>/', views.EmployeeLeaveView.list, name='retrieve-department_head-employee-leave'),
  path('employee-leaves/department_head=<int:department_head>/employee=<int:employee>/status=<int:status>/', views.EmployeeLeaveView.list, name='retrieve-department_head-employee-leave'),
  path('employee-leaves/department_head=<int:department_head>/employee=<int:employee>/order=<str:order>/', views.EmployeeLeaveView.list, name='retrieve-department_head-employee-leave'),
  path('employee-leaves/department_head=<int:department_head>/employee=<int:employee>/', views.EmployeeLeaveView.list, name='retrieve-department_head-employee-leave'),
  
  # leaves by department head
  path('employee-leaves/department_head=<int:department_head>/status=<int:status>/application_date_range=<str:application_date_range>/order=<str:order>/', views.EmployeeLeaveView.list, name='employee-leaves'),
  path('employee-leaves/department_head=<int:department_head>/status=<int:status>/application_date_range=<str:application_date_range>/', views.EmployeeLeaveView.list, name='employee-leaves'),
  path('employee-leaves/department_head=<int:department_head>/application_date_range=<str:application_date_range>/order=<str:order>/', views.EmployeeLeaveView.list, name='retrieve-department_head-employee-leave'),
  path('employee-leaves/department_head=<int:department_head>/application_date_range=<str:application_date_range>/', views.EmployeeLeaveView.list, name='retrieve-department_head-employee-leave'),
  path('employee-leaves/department_head=<int:department_head>/status=<int:status>/order=<str:order>/', views.EmployeeLeaveView.list, name='retrieve-department_head-employee-leave'),
  path('employee-leaves/department_head=<int:department_head>/status=<int:status>/', views.EmployeeLeaveView.list, name='retrieve-department_head-employee-leave'),
  path('employee-leaves/department_head=<int:department_head>/order=<str:order>/', views.EmployeeLeaveView.list, name='retrieve-department-employee-leave'),
  path('employee-leaves/department_head=<int:department_head>/', views.EmployeeLeaveView.list, name='retrieve-department-employee-leave'),
  
  # leaves by employee
  path('employee-leaves/employee=<int:employee>/status=<int:status>/application_date_range=<str:application_date_range>/order=<str:order>/', views.EmployeeLeaveView.list, name='employee-leaves'),
  path('employee-leaves/employee=<int:employee>/status=<int:status>/application_date_range=<str:application_date_range>/', views.EmployeeLeaveView.list, name='employee-leaves'),
  path('employee-leaves/employee=<int:employee>/application_date_range=<str:application_date_range>/order=<str:order>/', views.EmployeeLeaveView.list, name='employee-leaves'),
  path('employee-leaves/employee=<int:employee>/application_date_range=<str:application_date_range>/', views.EmployeeLeaveView.list, name='employee-leaves'),
  path('employee-leaves/employee=<int:employee>/status=<int:status>/order=<str:order>/', views.EmployeeLeaveView.list, name='employee-leaves'),
  path('employee-leaves/employee=<int:employee>/status=<int:status>/', views.EmployeeLeaveView.list, name='employee-leaves'),
  path('employee-leaves/employee=<int:employee>/order=<str:order>/', views.EmployeeLeaveView.list, name='employee-leaves'),
  path('employee-leaves/employee=<int:employee>/', views.EmployeeLeaveView.list, name='employee-leaves'),
  
  # default
  path('employee-leaves/status=<int:status>/application_date_range=<str:application_date_range>/order=<str:order>/', views.EmployeeLeaveView.list, name='employee-leaves'),
  path('employee-leaves/status=<int:status>/application_date_range=<str:application_date_range>/', views.EmployeeLeaveView.list, name='employee-leaves'),
  path('employee-leaves/application_date_range=<str:application_date_range>/order=<str:order>/', views.EmployeeLeaveView.list, name='employee-leaves'),
  path('employee-leaves/application_date_range=<str:application_date_range>/', views.EmployeeLeaveView.list, name='employee-leaves'),
  path('employee-leaves/status=<int:status>/order=<str:order>/', views.EmployeeLeaveView.list, name='employee-leaves'),
  path('employee-leaves/status=<int:status>/', views.EmployeeLeaveView.list, name='employee-leaves'),
  path('employee-leaves/order=<str:order>/', views.EmployeeLeaveView.list, name='employee-leaves'),
  path('employee-leaves/', views.EmployeeLeaveView.list, name='employee-leaves'),
  
  # location view 
  path('locations/new/', views.LocationView.post, name='create-location'),  
  path('locations/', views.LocationView.list, name='locations'),  
  path('locations/search=<str:search>/', views.LocationView.list, name ='location-by-search-term'),  
  path('locations/entry=<int:entry>/', views.LocationView.list, name ='total-locations'),  
  path('locations/total/', views.LocationView.total, name ='total-locations'),  
  path('locations/get/<int:id>/', views.LocationView.get, name ='retrieve-location'),  
  path('locations/update/<int:id>/', views.LocationView.update, name ='update-location'),  
  path('locations/delete/<int:id>/', views.LocationView.delete, name ='delete-location'),
  
  # login history view  
  path('login-histories/new/', views.LoginHistoryView.post, name='create-login-history'),
  path('login-histories/total/', views.LoginHistoryView.total, name='total-login-histories'),
  path('login-histories/total/<str:username>/', views.LoginHistoryView.total, name='total-login-histories-by-user'),
  path('login-histories/', views.LoginHistoryView.list, name='Login history list'),
  path('login-histories/search=<str:search>/', views.LoginHistoryView.list, name='login-histories-by-search'),    
  path('login-histories/entry=<int:entry>/', views.LoginHistoryView.list, name='login-histories-by-entry'),    
  path('login-histories/order=<str:order>/', views.LoginHistoryView.list, name='login-histories-by-order'), 
  path('login-histories/update/<int:login_id>/', views.LoginHistoryView.update, name='update-login-history'),
  path('login-histories/clear/', views.LoginHistoryView.clear, name='clear-login-history'),
  
  # measurement unit view 
  path('measurement-units/new/', views.MeasurementUnitView.post, name='create-measurement-unit'),  
  path('measurement-units/', views.MeasurementUnitView.list, name='measurement-units'),  
  path('measurement-units/get/<int:id>/', views.MeasurementUnitView.get, name ='retrieve-measurement-unit'),  
  path('measurement-units/search=<str:search>/', views.MeasurementUnitView.list, name ='measurement-units-by-search-term'),  
  path('measurement-units/entry=<int:entry>/', views.MeasurementUnitView.list, name ='total-measurement-units'),  
  path('measurement-units/total/', views.MeasurementUnitView.total, name ='total-measurement-units'),  
  path('measurement-units/update/<int:id>/', views.MeasurementUnitView.update, name ='update-measurement-unit'),  
  path('measurement-units/delete/<int:id>/', views.MeasurementUnitView.delete, name='delete-measurement-unit'),
  
  # mother view
  path('mothers/new/', views.MotherView.post, name='create-mother'),
  path('mothers/get/<int:employee>/', views.MotherView.get, name='retrieve-mother'),
  path('mothers/update/<int:id>/', views.MotherView.update, name='update-mother'),
  
  # mail view
  path('send-mail/', views.MailView.send_mail, name='send-mail'),
  
  # name extension view 
  path('name-extensions/new/', views.NameExtensionView.post, name='create-name-extension'),  
  path('name-extensions/', views.NameExtensionView.list, name='name-extensions'),  
  path('name-extensions/get/<int:id>/', views.NameExtensionView.get, name ='retrieve-name-extension'),  
  path('name-extensions/order=<str:order>/', views.NameExtensionView.list, name ='name-extensions-by-order'),  
  path('name-extensions/search=<str:search>/', views.NameExtensionView.list, name ='name-extensions-by-search-term'),  
  path('name-extensions/entry=<int:entry>/', views.NameExtensionView.list, name ='total-name-extensions'),  
  path('name-extensions/total/', views.NameExtensionView.total, name ='total-name-extensions'),  
  path('name-extensions/update/<int:id>/', views.NameExtensionView.update, name ='update-name-extension'),  
  path('name-extensions/delete/<int:id>/', views.NameExtensionView.delete, name='delete-name-extension'),
  
  # notifcation view
  path('notifications/new/', views.NotificationView.post, name='create-notification'),
  path('notifications/user=<int:user>/', views.NotificationView.list, name='list-of-notifications'),
  path('notifications/update/<int:id>/', views.NotificationView.update, name='update-notification'),
  path('notifications/delete/<int:id>/', views.NotificationView.delete, name='delete-notification'),
  path('notifications/clear/', views.NotificationView.clear, name='clear-notifications'),
  
  # department view
  path('departments/new/', views.DepartmentView.post, name='create-department'),
  path('departments/', views.DepartmentView.list, name='departments'),
  path('departments/total/', views.DepartmentView.total, name='departments'),
  path('departments/search=<str:search>/', views.DepartmentView.list, name='departments-by-search-term'),
  path('departments/order=<str:order>/', views.DepartmentView.list, name='departments-by-order'),
  path('departments/entry=<str:entry>/', views.DepartmentView.list, name='departments-by-entry'),
  path('departments/get/<int:id>/', views.DepartmentView.get, name='retrieve-department'),
  path('departments/get-department-head/<int:id>/', views.DepartmentView.get_department_head, name='retrieve-department'),
  path('departments/update/<int:id>/', views.DepartmentView.update, name='update-department'),
  path('departments/delete/<int:id>/', views.DepartmentView.delete, name='delete-department'),
  
  # department file view
  path('department-files/new/', views.DepartmentFileView.post, name='upload-department-file'),
  path('department-files/', views.DepartmentFileView.list, name='department-files'),
  path('department-files/total/', views.DepartmentFileView.total, name='total-department-files'),
  path('department-files/total/<int:office>/', views.DepartmentFileView.total, name='total-department-files-by-office'),
  path('department-files/get/<int:office>/', views.DepartmentFileView.get, name='retrieve-department-files'),
  path('department-files/get/<int:office>/entry=<str:entry>/', views.DepartmentFileView.get, name='retrieve-department-files-by-entry'),
  path('department-files/get/<int:office>/order=<str:order>/', views.DepartmentFileView.get, name='retrieve-department-files-by-order'),
  path('department-files/get/<int:office>/search_term=<str:search_term>/', views.DepartmentFileView.get, name='retrieve-department-files-by-search-term'),
  path('department-files/delete/<int:id>/', views.DepartmentFileView.delete, name='delete-department-file'),
  
  # office supply request view
  path('office-supply-requests/new/', views.OfficeSupplyRequestView.post, name='create-office-supply-request'),  
  path('office-supply-requests/', views.OfficeSupplyRequestView.list, name='office-supply-requests'),  
  path('office-supply-requests/<int:employee>/', views.OfficeSupplyRequestView.list, name='office-supply-requests'),  
  path('office-supply-requests/search=<str:search>/', views.OfficeSupplyRequestView.list, name ='office-supply-requests-by-search-term'),  
  path('office-supply-requests/entry=<int:entry>/', views.OfficeSupplyRequestView.list, name ='total-office-supply-request'),  
  path('office-supply-requests/total/', views.OfficeSupplyRequestView.total, name ='total-office-supply-request'),  
  path('office-supply-requests/get/<int:id>/', views.OfficeSupplyRequestView.get, name ='retrieve-office-supply-request'),  
  path('office-supply-requests/update/<int:id>/', views.OfficeSupplyRequestView.update, name ='update-office-supply-request'),  
  path('office-supply-requests/approve/<int:id>/', views.OfficeSupplyRequestView.approve, name ='aprrove-office-supply-request'),  
  path('office-supply-requests/decline/<int:id>/', views.OfficeSupplyRequestView.decline, name ='decline-office-supply-request'),  
  path('office-supply-requests/delete/', views.OfficeSupplyRequestView.delete, name ='delete-office-supply-request'),  
  
  # office supply transfer view
  path('office-supply-transfers/new/', views.OfficeSupplyTransferView.post, name='create-office-supply-transfer'),  
  path('office-supply-transfers/', views.OfficeSupplyTransferView.list, name='office-supply-transfers'),  
  path('office-supply-transfers/search=<str:search>/', views.OfficeSupplyTransferView.list, name ='office-supply-transfers-by-search-term'),  
  path('office-supply-transfers/entry=<int:entry>/', views.OfficeSupplyTransferView.list, name ='total-office-supply-transfer'),  
  path('office-supply-transfers/total/', views.OfficeSupplyTransferView.total, name ='total-office-supply-transfer'),  
  path('office-supply-transfers/get/<int:id>/', views.OfficeSupplyTransferView.get, name ='update-office-supply-transfer'),  
  path('office-supply-transfers/update/<int:id>/', views.OfficeSupplyTransferView.update, name ='update-office-supply-transfer'),  
  path('office-supply-transfers/delete/<int:id>/', views.OfficeSupplyTransferView.delete, name='delete-office-supply-transfer'),
  path('office-supply-transfers/delete-all/', views.OfficeSupplyTransferView.delete_all, name='delete-office-supply-transfer'),
  
  # office supply type view
  path('office-supply-types/new/', views.OfficeSupplyTypeView.post, name='create-office-supply-type'),  
  path('office-supply-types/', views.OfficeSupplyTypeView.list, name='office-supply-types'),  
  path('office-supply-types/search=<str:search>/', views.OfficeSupplyTypeView.list, name ='office-supply-types-by-search-term'),  
  path('office-supply-types/entry=<int:entry>/', views.OfficeSupplyTypeView.list, name ='total-office-supply-type'),  
  path('office-supply-types/total/', views.OfficeSupplyTypeView.total, name ='total-office-supply-type'),  
  path('office-supply-types/get/<int:id>/', views.OfficeSupplyTypeView.get, name ='update-office-supply-type'),  
  path('office-supply-types/update/<int:id>/', views.OfficeSupplyTypeView.update, name ='update-office-supply-type'),  
  path('office-supply-types/delete/<int:id>/', views.OfficeSupplyTypeView.delete, name='delete-office-supply-type'),
  
  # office supply articles view
  path('office-supply-articles/new/', views.OfficeSupplyArticleView.post, name='create-office-supply-article'),  
  path('office-supply-articles/', views.OfficeSupplyArticleView.list, name='office-supply-articles'),  
  path('office-supply-articles/search=<str:search>/', views.OfficeSupplyArticleView.list, name ='office-supply-articles-by-search-term'),  
  path('office-supply-articles/entry=<int:entry>/', views.OfficeSupplyArticleView.list, name ='total-office-supply-article'),  
  path('office-supply-articles/total/', views.OfficeSupplyArticleView.total, name ='total-office-supply-article'),  
  path('office-supply-articles/get/<int:id>/', views.OfficeSupplyArticleView.get, name ='retrieve-office-supply-article'),  
  path('office-supply-articles/update/<int:id>/', views.OfficeSupplyArticleView.update, name ='update-office-supply-article'),  
  path('office-supply-articles/delete/<int:id>/', views.OfficeSupplyArticleView.delete, name='delete-office-supply-article'),
  
  # office supply view
  path('office-supplies/new/', views.OfficeSupplyView.post, name='create-office-supply'), 
  path('office-supplies/stock-number/', views.OfficeSupplyView.stock_number, name='stock_number'),
  path('office-supplies/total/', views.OfficeSupplyView.total, name='total-office-supplies'),
  path('office-supplies/total/<str:count>/', views.OfficeSupplyView.total, name='total-office-supplies'),
  path('office-supplies/', views.OfficeSupplyView.list, name='office-supplies'),
  path('office-supplies/get-quantity/<int:id>/', views.OfficeSupplyView.get_quantity, name='get-office-supply-quantity'),
  path('office-supplies/update/<int:id>/', views.OfficeSupplyView.update, name='update-office-supply'),
  path('office-supplies/clear/', views.OfficeSupplyView.clear, name='clear-office-supply'),
  
  # office supply stock view
  path('office-supply-stocks/new/', views.OfficeSupplyStockView.post, name='create-office-supply-stock'), 
  path('office-supply-stocks/', views.OfficeSupplyStockView.list, name='office-supply-stocks'), 
  path('office-supply-stocks/get/<int:id>/', views.OfficeSupplyStockView.get, name='retreive-office-supply-stock'), 
  path('office-supply-stocks/verify/<int:type>/<int:article>/<int:measurement_unit>/', views.OfficeSupplyStockView.verify, name='get-office-supply-quantity'),
  path('office-supply-stocks/update/<int:id>/', views.OfficeSupplyStockView.update, name='update-office-supply-stock'), 
  path('office-supply-stocks/update-quantity/<int:id>/', views.OfficeSupplyStockView.update_quantity, name='update-quantity'), 
  
  # permanent address view
  path('permanent-address/new/', views.PermanentAddressView.post, name='create-address'),
  path('permanent-address/<int:employee>/', views.PermanentAddressView.get, name='retrieve-address'),
  path('permanent-address/update/<int:employee>/', views.PermanentAddressView.update, name='update-address'),
  
  # permission view
  path('permissions/new/', views.PermissionView.post, name='create-permission'),
  path('permissions/total/', views.PermissionView.total, name='total-permissions'),
  path('permissions/', views.PermissionView.list, name='permissions'),   
  path('permissions/search=<str:search>/', views.PermissionView.list, name='permissions-by-search-term'),   
  path('permissions/order=<str:order>/', views.PermissionView.list, name='permissions-by-order'),   
  path('permissions/entry=<str:entry>/', views.PermissionView.list, name='permissions-by-entry'),   
  path('permissions/update/<int:id>/', views.PermissionView.update, name='update-permission'),
	
  # positon view
  path('positions/new/', views.PositionView.post, name='create-position'),
  path('positions/total/', views.PositionView.total, name='total-positions'),
  path('positions/', views.PositionView.list, name='positions'),
  path('positions/department=<int:department>/', views.PositionView.list, name='positions-by-department'),
  path('positions/department=<int:department>/search=<str:search>/', views.PositionView.list, name='positions-by-department'),
  path('positions/department=<int:department>/order=<str:order>/', views.PositionView.list, name='positions-by-department'),
  path('positions/department=<int:department>/entry=<str:entry>/', views.PositionView.list, name='positions-by-department'),
  path('positions/search=<str:search>/', views.PositionView.list, name='positions-by-search-term'),
  path('positions/order=<str:order>/', views.PositionView.list, name='positions-by-order'),
  path('positions/entry=<str:entry>/', views.PositionView.list, name='positions-by-entry'),
  path('positions/get/<int:id>/', views.PositionView.get, name='retrieve-position'),
  path('positions/vacant/', views.PositionView.vacant, name='vacant-positions'),
  path('positions/vacant/<int:department>/', views.PositionView.vacant_by_department, name='vacant-positions-by-department'),
  path('positions/vacancies/', views.PositionView.vacancies, name="position-vacancies"),
  path('positions/update/<int:id>/', views.PositionView.update, name='update-position'),
  path('positions/delete/', views.PositionView.delete, name='delete-position'),
  
  # province view 
  path('provinces/new/', views.ProvinceView.post, name='create-province'),  
  path('provinces/', views.ProvinceView.list, name='provinces'),  
  path('provinces/search=<str:search>/', views.ProvinceView.list, name ='province-by-search-term'),  
  path('provinces/entry=<int:entry>/', views.ProvinceView.list, name ='total-provinces'),  
  path('provinces/total/', views.ProvinceView.total, name ='total-provinces'),  
  path('provinces/get/<int:id>/', views.ProvinceView.get, name ='retrieve-province'),  
  path('provinces/update/<int:id>/', views.ProvinceView.update, name ='update-province'),  
  path('provinces/delete/<int:id>/', views.ProvinceView.delete, name ='delete-province'),  
  
  # residential address view
  path('residential-address/new/', views.ResidentialAddressView.post, name='create-address'),
  path('residential-address/<int:employee>/', views.ResidentialAddressView.get, name='retrieve-address'),
  path('residential-address/update/<int:id>/', views.ResidentialAddressView.update, name='update-address'),
  
  # report view
  path('reports/new/', views.ReportView.post, name='create-report'),
  path('reports/', views.ReportView.list, name='reports'),
  path('reports/<int:employee>/', views.ReportView.reports_by_employee, name='reports'),
  path('reports/total/', views.ReportView.total, name='total-reports'),
  path('reports/search=<str:search>/', views.ReportView.list, name='reports-by-search-term'),
  path('reports/order=<str:order>/', views.ReportView.list, name='reports-by-order'),
  path('reports/entry=<str:entry>/', views.ReportView.list, name='reports-by-entry'),
  path('reports/get/<int:employee>/', views.ReportView.get, name='retrieve-reports'),
  path('reports/get/<int:employee>/total/', views.ReportView.total, name='total-reports-by-employee'),
  path('reports/get/<int:employee_no>/search=<str:search>/', views.ReportView.get, name='retrieve-reports-by-search-term'),
  path('reports/get/<int:employee_no>/order=<str:order>/', views.ReportView.get, name='retrieve-reports-by-order'),
  path('reports/get/<int:employee_no>/entry=<str:entry>/', views.ReportView.get, name='retrieve-reports-by-entry'),
  path('reports/update/<int:id>/', views.ReportView.update, name='update-job'),
  path('reports/delete/<int:id>/', views.ReportView.delete, name='delete-job'),
  
  # role view 
  path('roles/new/', views.RoleView.post, name='create-role'),  
  path('roles/', views.RoleView.list, name='roles'),  
  path('roles/get/<int:id>/', views.RoleView.get, name ='retrieve-role'),  
  path('roles/search=<str:search>/', views.RoleView.list, name ='roles-by-search-term'),  
  path('roles/entry=<int:entry>/', views.RoleView.list, name ='total-roles'),  
  path('roles/total/', views.RoleView.total, name ='total-roles'),  
  path('roles/update/<int:id>/', views.RoleView.update, name ='update-role'),  
  path('roles/delete/<int:id>/', views.RoleView.delete, name='delete-role'),
  
  # sex view 
  path('sexes/new/', views.SexView.post, name='create-sex'),  
  path('sexes/', views.SexView.list, name='sexes'),  
  path('sexes/get/<int:id>/', views.SexView.get, name ='retrieve-sex'),  
  path('sexes/search=<str:search>/', views.SexView.list, name ='sexes-by-search-term'),  
  path('sexes/entry=<int:entry>/', views.SexView.list, name ='total-sexes'),  
  path('sexes/total/', views.SexView.total, name ='total-sexes'),  
  path('sexes/update/<int:id>/', views.SexView.update, name ='update-sex'),  
  path('sexes/delete/<int:id>/', views.SexView.delete, name='delete-sex'),
  
  # salary view 
  path('salaries/new/', views.SalaryView.post, name='create-salary'),
  path('salaries/total/', views.SalaryView.total, name='salaries'),
  path('salaries/', views.SalaryView.list, name='salaries'),
  path('salaries/get/<int:id>/', views.SalaryView.get, name ='retrieve-salary'),  
  path('salaries/update/<int:id>/', views.SalaryView.update, name ='update-salary'),  
  path('salaries/delete/<int:id>/', views.SalaryView.delete, name ='delete-salary'),  
  
  # settings view
  path('settings/', views.SettingsView.get, name='settings'),
  path('settings/update/', views.SettingsView.update, name='update-settings'),
  
  # spouse view
  path('spouses/new/', views.SpouseView.post, name='create-spouse'),
  path('spouses/get/<int:employee>/', views.SpouseView.get, name='retrieve-spouse'),
  path('spouses/update/<int:id>/', views.SpouseView.update, name='update-spouse'),
  
  # session view
  path('sessions/', views.SessionView.list, name='sessions'),
  path('sessions/login/', views.SessionView.login, name='login'),
  path('sessions/get/<str:session_id>/', views.SessionView.get, name='retrieve-session'),
  path('sessions/update/', views.SessionView.update, name='update'),
  path('sessions/logout/<str:session_id>/', views.SessionView.logout, name='logout'),
  path('sessions/logout/username=<str:username>/', views.SessionView.logout, name='logout'),
  path('sessions/clear/', views.SessionView.clear, name='logout'),

  # educational background
  path('educational-backgrounds/new/', views.EducationalBackgroundView.post, name='create-educational-background'),
  path('educational-backgrounds/get/<int:id>/', views.EducationalBackgroundView.get, name='retrieve-educational-backgrounds'),
  path('educational-backgrounds/<int:employee>/', views.EducationalBackgroundView.list, name='educational-backgrounds'),
  path('educational-backgrounds/update/<int:id>/', views.EducationalBackgroundView.update, name='update-educational-backgrounds'),
  
  # father view
  path('fathers/new/', views.FatherView.post, name='create-father'),
  path('fathers/get/<int:employee>/', views.FatherView.get, name='retrieve-father'),
  path('fathers/update/<int:id>/', views.FatherView.update, name='update-father'),
  
  # file view
  path('my-files/new/', views.FileView.post, name='create-file'),
  path('my-files/total/<str:username>/', views.FileView.total, name='total-files'),
  path('my-files/', views.FileView.list, name='files'),
  path('my-files/get/<str:username>/', views.FileView.get, name='retrieve-file'),
  path('my-files/get/<str:username>/search_term=<str:search_term>/', views.FileView.get, name='retrieve-file-by-search-term'),
  path('my-files/get/<str:username>/entry=<str:entry>/', views.FileView.get, name='retrieve-file-by-entry'),
  path('my-files/get/<str:username>/order=<str:order>/',   views.FileView.get, name='retrieve-file-by-order'),
  path('my-files/update/<int:id>/', views.FileView.update, name='update-file'), 
  path('my-files/delete/<int:id>/', views.FileView.delete, name='delete-file'),
  path('my-files/clear/', views.FileView.clear, name='delete-all-files'),
  
  # user group view
  path('user-groups/new/', views.UserGroupView.post, name='create-user-group'),
  path('user-groups/total/', views.UserGroupView.total, name='total-user-groups'),    
  path('user-groups/', views.UserGroupView.list, name='user-groups'),
  path('user-groups/search=<str:search>/', views.UserGroupView.list, name='user-group-by-search-term'),
  path('user-groups/entry=<int:entry>/', views.UserGroupView.list, name='user-groups-by-entry'),
  path('user-groups/get/<int:id>/', views.UserGroupView.get, name='retrieve-user-group'),
  path('user-groups/get/username=<str:username>/', views.UserGroupView.get, name='retrieve-user-group'),
  path('user-groups/update/<int:id>/', views.UserGroupView.update, name='update-user-group'),
  path('user-groups/update/user=<int:user>/', views.UserGroupView.update, name='update-user-group'),
  path('user-groups/delete/<int:id>/', views.UserGroupView.delete, name='delete-user-group'),
  
  # user permissions view
  path('user-permissions/new/', views.UserPermissionsView.post, name='create-employee'),
  path('user-permissions/', views.UserPermissionsView.list, name='user-permissions'),
  path('user-permissions/<int:user>/', views.UserPermissionsView.list, name='user-permissions-by-user'),
  path('user-permissions/total/', views.UserPermissionsView.total, name='total-user-permissions'),
  path('user-permissions/search=<str:search>/', views.UserPermissionsView.list, name='user-permissions-by-search-term'),
  path('user-permissions/entry=<int:entry>/', views.UserPermissionsView.list, name='user-permissions-by-entry'),
  path('user-permissions/get/<int:id>/', views.UserPermissionsView.get, name='user-permissions-by-id'),
  path('user-permissions/update/<int:id>/', views.UserPermissionsView.update, name='update-user-permission'),
  path('user-permissions/delete/', views.UserPermissionsView.delete, name='delete-user-permission'),
  path('user-permissions/delete/<int:id>/', views.UserPermissionsView.delete, name='delete-user-permission'),
  path('user-permissions/delete/user=<int:id>/', views.UserPermissionsView.delete, name='delete-user-permission'),
  
  # user type view
  path('user-types/new/', views.UserTypeView.post, name='create-user-type'),    
  path('user-types/total/', views.UserTypeView.total, name='total-user-types'),    
  path('user-types/', views.UserTypeView.list, name='user-types'),    
  path('user-types/entry=<int:entry>/', views.UserTypeView.list, name ='user-types-by-entry'),  
  path('user-types/update/<int:id>/', views.UserTypeView.update, name ='update-user-type'),  
  path('user-types/delete/<int:id>/', views.UserTypeView.delete, name='delete-user-type'),
  
  # user view
  path('users/new/', views.UserView.post, name='create-user'),
  path('users/total/', views.UserView.total, name='total-users'),
  path('users/', views.UserView.list, name='users'),    
  path('users/unused-accounts/', views.UserView.unused_accounts, name='users'),    
  path('users/no-user-group/', views.UserView.no_user_group, name='no-user-group'),    
  path('users/emails/', views.UserView.emails, name='user-emails'),
  path('users/search=<str:search>/', views.UserView.list, name='users-by-search'),    
  path('users/entry=<int:entry>/', views.UserView.list, name='users-by-entry'),    
  path('users/order=<str:order>/', views.UserView.list, name='users-by-order'),     
  path('users/get/employee=<int:employee>/', views.UserView.get, name='retrieve-user'), 
  path('users/get/username=<str:username>/', views.UserView.get, name='retrieve-user'), 
  path('users/validate-email/<str:email>/', views.UserView.validate_email, name='validate-email'),
  path('users/update/username=<str:username>/', views.UserView.update, name='update-user'),
  path('users/update/<int:id>/', views.UserView.update, name='update-user'),
  path('users/update-password/', views.UserView.update_password, name='update-password'),
  path('users/reset-password/',   views.UserView.reset_password, name='reset-password'),
  path('users/login/<str:username>/', views.UserView.login, name='login'),
  path('users/logout/<str:username>/', views.UserView.logout, name='logout'),
  path('users/activate/username=<str:username>/', views.UserView.activate, name='deactivate-user'),
  path('users/activate/employee=<int:employee>/', views.UserView.activate, name='activate-user'),
  path('users/activate/<int:id>/', views.UserView.activate, name='activate-user'),
  path('users/deactivate/username=<str:username>/', views.UserView.deactivate, name='deactivate-user'),
  path('users/deactivate/employee=<int:employee>/', views.UserView.deactivate, name='deactivate-user'),
  path('users/deactivate/<int:id>/', views.UserView.deactivate, name='deactivate-user'),
  
  # user activity view
  path('user-activities/new/', views.UserActivityView.post, name='create-user-activity'),  
  path('user-activities/total/', views.UserActivityView.total, name='total-user-activities'),
  path('user-activities/total/<str:username>/', views.UserActivityView.total_by_user, name='total-user-activities-by-user'),
  path('user-activities/search=<str:search>/', views.UserActivityView.list, name='user-activities-by-search'),    
  path('user-activities/order=<str:order>/', views.UserActivityView.list, name='user-activities-by-order'), 
  path('user-activities/', views.UserActivityView.list, name='user-activities'),
  ]
