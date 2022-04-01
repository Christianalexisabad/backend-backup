from .utility import adjusted_date, capitalize, starts_with_capital_letter, has_illegal_chars, password_length_valid, get_name,get_device, order_list, get_duration
from .hashutility import hashedPassword,checkPassword, encrypt, decrypt, generated_session_id, generated_employee_no, stringify
from . import date
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q 
from . import serializers
from . import filters
from . import models
from django.conf import settings
from bcrypt import *
import sys
import json
import re
from dateutil.relativedelta import *
from django.core.mail import send_mail

current_date = date.get_current_date()

class PermanentAddressView:
    
    # create address
    @api_view(['POST'])
    def post(request):
        
        try:
            employee = request.data["employee"]
        
            if models.PermanentAddress.objects.filter(employee=employee).exists():
                return Response({
                    "message": "Address with employee no " + employee + " already exists!", 
                }, status=status.HTTP_409_CONFLICT)      
            
            serializer = serializers.PermanentAddress(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "Updated Successfully!", 
                    "data": serializer.data 
                }, status=status.HTTP_201_CREATED)

            return Response({
                "message": "Bad request",
                "data": request.data
            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    # retrieve permanent address
    @api_view(['GET'])
    def get(request, employee):

        try:
            data = models.PermanentAddress.objects.get(employee=employee)
            serializer = serializers.PermanentAddress(data, many=False)
            
            return Response({
                "message": "Success!", 
                "data": serializer.data 
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "message": "Record not found.",
                "data": {}
            }, status=status.HTTP_404_NOT_FOUND)
        
    # update permanent address
    @api_view(['PATCH'])
    def update(request, employee):
        
        try:
            instance = models.PermanentAddress.objects.get(employee=employee)
            
            serializer = serializers.PermanentAddress(
                instance=instance, 
                data=request.data
            )
        
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "Updated Successfully!", 
                    "data": serializer.data 
                }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                "message": str(e), 
            })


class ResidentialAddressView:
    
    # create address
    @api_view(['POST'])
    def post(request):
        
        try:
            employee = request.data["employee"]
        
            if models.PermanentAddress.objects.filter(employee=employee).exists():
                return Response({
                    "message": "Address with employee no " + employee + " already exists!", 
                }, status=status.HTTP_409_CONFLICT)    
                
            serializer = serializers.ResidentialAddress(data=request.data)
        
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "Updated Successfully!", 
                    "data": serializer.data 
                }, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({
                "message": str(e)
            })
    
    # retrieve residential address
    @api_view(['GET'])
    def get(request, employee):
        
        try:
            data = models.ResidentialAddress.objects.get(employee=employee)
            serializer = serializers.ResidentialAddress(data, many=False)
        
            return Response({
                "message": "Success!", 
                "data": serializer.data 
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                "message": "Record not found.",
                "data": {}
            }, status=status.HTTP_404_NOT_FOUND)
        
    # update permanent address
    @api_view(['PATCH', 'PUT'])
    def update(request, id):
        
        instance = models.ResidentialAddress.objects.get(pk=id)

        serializer = serializers.ResidentialAddress(
            instance=instance, 
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Updated Successfully!", 
                "data": serializer.data 
            }, status=status.HTTP_200_OK)
       

class AttendanceStatusView:  

    # create attendance status
    @api_view(['POST'])
    def post(request):
       
        serializer = serializers.AttendanceStatus(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Created Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
    
        return Response({
            "message": "Failed to add status."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # attendance status list
    @api_view(['GET'])
    def list(request, **kwargs):
        
        data = models.AttendanceStatus.objects.all()
      
        if kwargs.get("search"):
            term = kwargs.get("search")
            data = models.AttendanceStatus.objects.filter(
                Q(name__icontains=term) | 
                Q(pk__iexact=term)
            )
        elif kwargs.get("entry"):
            data = models.AttendanceStatus.objects.all()[:kwargs.get("entry")]
       
        serializer = serializers.AttendanceStatus(data, many=True)
        
        return Response({
            "messsage": "Success!", 
            "total": len(serializer.data), 
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # total attendance statuss
    @api_view(['GET'])
    def total(request):
        
        data = models.AttendanceStatus.objects.count()
       
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)
    
    # retrieve attendance status
    @api_view(['GET'])
    def get(request, id):
        
        try:
            data = models.AttendanceStatus.objects.get(pk=id)
      
            serializer = serializers.AttendanceStatus(data, many=False)
          
            return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)
       
        except Exception as e:
            return Response({
                "message": "Record not found.",
                "data": {}
            }, status=status.HTTP_404_NOT_FOUND)
        
    # update attendance status
    @api_view(['PATCH'])
    def update(request, id):
        
        instance = models.AttendanceStatus.objects.get(pk=id)
      
        serializer = serializers.AttendanceStatus(
            instance=instance, 
            data=request.data
        )
       
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
       
        return Response({ 
            "message": "Update Failed!"
        }, status=status.HTTP_400_BAD_REQUEST)

class AccountRequestView:
    
    # request account
    @api_view(['POST'])
    def post(request):
        
        try:
            serializer = serializers.AccountRequest(data=request.data)
           
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "Request sent!", 
                    "data": serializer.data 
                }, status=status.HTTP_201_CREATED)
           
            return Response({
                "message": "Success!", 
                "data": serializer.data 
            }, status=status.HTTP_200_OK)

        
        except Exception as e:
            return Response({
                "message": "Data not found!"
            }, status=status.HTTP_404_NOT_FOUND)
        
    # account requests
    @api_view(['GET'])
    def list(request):
     
        data = models.AccountRequest.objects.all()

        serializer = serializers.AccountRequest(data, many=True)
       
        return Response({
            "message": "Success", 
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    
    @api_view(['PATCH'])
    def approve_account(request, id):
        
        instance = models.AccountRequest.objects.get(pk=id)
        
        serializer = serializers.AccountRequest(
            instance=instance, 
            data={
                "status": 1
            }
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Account approved!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        return Response({
            "message": "Success!", 
            "data": serializer.data 
        }, status=status.HTTP_200_OK)

    
    @api_view(['PATCH'])
    def decline_account(request, id):
    
        instance = models.AccountRequest.objects.get(pk=id)
       
        serializer = serializers.AccountRequest(
            instance=instance, 
            data={
                "status": 0
            }
        )
    
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Account declined!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
       
        return Response({
            "message": "Success!", 
            "data": serializer.data 
        }, status=status.HTTP_200_OK)


    @api_view(['PATCH'])
    def update(request, id):
     
        instance = models.AccountRequest.objects.get(pk=id)
    
        serializer = serializers.AccountRequest(
            instance=instance, 
            data=request.data
        )
     
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Request updated!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
     
        return Response({
            "message": "Success!", 
            "data": serializer.data 
        }, status=status.HTTP_200_OK)

        
class AnnouncementView:

    # create announcement
    @api_view(['POST'])
    def post(request):
       
        serializer = serializers.Announcement(
            data=request.data, 
            many=False
        )
       
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, 
                status=status.HTTP_201_CREATED
            )
       
        return Response({
            "message": "Success!", 
            "data": serializer.data 
        }, status=status.HTTP_200_OK)


    # total announcements
    @api_view(['GET'])
    def total(request):
       
        total = models.Announcement.objects.count()
        return Response(total)

    # list of announcements
    @api_view(['GET'])
    def list(request):
     
        data = models.Announcement.objects.all().order_by("-id")
        
        serializer = serializers.Announcement(data, many=True)

        return Response({
            "message": "Success!", 
            "total": len(serializer.data), 
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # update announcement
    @api_view(['PATCH'])
    def update(request, id):
     
        instance = models.Announcement.objects.get(pk=id)
      
        serializer = serializers.Announcement(
            instance=instance, 
            data=request.data
        )
     
        if serializer.is_valid():
            serializer.save()
            return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)
     
        return Response({
            "message": "Success!", 
            "data": serializer.data 
        }, status=status.HTTP_200_OK)


    # delete announcement
    @api_view(['DELETE'])
    def delete(request, id):
     
        models.Announcement.objects.get(pk=id).delete()

        return Response({
            "message": "Deleted Successfully!"
        }, status=status.HTTP_200_OK)

class AttendanceView:

    # create attendance
    @api_view(['POST'])
    def post(request):
        
        try:
            serializer = serializers.Attendance(data=request.data)
          
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "Time In Success!"
                }, status=status.HTTP_201_CREATED)
          
            return Response({
                "message": "Time In Failed!"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({
                "message": "Data not found!"
            }, status=status.HTTP_404_NOT_FOUND)

    # total attendances 
    @api_view(['GET'])
    def total(request, **kwargs):

        if kwargs.get("employee"): 
            total = models.Attendance.objects.filter(employee=kwargs.get("employee")).count()
        else:
            total = models.Attendance.objects.count()
       
        return Response(total, status=status.HTTP_200_OK)

    # total attendances 
    @api_view(['GET'])
    def get_attendance(request, **kwargs):
        
        employee = kwargs.get("employee")
        status = kwargs.get("status")

        total = models.Attendance.objects.filter(
            Q(employee=employee) & 
            Q(date__icontains=get_year_and_month()) & 
            Q(am_status=status) & 
            Q(pm_status=status)
        ).count()
        
        return Response(total)

    #  attendance today 
    @api_view(['GET'])
    def today(request, **kwargs):
        
        try:
            data = models.Attendance.objects.get(
                employee=kwargs.get("employee"), 
                date=kwargs.get("date")
            )
        
            serializer = serializers.Attendance(data, many=False)
            
            return Response({
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                "message": "Data not found!"
            }, status=status.HTTP_404_NOT_FOUND)

    # attendance list
    @api_view(['GET'])
    def list(request, **kwargs):
     
        try:
            data = models.Attendance.objects.filter(filters.attendance(kwargs)).order_by(*order_list(kwargs.get("order")))
        except Exception as e:
            data = models.Attendance.objects.all().order_by(*order_list(kwargs.get("order")))
            
        serializer = serializers.Attendances(data, many=True)
     
        return Response({
            "message": "Success!", 
            "total": len(serializer.data), 
            "data": serializer.data
        }, status=status.HTTP_200_OK)


    # get attendance   
    @api_view(['GET'])
    def get(request, **kwargs):
        
        try:
            data = models.Attendance.objects.get(employee=kwargs.get("employee"), date__icontains=kwargs.get("date"))
            
            serializer = serializers.Attendances(data, many=False)
            
            return Response({
                "message": 
                "Success!", 
                "data": serializer.data 
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "message": "No records found!",
            }, status=status.HTTP_404_NOT_FOUND)
        
    # update attendance
    @api_view(['PATCH'])
    def update(request, id):
        
        instance = models.Attendance.objects.get(pk=id)
       
        serializer = serializers.Attendance(
            instance=instance, 
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Attendance updated."
            }, status=status.HTTP_200_OK)
        
        return Response({
            "message": "Success!", 
            "data": serializer.data 
        }, status=status.HTTP_200_OK)


    # presents 
    @api_view(['GET'])
    def count_attendance(request, status):

        if date.get_datetime().find("AM") > -1:
            total = models.Attendance.objects.filter(
                am_status=status, 
                date__icontains=date.get_current_date()
            ).count()
       
        else:
            total = models.Attendance.objects.filter(
                pm_status=status, 
                date__icontains=date.get_current_date()
            ).count()
      
        return Response(total)
    
    # delete attendance a
    @api_view(['DELETE'])
    def delete(request):
       
        models.Attendance.objects.all().delete()
       
        return Response({
            "message": "Deleted Successfully!"
        }, status=status.HTTP_200_OK)

class BarangayView:  

    # create barangay
    @api_view(['POST'])
    def post(request):
     
        serializer = serializers.Barangay(data=request.data)
     
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Barangay added Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
     
        return Response({ 
            "message": "Unable to add barangay."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # barangay list
    @api_view(['GET'])
    def list(request, **kwargs):
        
        data = models.Barangay.objects.all()
       
        if kwargs.get("search"):
            term = kwargs.get("search")
            data = models.Barangay.objects.filter(
                Q(name__icontains=term) | 
                Q(pk__iexact=term)
            )

        elif kwargs.get("entry"):
            data = models.Barangay.objects.all()[:kwargs.get("entry")]
        
        serializer = serializers.Barangay(data, many=True)
        
        return Response({
            "message": "Success!",
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    
    # retrieve barangay
    @api_view(['GET'])
    def get(request, id):
        
        try:
            data = models.Barangay.objects.get(pk=id)
            serializer = serializers.Barangay(data, many=False)
           
            return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                "message": "Record not found.",
                "data": {}
            }, status=status.HTTP_404_NOT_FOUND)

    # total countries
    @api_view(['GET'])
    def total(request):
        
        data = models.Barangay.objects.count()
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)

    # update barangay
    @api_view(['PATCH'])
    def update(request, id):
        
        instance = models.Barangay.objects.get(pk=id)
      
        serializer = serializers.Barangay(
            instance=instance, 
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        return Response({ 
            "message": "Failed to update barangay."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # delete barangay
    @api_view(['DELETE'])
    def delete(request, id):
     
        models.Barangay.objects.get(pk=id).delete()
    
        return Response({
            "message": "Deleted Successfully!"
        }, status=status.HTTP_200_OK)

class ContributionDeadlineView:  

    # create contribution deadline
    @api_view(['POST'])
    def post(request):
     
        serializer = serializers.ContributionDeadline(data=request.data)
     
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "ContributionDeadline added Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
     
        return Response({ 
            "message": "Unable to add contribution deadline."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # contribution deadline list
    @api_view(['GET'])
    def list(request, **kwargs):
        
        data = models.ContributionDeadline.objects
       
        if kwargs.get("search"):
            term = kwargs.get("search")
            data = models.ContributionDeadline.objects.filter(
                Q(name__icontains=term) | 
                Q(pk__iexact=term)
            )
        elif kwargs.get("entry"):
            data = models.ContributionDeadline.objects.all()[:kwargs.get("entry")]
       
        serializer = serializers.ContributionDeadline(data, many=True)
       
        return Response({
            "messsage": "Success!", 
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    
    # retrieve contribution deadline
    @api_view(['GET'])
    def get(request, id):
        
        try:
            data = models.ContributionDeadline.objects.get(pk=id)
            serializer = serializers.ContributionDeadline(data, many=False)
     
            return Response({
                "messsage": "Success!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
      
        except Exception as e:
            return Response({
                "message": "Record not found.",
                "data": {}
            }, status=status.HTTP_404_NOT_FOUND)

    # total contribution deadlines
    @api_view(['GET'])
    def total(request):
      
        data = models.ContributionDeadline.objects.count()
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)

    # update contribution deadline
    @api_view(['PATCH'])
    def update(request, id):
       
        instance = models.ContributionDeadline.objects.get(pk=id)
        
        serializer = serializers.ContributionDeadline(
            instance=instance, 
            data=request.data
        )
       
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        return Response({ 
            "message": "Failed to update contribution deadline."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # delete contribution deadline
    @api_view(['DELETE'])
    def delete(request, id):
    
        models.ContributionDeadline.objects.get(pk=id).delete()
    
        return Response({
            "message": "Deleted Successfully!"
        }, status=status.HTTP_200_OK)


class ContributionView:  

    # create contribution
    @api_view(['POST'])
    def post(request):
        
        serializer = serializers.Contribution(data=request.data)
      
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Contribution added Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
      
        return Response({ 
            "message": "Unable to add contribution."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # contribution list
    @api_view(['GET'])
    def list(request, **kwargs):
        
        data = models.Contribution.objects.all()
        
        if kwargs.get("search"):
            term = kwargs.get("search")
            data = models.Contribution.objects.filter(
                Q(name__icontains=term) | 
                Q(pk__iexact=term)
            )
        elif kwargs.get("entry"):
            data = models.Contribution.objects.all()[:kwargs.get("entry")]
        
        serializer = serializers.Contribution(data, many=True)
        
        return Response({
            "messsage": "Success!", 
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    
    # retrieve contribution
    @api_view(['GET'])
    def get(request, id):
        
        try:
            data = models.Contribution.objects.get(pk=id)
            serializer = serializers.Contribution(data, many=False)
   
            return Response({
                "messsage": "Success!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
   
        except Exception as e:
            return Response({
                "message": "Record not found.",
                "data": {}
            }, status=status.HTTP_404_NOT_FOUND)

    # update contribution
    @api_view(['PATCH'])
    def update(request, id):
        
        instance = models.Contribution.objects.get(pk=id)
      
        serializer = serializers.Contribution(
            instance=instance, 
            data=request.data
        )
 
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        return Response({ 
            "message": "Failed to update contribution."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # delete contribution
    @api_view(['DELETE'])
    def delete(request, id):
       
        models.Contribution.objects.get(pk=id).delete()
        
        return Response({
            "message": "Deleted Successfully!"
        }, status=status.HTTP_200_OK)

class BloodTypeView:  

    # create blood type
    @api_view(['POST'])
    def post(request):
        if models.BloodType.objects.filter(name=request.data["name"]).exists():
            return Response({ 
                "message": "Blood type already exists."
            }, status=status.HTTP_409_CONFLICT)
       
        serializer = serializers.BloodType(data=request.data)
       
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Blood type added Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
       
        return Response({ 
            "message": "Failed to add blood type."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # blood type list
    @api_view(['GET'])
    def list(request, **kwargs):
        
        data = models.BloodType.objects.all()
       
        if kwargs.get("search"):
            term = kwargs.get("search")
            data = models.BloodType.objects.filter(
                Q(name__icontains=term) | 
                Q(pk__iexact=term)
            )
        elif kwargs.get("entry"):
            data = models.BloodType.objects.all()[:kwargs.get("entry")]
       
        serializer = serializers.BloodType(data, many=True)
       
        return Response({
            "message": "Success!",
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # total blood types
    @api_view(['GET'])
    def total(request):
        
        data = models.BloodType.objects.count()
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)
    
    # retrieve blood type
    @api_view(['GET'])
    def get(request, id):
        
        try:
            data = models.BloodType.objects.get(pk=id)
            serializer = serializers.BloodType(data, many=False)
        
            return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                "message": "Record not found.",
                "data": {}
            }, status=status.HTTP_404_NOT_FOUND)
        
    # update blood type
    @api_view(['PATCH'])
    def update(request, id):
        
        instance = models.BloodType.objects.get(pk=id)

        serializer = serializers.BloodType(
            instance=instance, 
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        return Response({ 
            "message": "Update Failed!"
        }, status=status.HTTP_400_BAD_REQUEST)

    # delete blood type
    @api_view(['DELETE'])
    def delete(request, id):
   
        models.BloodType.objects.get(pk=id).delete()
        
        return Response({
            "message": "Deleted Successfully!"
        }, status=status.HTTP_200_OK)

    
class BenefitView:

    # create benefit 
    @api_view(['POST'])
    def post(request):
        
        try:
            serializer = serializers.Benefit(data=request.data)
          
            if serializer.is_valid():
                serializer.save()

                return Response({
                    "message": "Created Successfully!",
                    "data": serializer.data
                }, status=status.HTTP_201_CREATED)
          
            return Response({
                "message": "Success!", 
                "data": serializer.data 
            }, status=status.HTTP_200_OK)

        
        except Exception as e:
            return Response({
                "message": "Data not found!"
            }, status=status.HTTP_404_NOT_FOUND)

    # total benefits 
    @api_view(['GET'])
    def total(request, **kwargs):
        
        if kwargs.get("employee"):
            data = models.Benefit.objects.filter(employee=kwargs.get("employee")).count()
        else:
            data = models.Benefit.objects.count()
        
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)

    @api_view(['GET'])
    def get(request, id):
       
        data = models.Benefit.objects.get(pk=id)
        
        serializer = serializers.Benefits(data, many=False)
       
        return Response({
            "message": "Success!", 
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # benefit list
    @api_view(['GET'])
    def list(request, **kwargs):
      
        try:
            data = models.Benefit.objects.filter(filters.benefit(kwargs)).exclude(employee__employee_status__gt=1).order_by(*order_list(kwargs.get("order")))
        except Exception as e:
            data = models.Benefit.objects.all().order_by(*order_list(kwargs.get("order")))
      
        serializer = serializers.Benefits(data, many=True)
      
        return Response({
            "message": "Success!", 
            "total": len(serializer.data), 
            "data": serializer.data
        }, status=status.HTTP_200_OK)


    # update benefit
    @api_view(['PATCH'])
    def update(request, id):
       
        try:
            instance = models.Benefit.objects.get(pk=id)
            
            serializer = serializers.Benefits(
                instance=instance, 
                data=request.data
            )
       
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "Success!",
                    "data": serializer.data
                }, status=status.HTTP_200_OK)
       
            return Response({
                "message": "No changes made!",
                "data": request.data
            }, status=status.HTTP_304_NOT_MODIFIED)
       
        except Exception as e:
            return Response({
                "message": "Data not found!"
            }, status=status.HTTP_404_NOT_FOUND)
    
    # delete Benefit
    @api_view(['DELETE'])
    def delete(request, id):
       
        models.Benefit.objects.get(pk=id).delete()
       
        return Response({
            "message": "Deleted successfully!"
        }, status=status.HTTP_200_OK)

class Biometrics():

    @api_view(['POST'])
    def post(request):
       
        serializer = serializers.Add_Biometrics(data=request.data)
       
        if serializer.is_valid():
            serializer.save()
       
        return Response({
            "message": "Success!",
            "data": serializer.data,
        }, status=status.HTTP_200_OK)

    @api_view(['GET'])
    def list(request, employee, order, entries):
      
        if employee == "all":
            data = models.Biometrics.objects.all().order_by(order)[:entries]
        else:
            data = models.Biometrics.objects.filter(employee=int(employee)).order_by(order)[:entries]
      
        serializer = serializers.Display_Biometrics(data, many=True)
      
        return Response({
            "message": "Success!",
            "data": serializer.data,
        }, status=status.HTTP_200_OK)
    
class CityView:  

    # create city
    @api_view(['POST'])
    def post(request):
      
        serializer = serializers.City(data=request.data)
      
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "City added Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
      
        return Response({ 
            "message": "Unable to add city."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # city list
    @api_view(['GET'])
    def list(request, **kwargs):
     
        data = models.City.objects.all()
     
        if kwargs.get("search"):
            term = kwargs.get("search")
            data = models.City.objects.filter(
                Q(name__icontains=term) |
                Q(pk__iexact=term)
            )
        elif kwargs.get("entry"):
            data = models.City.objects.all()[:kwargs.get("entry")]
     
        serializer = serializers.Cities(data, many=True)
        return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    
    # retrieve city
    @api_view(['GET'])
    def get(request, id):
        
        try:
            data = models.City.objects.get(pk=id)
            serializer = serializers.City(data, many=False)
        
            return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                "message": "Record not found.",
                "data": {}
            }, status=status.HTTP_404_NOT_FOUND)

    # total countries
    @api_view(['GET'])
    def total(request):
        
        data = models.City.objects.count()
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)

    # update city
    @api_view(['PATCH'])
    def update(request, id):
       
        instance = models.City.objects.get(pk=id)
        
        serializer = serializers.City(
            instance=instance, 
            data=request.data
        )
       
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
       
        return Response({ 
            "message": "Failed to update city."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # delete city
    @api_view(['DELETE'])
    def delete(request, id):
     
        models.City.objects.get(pk=id).delete()
    
        return Response({
            "message": "Deleted Successfully!"
        }, status=status.HTTP_200_OK)
    

class CitizenshipView:  

    # create citizenship
    @api_view(['POST'])
    def post(request):
        
        serializer = serializers.Citizenship(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Citizenship added Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({ 
            "message": "Unable to add citizenship."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # citizenship list
    @api_view(['GET'])
    def list(request, **kwargs):
        
        data = models.Citizenship.objects.all()
        
        if kwargs.get("search"):
            term = kwargs.get("search")
            data = models.Citizenship.objects.filter(
                Q(name__icontains=term) | 
                Q(pk__iexact=term)
            )
        elif kwargs.get("entry"):
            data = models.Citizenship.objects.all()[:kwargs.get("entry")]
        
        serializer = serializers.Citizenship(data, many=True)
        return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    
    # retrieve citizenship
    @api_view(['GET'])
    def get(request, id):
        
        try:
            data = models.Citizenship.objects.get(pk=id)
            serializer = serializers.Citizenship(data, many=False)
        
            return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                "message": "Record not found.",
                "data": {}
            }, status=status.HTTP_404_NOT_FOUND)

    # total citizenship
    @api_view(['GET'])
    def total(request):
        
        data = models.Citizenship.objects.count()
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)

    # update citizenship
    @api_view(['PATCH'])
    def update(request, id):
        
        instance = models.Citizenship.objects.get(pk=id)
      
        serializer = serializers.Citizenship(
            instance=instance, 
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        return Response({ 
            "message": "Failed to update citizenship."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # delete citizenship
    @api_view(['DELETE'])
    def delete(request, id):
     
        models.Citizenship.objects.get(pk=id).delete()
    
        return Response({
            "message": "Deleted Successfully!"
        }, status=status.HTTP_200_OK)
    
    
class CivilStatusView:  

    # create civil status
    @api_view(['POST'])
    def post(request):
        
        if models.CivilStatus.objects.filter(name=request.data["name"]).exists():
            return Response({ 
                "message": "Civil status already exists."
            }, status=status.HTTP_409_CONFLICT)
        
        serializer = serializers.CivilStatus(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Civil status added Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({ 
            "message": "Failed to add civil status."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # civil status list
    @api_view(['GET'])
    def list(request, **kwargs):
    
        data = models.CivilStatus.objects.all()
        
        serializer = serializers.CivilStatus(data, many=True)
        return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # total civil statuss
    @api_view(['GET'])
    def total(request):
     
        data = models.CivilStatus.objects.count()
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)
    
    # retrieve civil status
    @api_view(['GET'])
    def get(request, id):
      
        try:
            data = models.CivilStatus.objects.get(pk=id)
            serializer = serializers.CivilStatus(data, many=False)
      
            return Response({ 
                "message": "Success!", 
                "total": len(serializer.data),
                "data": serializer.data
            }, status=status.HTTP_200_OK)
      
        except Exception as e:
            return Response({
                "message": "Record not found.",
                "data": {}
            }, status=status.HTTP_404_NOT_FOUND)
        

    # update civil status
    @api_view(['PATCH'])
    def update(request, id):
        
        instance = models.CivilStatus.objects.get(pk=id)
        
        serializer = serializers.CivilStatus(
            instance=instance, 
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        return Response({ 
            "message": "Update Failed!"
        }, status=status.HTTP_400_BAD_REQUEST)

    # delete civil status
    @api_view(['DELETE'])
    def delete(request, id):
      
        models.CivilStatus.objects.get(pk=id).delete()
   
        return Response({
            "message": "Deleted Successfully!"
        }, status=status.HTTP_200_OK)
        

class ChildrenView:

    # create children
    @api_view(['POST'])
    def post(request):
      
        serializer = serializers.Children(data=request.data)
      
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Children added.", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
      
        return Response({
            "message": "Failed to add spouse."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['GET'])
    def get(request, id):
        
        try:
            data = models.Children.objects.get(pk=id)
            serializer = serializers.Children(data, many=False)
        
            return Response({
                "message": "Success!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET'])
    def list(request, employee):
        
        data = models.Children.objects.filter(employee=employee)
        
        serializer = serializers.Children(data, many=True)
        
        return Response({
            "message": "Success!", 
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    
    # update children
    @api_view(['PATCH'])
    def update(request, id):
        
        instance = models.Children.objects.get(pk=id)
        
        serializer = serializers.Children(
            instance=instance, 
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        return Response({
            "message": "Data Update Failed!"
        }, status=status.HTTP_400_BAD_REQUEST)

class ContentTypeView:  

    # create content type
    @api_view(['POST'])
    def post(request):
      
        serializer = serializers.ContentType(data=request.data)
      
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Content Type Created Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({ 
            "message": "Failed to Create Content Type."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # content type list
    @api_view(['GET'])
    def list(request, **kwargs):
        
        data = models.ContentType.objects.all()
     
        if kwargs.get("entry"):
            data = models.ContentType.objects.all()[:kwargs.get("entry")]
        
        serializer = serializers.ContentType(data, many=True)
        
        return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # total content types
    @api_view(['GET'])
    def total(request):
        
        data = models.ContentType.objects.count()
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)

    # update content type
    @api_view(['PATCH'])
    def update(request, id):
        
        instance = models.ContentType.objects.get(pk=id)
        
        serializer = serializers.ContentType(
            instance=instance, 
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        return Response({
            "message": "Data Update Failed!"
        }, status=status.HTTP_400_BAD_REQUEST)


class DashboardView:

    @api_view(['GET'])  
    def employee_types(request):

        data = models.EmployeeType.objects.all()
        
        serializer = serializers.EmployeeType(data, many=True)
        data = serializer.data

        output={}
        for i in range(len(data)):
            output[data[i]["name"]] = models.Employee.objects.filter(employee_type=data[i]["id"]).count()

        return Response({
            "message": "Success!", 
            "data": output}, status=status.HTTP_200_OK)

    
    @api_view(['GET'])  
    def employee_sex(request):

        data = models.Sex.objects.all()
        
        serializer = serializers.Sex(data, many=True)
        data = serializer.data

        output={}
        for i in range(len(data)):
            output[data[i]["name"]] = models.Employee.objects.filter(sex=data[i]["id"]).count()

        return Response({
            "message": "Success!", 
            "data": output}, status=status.HTTP_200_OK)


    @api_view(['GET'])  
    def employee_age_ratio(request):

        data = models.Employee.objects.all()
        
        serializer = serializers.Employee(data, many=True)
        data = serializer.data

        output={
            "18-40": models.Employee.objects.filter(age__range=(18, 40)).count(),
            "40-60": models.Employee.objects.filter(age__range=(41, 60)).count()
        }
        
        return Response({
            "message": "Success!", 
            "data": output
        }, status=status.HTTP_200_OK)


    @api_view(['GET'])  
    def daily_attendance(request, **kwargs):

        data={}

        date_range = kwargs.get("date_range").split(":")
        date1 = date_range[0]
        date2 = date_range[1]
    
        days_between = date.days_between(date1, date2)
        
        for index in range(days_between + 1):
            
            new_date = adjusted_date(date1, index)
            
            count = models.Attendance.objects.filter(
                am_status=1, 
                pm_status=1, 
                date__icontains=new_date
            ).count()
            
            data[new_date] = count
            
        return Response({
            "message": "Success!",
            "total": len(data),
            "data": data
        }, status=status.HTTP_200_OK)

    
    @api_view(['GET'])  
    def employee_monthly_attendance(request, employee, start_date, end_date):

        output={} 
        month_difference = date.months_between(start_date[:7], end_date[:7])
        last_month = date.last_month(start_date[:7], 3)

        for i in range(month_difference + 1):
            
            last_month = last_month(start_date[:7], i-1)
            last_month = str(last_month)[:7]

            output[last_month] = models.Attendance.objects.filter(
                employee=employee, 
                am_status=1, 
                pm_status=1, 
                date__icontains=last_month
            ).count()
        
        return Response({
            "message": "Success!", 
            "data": output
        }, status=status.HTTP_200_OK)

    @api_view(['GET'])  
    def super_admin_dashboard(request):

        return Response({
            "users": models.User.objects.count(),
            "new_users": models.User.objects.filter(created_at=date.get_current_date()).count(),
            "online": models.User.objects.filter(is_active=1).count(),
            "offline": models.User.objects.filter(is_active=0).count(),
        })

    @api_view(['GET'])  
    def inventory_dashboard(request):

        new_items = 0

        for i in range(8):
            new_items += models.OfficeSupply.objects.filter(assumption_date__icontains=adjusted_date(-(i))).count()
            new_items += models.Equipment.objects.filter(assumption_date__icontains=adjusted_date(-(i))).count()

        return Response({
            "total_items": models.OfficeSupply.objects.count() +  models.Equipment.objects.count(),
            "office_supplies": models.OfficeSupply.objects.count(),
            "equipments": models.Equipment.objects.count(),
            "new_items": new_items,
        })
    
    @api_view(['GET'])  
    def admin_dashboard(request):
       
        return Response({
            "departments": models.Department.objects.count(),
            "positions": models.Position.objects.count(),
            "employees": models.Employee.objects.count(),
            "users": models.User.objects.count(),
            "items": models.OfficeSupply.objects.count() + models.Equipment.objects.count(),
            "files": models.File.objects.count(),
            # "history": models.LoginHistory.objects.count() + models.UserActivity.objects.count(),
            "reports": models.Report.objects.count()
        })

    @api_view(['GET']) 
    def hr_dashboard(request):

        new_employees = 0

        # present_filter_set = (Q(date=current_date) & (Q(am_status=1) | Q(pm_status=1)))
        # late_filter_set = (Q(date=current_date) & (Q(am_status=2) | Q(pm_status=2)))
        # absent_filter_set = (Q(date=current_date) & (Q(am_status=4) | Q(pm_status=4)))
        # employee_leave = (Q(start_date__gte=current_date) & Q(end_date__lte=current_date) & Q(hr_remarks=1))

        # for i in range(8):
        #     new_employees += models.Employee.objects.filter(created_at__icontains=adjusted_date(-(i))).count()

        return Response({
            # "employees": models.Employee.objects.count(),
            # "new_employee": new_employees,
            # # "regular": models.JobHistory.objects.filter(employee_type=1).count(),
            # # "contractual": models.JobHistory.objects.filter(employee_type=2).count(),
            # 1: models.Attendance.objects.filter(*{present_filter_set}).count(),
            # "late": models.Attendance.objects.filter(*{late_filter_set}).count(),
            # "on_leave": models.Leave.objects.filter(*{employee_leave}).count(),
            # "absent": models.Attendance.objects.filter(*{absent_filter_set}).count(),
        })

    @api_view(['GET'])
    def employee_dashboard(request, employee):

        present_filter_set = (
            Q(employee=employee) & 
            Q(date=current_date) & 
            (
                Q(am_status=1) | 
                Q(pm_status=1)
            )
        )

        late_filter_set = (
            Q(employee=employee) & 
            Q(date=current_date) & 
            (
                Q(am_status=2) | 
                Q(pm_status=2)
            )
        )

        absent_filter_set = (
            Q(employee=employee) & 
            Q(date=current_date) & 
            (
                Q(am_status=4) | 
                Q(pm_status=4)
            )
        )

        employee_leave = (
            Q(employee=employee) & 
            Q(start_date__gte=current_date) & 
            Q(end_date__lte=current_date) & 
            Q(hr_remarks=1)
        )

        employee = models.Employee.objects.get(pk=employee)
        employee_serializer = serializers.Employee(employee, many=False)

        present = models.Attendance.objects.filter(*{present_filter_set}).count()
        late = models.Attendance.objects.filter(*{late_filter_set}).count()
        absent = models.Attendance.objects.filter(*{absent_filter_set}).count()
        on_leave = models.Leave.objects.filter(*{employee_leave}).count()
        benefits = models.Benefit.objects.filter(employee=employee).count()
        
        return Response({ 
                "present": present,
                "late": late,
                "absent": absent,
                "on_leave": on_leave,
                "benefits": benefits,
        })

class EmployeeTypeView:  

    # create employee type
    @api_view(['POST'])
    def post(request):
     
        if models.EmployeeType.objects.filter(name=request.data["name"]).exists():
            return Response({ 
                "message": "Employee type already exists."
            }, status=status.HTTP_409_CONFLICT)
     
        serializer = serializers.EmployeeType(data=request.data)
     
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Employee type added Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
     
        return Response({ 
            "message": "Failed to add employee type."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # employee types
    @api_view(['GET'])
    def list(request, **kwargs):
        
        data = models.EmployeeType.objects.all()
        
        if kwargs.get("search"):
            term = kwargs.get("search")
            data = models.EmployeeType.objects.filter(
                Q(name__icontains=term) | 
                Q(pk__iexact=term)
            )
        elif kwargs.get("entry"):
            data = models.EmployeeType.objects.all()[:kwargs.get("entry")]
        
        serializer = serializers.EmployeeType(data, many=True)
        
        return Response({
            "message": "Success!",
            "total": len(serializer.data),
            "data": serializer.data,
        }, status=status.HTTP_200_OK)

    # total employee types
    @api_view(['GET'])
    def total(request):
        
        data = models.EmployeeType.objects.count()
        return Response({ 
                "message": "Success!", 
            "data": data 
        }, status=status.HTTP_200_OK)
    
    # retrieve employee type
    @api_view(['GET'])
    def get(request, id):
        
        try:
            data = models.EmployeeType.objects.get(pk=id)
            serializer = serializers.EmployeeType(data, many=False)
       
            return Response({ 
                "message": "Success!", 
                "total": len(serializer.data),
                "data": serializer.data
            }, status=status.HTTP_200_OK)
       
        except Exception as e:
            return Response({
                "message": "Record not found.",
                "data": {}
            }, status=status.HTTP_404_NOT_FOUND)
        

    # update employee type
    @api_view(['PATCH'])
    def update(request, id):
      
        instance = models.EmployeeType.objects.get(pk=id)
        
        serializer = serializers.EmployeeType(
            instance=instance, 
            data=request.data
        )
      
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
      
        return Response({ 
            "message": "Update Failed!"
        }, status=status.HTTP_400_BAD_REQUEST)

    # delete employee type
    @api_view(['DELETE'])
    def delete(request, id):
       
        models.EmployeeType.objects.get(pk=id).delete()

        return Response({
            "message": "Deleted Successfully!"
        }, status=status.HTTP_200_OK)
           
class EmployeeStatusView:  

    # create employee status
    @api_view(['POST'])
    def post(request):
        
        serializer = serializers.EmployeeStatus(data=request.data)
       
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Employee status added Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
       
        return Response({ 
            "message": "Failed to add employee status."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # employee status list
    @api_view(['GET'])
    def list(request, **kwargs):
        
        data = models.EmployeeStatus.objects.all()
     
        if kwargs.get("search"):
            term = kwargs.get("search")
            data = models.EmployeeStatus.objects.filter(
                Q(name__icontains=term) | 
                Q(pk__iexact=term)
            )
        elif kwargs.get("entry"):
            data = models.EmployeeStatus.objects.all()[:kwargs.get("entry")]
        
        serializer = serializers.EmployeeStatus(data, many=True)
     
        return Response({
            "message": "Success!",
            "total": len(serializer.data),
            "data": serializer.data,
        }, status=status.HTTP_200_OK)

    # total employee statuss
    @api_view(['GET'])
    def total(request):
        
        data = models.EmployeeStatus.objects.count()
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)
    
    # retrieve employee status
    @api_view(['GET'])
    def get(request, id):
        
        try:
            data = models.EmployeeStatus.objects.get(pk=id)
            serializer = serializers.EmployeeStatus(data, many=False)
            
            return Response({ 
                "message": "Success!", 
                "total": len(serializer.data),
                "data": serializer.data
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                "message": "Record not found.",
                "data": {}
            }, status=status.HTTP_404_NOT_FOUND)
        

    # update employee status
    @api_view(['PATCH'])
    def update(request, id):
        
        instance = models.EmployeeStatus.objects.get(pk=id)
       
        serializer = serializers.EmployeeStatus(
            instance=instance, 
            data=request.data
        )
      
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
      
        return Response({ 
            "message": "Update Failed!"
        }, status=status.HTTP_400_BAD_REQUEST)

    
class EmployeeStatusHistoryView:  

    # create employee status
    @api_view(['POST'])
    def post(request):
        
        serializer = serializers.EmployeeStatusHistory(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Statuss Changed Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({ 
            "message": "Failed to add employee status history."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # employee status history list
    @api_view(['GET'])
    def list(request, **kwargs):
      
        data = models.EmployeeStatusHistory.objects.all()
      
        if kwargs.get("search"):
            term = kwargs.get("search")
            data = models.EmployeeStatusHistory.objects.filter(
                Q(name__icontains=term) | 
                Q(pk__iexact=term)
            )
        elif kwargs.get("entry"):
            data = models.EmployeeStatusHistory.objects.all()[:kwargs.get("entry")]
      
        serializer = serializers.EmployeeStatusHistory(data, many=True)
      
        return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # employee status history list
    @api_view(['GET'])
    def employee_status_history_list(request, **kwargs):

        employee = kwargs.get("employee")

        if kwargs.get("search"):
            term = kwargs.get("search")
            data = models.EmployeeStatusHistory.objects.filter(
                Q(name__icontains=term) | 
                Q(pk__iexact=term)
            )
        elif kwargs.get("entry"):
            data = models.EmployeeStatusHistory.objects.filter(employee=employee)[:kwargs.get("entry")]
        else: 
            data = models.EmployeeStatusHistory.objects.filter(employee=employee)
        
        serializer = serializers.EmployeeStatusHistory(data, many=True)
        
        return Response({
            "message": "Success!", 
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # total employee status historys
    @api_view(['GET'])
    def total(request):
        
        data = models.EmployeeStatusHistory.objects.count()
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)
    
    # retrieve employee status history
    @api_view(['GET'])
    def get(request, id):
        
        try:
            data = models.EmployeeStatusHistory.objects.get(pk=id)
            serializer = serializers.EmployeeStatusHistory(data, many=False)
       
            return Response({ 
                "message": "Success!", 
                "total": len(serializer.data),
                "data": serializer.data
            }, status=status.HTTP_200_OK)
       
        except Exception as e:
            return Response({
                "message": "Record not found.",
                "data": {}
            }, status=status.HTTP_404_NOT_FOUND)

    # update employee status history
    @api_view(['PATCH'])
    def update(request, id):
        
        instance = models.EmployeeStatusHistory.objects.get(pk=id)
        
        serializer = serializers.EmployeeStatusHistory(
            instance=instance, 
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        return Response({ 
            "message": "Update Failed!"
        }, status=status.HTTP_400_BAD_REQUEST)

class EducationalBackgroundView:

    # create educational background
    @api_view(['POST'])
    def post(request):
       
        serializer = serializers.EducationalBackground(data=request.data)
       
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Created Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
       
        return Response({
            "message": "Unable to create data."
        }, status=status.HTTP_400_BAD_REQUEST)

    # get educational background
    @api_view(['GET'])
    def list(request, employee):
        
        data = models.EducationalBackground.objects.filter(employee=employee)
        
        serializer = serializers.EducationalBackground(data, many=True)
        return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    
    # get educational background
    @api_view(['GET'])
    def get(request, id):
        
        try:
            data = models.EducationalBackground.objects.get(pk=id)
            serializer = serializers.EducationalBackground(data, many=False)
            
            return Response({  
                "message": "Success!", 
                "total": len(serializer.data),
                "data": serializer.data
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                "message": "Data not found!"
            }, status=status.HTTP_404_NOT_FOUND)
        
    # update educational background
    @api_view(['PATCH'])
    def update(request, id):
        
        instance = models.EducationalBackground.objects.get(pk=id)
        
        serializer = serializers.EducationalBackground(
            instance=instance, 
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Date updated.", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
            
        return Response({
            "message": "Data Update Failed!"
        }, status=status.HTTP_400_BAD_REQUEST)

class EmployeeView:

    # add employee
    @api_view(['POST'])
    def post(request):
        
        try:
            serializer = serializers.Employee(data=request.data)
            
            if serializer.is_valid():   
                serializer.save()   
                return Response({
                    "message": "Employee Added Successfully!", 
                    "data": serializer.data
                }, status=status.HTTP_201_CREATED)
            
            return Response({
                "message": "Bad request."
            }, status=status.HTTP_400_BAD_REQUEST)
       
        except Exception as e:
            return Response({
                "message": str(e)
            },status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # retrieve employee id with position id
    @api_view(['GET'])
    def employee_numbers(request):
        
        data = models.Employee.objects.all()    
        serializer = serializers.EmployeeNumbers(data, many=True)
        
        return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # retrieve employee
    @api_view(['GET'])
    def get(request, employee):
        
        try:
            instance = models.Employee.objects.get(pk=employee)  
            serializer = serializers.Employee(instance, many=False)

            return Response({   
                "message": "Success!",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                "message": "Data not found!"
            }, status=status.HTTP_404_NOT_FOUND)
    
    @api_view(['GET'])  
    def employees_by_year(request, start_year, end_year):

        output={}

        for i in range((end_year - start_year) + 1):
            year = start_year + i
            output[year] = models.Employee.objects.filter(date_hired__icontains=year).count()

        return Response({
            "message": "Success!", 
            "data": output
        }, status=status.HTTP_200_OK)

    # employee list
    @api_view(['GET'])
    def list(request, **kwargs):
        
        data = models.Employee.objects.filter(filters.employee(kwargs)).order_by(*order_list(kwargs.get("order")))
        
        serializer = serializers.Employees(data, many=True)
        data = serializer.data
        for i in range(len(data)):
            try:
                department_head_id = data[i]["position"]["department"]["department_head_id"]
                dept_head = models.Employee.objects.get(id=department_head_id)
                dept_head_serializer = serializers.Employees(dept_head, many=False)
                data[i]["position"]["department"]["department_head"] = dept_head_serializer.data
            except Exception as e:
                data[i]["position"]["department"]["department_head"] = None
            
        return Response({
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # employee names
    @api_view(['GET'])
    def employee_names(request):
        
        data = models.Employee.objects.all()
        serializer = serializers.EmployeeNames(data, many=True)
        
        employees = [];
        
        for employee in serializer.data:
            employees.append({
                "id": employee['id'],
                "name": get_name(employee),
            })
        
        return Response({
            "message": "Success!", 
            "total": len(employees),
            "data": employees
        }, status=status.HTTP_200_OK)


    # retrieve employee work information
    @api_view(['GET'])
    def work_info(request, employee):
        
        try:
            instance = models.Employee.objects.get(pk=employee)  
            serializer = serializers.GetWorkInfo(instance, many=False)
            data = serializer.data
            
            department_head_id = data["position"]["department"]["department_head_id"]
            
            try:
                department_head = models.Employee.objects.get(pk=department_head_id)
                department_head_serializer = serializers.EmployeeName(instance, many=False)
                department_head = department_head_serializer.data
                data["position"]["department"]["department_head"] = department_head
            except Exception as e:
                pass

            return Response({
                "message": "Success!",
                "data": data,
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "message": "Data not found!"
            }, status=status.HTTP_404_NOT_FOUND)
      
    # retrieve employee work information
    @api_view(['GET'])
    def contact_info(request, employee):
        
        try:
            instance = models.Employee.objects.get(pk=employee)  
            serializer = serializers.EmployeeContactInformation(instance, many=False)

            return Response({
                "message": "Success!",
                "data": serializer.data,
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "message": "Data not found!"
            }, status=status.HTTP_404_NOT_FOUND)
          
      
    # generated employee no
    @api_view(['GET'])
    def generated_employee_no(request):
        
        employee_head_count = str(models.Employee.objects.filter(date_hired__icontains=get_year()).count() + 1)
        employee_no = generated_employee_no() + "-" + employee_head_count
        
        return Response({
            "message": "Success!",
            "data": employee_no
        }, status=status.HTTP_201_CREATED)

    # get employee id
    @api_view(['GET'])
    def get_employee_id(request, user):
        
        data = models.Employee.objects.get(user=user)
        
        serializer = serializers.Employees(data, many=False)
        
        return Response({
            "message": "Success!", 
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # get employee status
    @api_view(['GET'])
    def get_employee_status(request, id):
        
        data = models.Employee.objects.get(pk=id)
        
        serializer = serializers.Employee(data, many=False)
        
        return Response({
            "message": "Success!", 
            "data": serializer.data["employee_status"]})

    # get department id
    @api_view(['GET'])
    def get_department_id(request, id):
        
        data = models.Employee.objects.get(pk=id)
        
        serializer = serializers.Employees(data, many=False)
        
        return Response({
            "message": "Success!", 
            "data": serializer.data["position"]["department"]["id"]})

    # get department id
    @api_view(['GET'])
    def get_position_id(request, id):
        
        data = models.Employee.objects.get(pk=id)
        
        serializer = serializers.Employees(data, many=False)
        
        return Response({
            "message": "Success!", 
            "data": serializer.data["position"]["id"]})

    # get employee no
    @api_view(['GET'])
    def get_employee_no(request, id):
        
        data = models.Employee.objects.get(pk=id)
        
        serializer = serializers.Employees(data, many=False)
        return Response(serializer.data["employee_no"])

    # get employee no
    @api_view(['GET'])
    def validate_employee_no(request, employee_no):
       
        if models.Employee.objects.filter(employee_no=employee_no).exists():
            return Response({
                "message": "Employee no exist!"
            }, status=status.HTTP_409_CONFLICT)
       
        return Response({
            "message": "Employee no available"
        }, status=status.HTTP_200_OK)
        
    # total employees
    @api_view(['GET'])
    def total(request, **kwargs):

        data = models.Employee.objects.count()

        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)

    # total employees
    @api_view(['GET'])
    def on_leave(request, **kwargs):

        data = models.Employee.objects.filter(employee_status_id=4).count()
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)

    # list of employee emails
    @api_view(['GET'])
    def emails(request):
       
        data = models.Employee.objects.all(); 
        serializer = serializers.EmployeeEmails(data, many=True)
        return Response({
            "message": "Success!",
            "data": serializer.data,
        }, status=status.HTTP_200_OK)
    
    # validate employee
    @api_view(['POST'])
    def validate(request):
        
        email = request.data["email"]
        employee_email = models.Employee.objects.filter(email=email)
        employee_no = models.Employee.objects.filter(employee_no=request.data["employee_no"])
        user_email = models.User.objects.filter(email=email)
        
        if email is not None and (employee_email.exists() or user_email.exists()):
            return Response({
                "message": "Email already exists"
            }, status=status.HTTP_409_CONFLICT)
      
        elif employee_no.exists():
            return Response({
                "message": "Employee no already exists"
            }, status=status.HTTP_409_CONFLICT)
        
        return Response({
            "message": "Employee No is available!"
        }, status=status.HTTP_200_OK)
    
    # validate employee email
    @api_view(['GET'])
    def validate_email(request, **kwargs):
        
        if models.Employee.objects.filter(
            Q(email=kwargs.get("email")) & 
            ~Q(pk=kwargs.get("employee")) 
        ).exists():
            return Response({
                "message": "Email already exists."
            }, status=status.HTTP_409_CONFLICT)
     
        return Response({
            "message": "Email is available!"
        }, status=status.HTTP_200_OK)

    @api_view(['GET'])
    def employee_no_and_name(request):
        
        data = models.Employee.objects.all()
        serializer = serializers.EmployeeNoAndName(data, many=True)
       
        return Response({
            "message": "Success!",
            "data": serializer.data,
        }, status=status.HTTP_200_OK) 

    # update employee
    @api_view(['PATCH'])
    def update(request, id):
        
        instance = models.Employee.objects.get(pk=id)   

        serializer = serializers.Employee(
            instance=instance, 
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
            
        return Response({
            "message": "Data Update Failed!"
        }, status=status.HTTP_400_BAD_REQUEST)   

    # clear employees
    @api_view(['DELETE'])
    def clear(request):
     
        models.Employee.objects.all().delete()
     
        return Response({ 
            "message": "Employees Cleared."
        }, status=status.HTTP_200_OK)

    @api_view(['GET'])  
    def generate_report(request, column, value, start_date, end_date):

        output={} 
        data = models.Employee.objects.filter(**{ 
            column: value, 
            "date_hired__gte": start_date, 
            "date_hired__lte": end_date
        })
        
        serializer = serializers.Employees(data, many=True)
        data = []

        for i in range(len(serializer.data)):

            employee = serializer.data[i]
            
            data.append({
                "name": get_name(employee),
                "employee_no": employee["employee_no"],
                "employee_type": employee["employee_type"]["name"],
                "position": employee["position"]["title"],
                "department": employee["position"]["department"]["name"],
                "sex": employee["sex"],
                "date_hired": employee["date_hired"],
            })

        return Response({
            "message": "Success!", 
            "data": data
        }, status=status.HTTP_200_OK)


class EquipmentRequestView:

    # create equipment request
    @api_view(['POST'])
    def post(request):
        
        serializer = serializers.EquipmentRequest(data=request.data)
       
        if serializer.is_valid():
            serializer.save()   
            return Response({
                "message": "Add Successfully!"
            }, status=status.HTTP_201_CREATED)
       
        return Response({
            "message": "Failed to add item."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # total equipment requests
    @api_view(['GET'])
    def total(request):
        
        data = models.EquipmentRequest.objects.count()
        
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)
    
     # retrieve equipment requests
    @api_view(['GET'])
    def get(request, id):
        
        data = models.EquipmentRequest.objects.get(pk=id)
        
        serializer = serializers.EquipmentRequest(data, many=data)
        
        return Response({
            "message": "Success", 
            "data": serializer.data
        }, status=status.HTTP_400_BAD_REQUEST)

    # equipment requests 
    @api_view(['GET'])
    def list(request, **kwargs):
        
        try:
            if kwargs.get("search"):
            
                data = models.EquipmentRequest.objects.all()
                serializer = serializers.EquipmentRequest(data, many=True)
            
                for key in serializer.data[0].keys():
                  
                    data = models.EquipmentRequest.objects.filter(**{key + "__icontains": kwargs.get("search")})
                    serializer = serializers.EquipmentRequest(data, many=True)
                  
                    if serializer.data:
                        return Response({ 
                            "message": "Success!", 
                            "total": len(serializer.data),
                            "data": serializer.data
                        }, status=status.HTTP_200_OK)
          
            elif kwargs.get("order"):
                data = models.EquipmentRequest.objects.order_by(kwargs.get("order"))
           
            elif kwargs.get("entry"):
                data = models.EquipmentRequest.objects.all()[:int(kwargs.get("entry"))]
           
            else:
                data = models.EquipmentRequest.objects.all()
           
            serializer = serializers.EquipmentRequest(data, many=True)
            
            return Response({ 
                "message": "Success!", 
                "total": len(serializer.data),
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class EquipmentTypeView:

    # create equipment type
    @api_view(['POST'])
    def post(request):
        
        serializer = serializers.EquipmentType(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Type Created Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            "message": "Failed to Create Type."
        }, status=status.HTTP_400_BAD_REQUEST)

    # total equipment types
    @api_view(['GET'])
    def total(request):
        
        data = models.EquipmentType.objects.count()
        
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)
    
    # retrieve equipment type
    @api_view(['GET'])
    def get(request, id):
        
        data = models.EquipmentType.objects.get(pk=id)
        
        serializer = serializers.EquipmentType(data, many=False)
        
        return Response({
            "message": "Success", 
            "data": serializer.data
        }, status=status.HTTP_200_OK)

     # equipment types
    @api_view(['GET'])
    def list(request, **kwargs):
        
        data = models.EquipmentType.objects.all()
        
        if kwargs.get("search"):
            term = kwargs.get("search")
            data = models.EquipmentType.objects.filter(Q(name__icontains=term) | Q(pk__iexact=term))
        elif kwargs.get("entry"):
            data = models.EquipmentType.objects.all()[:kwargs.get("entry")]
        
        serializer = serializers.EquipmentType(data, many=True)
        
        return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # update equipment type
    @api_view(['PATCH'])
    def update(request, id):
        
        instance = models.EquipmentType.objects.get(pk=id)   
        
        serializer = serializers.EquipmentType(
            instance=instance, 
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
            
        return Response({
            "message": "Update Failed!"
        }, status=status.HTTP_400_BAD_REQUEST)
    
     # delete type
    @api_view(['DELETE'])
    def delete(request, id):
        
        try:
            models.EquipmentType.objects.get(pk=id).delete()
           
            return Response({
                "status": status.HTTP_200_OK, 
                "message": "Deleted Successfully!"
            })
        
        except Exception as e:
            return Response({
                "message": "Data not found!"
            }, status=status.HTTP_404_NOT_FOUND)

class EquipmentRequestView:

    # create equipment request
    @api_view(['POST'])
    def post(request):
        
        serializer = serializers.EquipmentRequest(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
        
            return Response({
                "message": "Request submitted Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            "message": "Failed to Create Type."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # equipment requests
    @api_view(['GET'])
    def list(request, **kwargs):
        
        try:
            if kwargs.get("search"):
        
                serializer = serializers.EquipmentRequest(models.EquipmentRequest.objects.all(), many=True)
        
                for key in serializer.data[0].keys():
        
                    data = models.EquipmentRequest.objects.filter(**{key+ "__icontains": kwargs.get("search")})
                    serializer = serializers.EquipmentRequest(data, many=True)
        
                    if serializer.data:
                        return Response({ 
                            "message": "Success!", 
                            "total": len(serializer.data),
                            "data": serializer.data
                        }, status=status.HTTP_200_OK)
            
            elif kwargs.get("order"):
                data = models.EquipmentRequest.objects.order_by(kwargs.get("order"))
            
            elif kwargs.get("entry"):
                data = models.EquipmentRequest.objects.all()[:int(kwargs.get("entry"))]
            
            else:
                data = models.EquipmentRequest.objects.all()
            
            serializer = serializers.EquipmentRequest(data, many=True)
            
            return Response({ 
                "message": "Success!", 
                "total": len(serializer.data),
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
        
    # retrieve equipment request
    @api_view(['GET'])
    def get(request, id):
        
        data = models.EquipmentRequest.objects.get(pk=id)
        
        serializer = serializers.EquipmentRequest(data, many=False)
        
        return Response({
            "message": "Success", 
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # update equipment request
    @api_view(['PATCH'])
    def update(request, id):
        
        instance = models.EquipmentRequest.objects.get(pk=id)   
        
        serializer = serializers.EquipmentRequest(
            instance=instance, 
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
            
        return Response({
            "message": "Update Failed!"
        }, status=status.HTTP_400_BAD_REQUEST)
    

class EquipmentArticleView:

    # create equipment article
    @api_view(['POST'])
    def post(request):
       
        if models.EquipmentArticle.objects.filter(
            name=request.data["name"], 
            type=request.data["type"]
        ).exists():
            return Response({
                "message": "Article exists."
            }, status=status.HTTP_409_CONFLICT)
        
        serializer = serializers.EquipmentArticle(data=request.data)
      
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Article successfully added.", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            "message": "Failed to Create Type."
        }, status=status.HTTP_400_BAD_REQUEST)

    # total equipment articles
    @api_view(['GET'])
    def total(request):
        
        data = models.EquipmentArticle.objects.count()
        
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)

    # retrieve equipment article
    @api_view(['GET'])
    def get(request, id):
        
        data = models.EquipmentArticle.objects.get(pk=id)
        serializer = serializers.EquipmentArticle(data, many=False)
        
        return Response({
            "message": "Success", 
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    
     # equipment articles
    @api_view(['GET'])
    def list(request, **kwargs):
        
        data = models.EquipmentArticle.objects.all()
        
        if kwargs.get("search"):
            term = kwargs.get("search")
            data = models.EquipmentArticle.objects.filter(Q(name__icontains=term) | Q(pk__iexact=term))
        elif kwargs.get("entry"):
            data = models.EquipmentArticle.objects.all()[:kwargs.get("entry")]
        
        serializer = serializers.EquipmentArticle(data, many=True)
        
        return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # update equipment article
    @api_view(['PATCH'])
    def update(request, id):
        
        instance = models.EquipmentArticle.objects.get(pk=id)   

        serializer = serializers.EquipmentArticle(
            instance=instance, 
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
            
        return Response({
            "message": "Update Failed!"
        }, status=status.HTTP_400_BAD_REQUEST)
    
     # delete type
    @api_view(['DELETE'])
    def delete(request, id):
        
        try:
            models.EquipmentArticle.objects.get(pk=id).delete()
           
            return Response({
                "message": "Deleted Successfully!"
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "message": "Data not found!",
            }, status=status.HTTP_404_NOT_FOUND)


class EquipmentView:

    # create equipment 
    @api_view(['POST'])
    def post(request):
        
        serializer = serializers.Equipment(data=request.data)
        
        if serializer.is_valid():
            serializer.save()   
            return Response({
                "message": "Equipment Successfully Added!", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            "message": "Failed to add equipment"
        }, status=status.HTTP_400_BAD_REQUEST)

    # generate property number
    @api_view(['GET'])
    def property_number(reques):
        
        data = models.Equipment.objects.count() + 1
     
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)
    
    # total equipments
    @api_view(['GET'])
    def total(request):
        equipments = models.Equipment.objects.count()
        return Response(equipments)

    # equipment list
    @api_view(['GET'])
    def list(request, **kwargs):
        
        try:
            if kwargs.get("search"):
             
                serializer = serializers.Equipment(models.Equipment.objects.all(), many=True)
             
                for key in serializer.data[0].keys():
             
                    data = models.Equipment.objects.filter(**{key+ "__icontains": kwargs.get("search")})
                    serializer = serializers.Equipments(data, many=True)
             
                    if serializer.data:
                        return Response({ 
                            "message": "Success!", 
                            "total": len(serializer.data),
                            "data": serializer.data
                        }, status=status.HTTP_200_OK)
            
            elif kwargs.get("order"):
                data = models.Equipment.objects.order_by(kwargs.get("order"))
            
            elif kwargs.get("entry"):
                data = models.Equipment.objects.all()[:int(kwargs.get("entry"))]
            
            else:
                data = models.Equipment.objects.all()
            
            serializer = serializers.Equipments(data, many=True)
            
            return Response({ 
                "message": "Success!", 
                "total": len(serializer.data),
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)   

    # update equipmentc
    @api_view(['PATCH'])
    def update(request, id):
        
        instance = models.Equipment.objects.get(pk=id)   
        
        serializer = serializers.Equipment(
            instance=instance, 
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Item successfully update."
            }, status=status.HTTP_200_OK)
            
        return Response({
            "message": "Item Update Failed!"
        }, status=status.HTTP_400_BAD_REQUEST)

class GovernmentCompanyView:  

    # create government company
    @api_view(['POST'])
    def post(request):
        
        serializer = serializers.GovernmentCompany(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "GovernmentCompany added Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({ 
            "message": "Unable to add government company."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # government company list
    @api_view(['GET'])
    def list(request, **kwargs):
        
        data = models.GovernmentCompany.objects.all()
        
        if kwargs.get("search"):
            term = kwargs.get("search")
            data = models.GovernmentCompany.objects.filter(Q(name__icontains=term) | Q(pk__iexact=term))
        
        elif kwargs.get("entry"):
            data = models.GovernmentCompany.objects[:kwargs.get("entry")]
        
        serializer = serializers.GovernmentCompany(data, many=True)
        
        return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    
    # retrieve government company
    @api_view(['GET'])
    def get(request, id):
        
        try:
            data = models.GovernmentCompany.objects.get(pk=id)
            serializer = serializers.GovernmentCompany(data, many=False)
            
            return Response({  
                "message": "Success!", 
                "total": len(serializer.data),
                "data": serializer.data
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                "message": "Record not found.",
                "data": {}
            }, status=status.HTTP_404_NOT_FOUND)

    # total government companys
    @api_view(['GET'])
    def total(request):
        
        data = models.GovernmentCompany.objects.count()
        
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)

    # update government company
    @api_view(['PATCH'])
    def update(request, id):
        
        instance = models.GovernmentCompany.objects.get(pk=id)
        
        serializer = serializers.GovernmentCompany(
            instance=instance, 
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
            
        return Response({
            "message": "Failed to update government company."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # delete government company
    @api_view(['DELETE'])
    def delete(request, id):
        
        try:
            models.GovernmentCompany.objects.get(pk=id).delete()
            
            return Response({
                "message": "Deleted Successfully!"
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                "message": "Data not found!"
            }, status=status.HTTP_404_NOT_FOUND)


class GovernmentIssuedIDView:  

    # create government issued id
    @api_view(['POST'])
    def post(request):
        
        serializer = serializers.GovernmentIssuedID(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
        
            return Response({ 
                "message": "GovernmentIssuedID added Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({ 
            "message": "Unable to add government issued id."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # government issued id list
    @api_view(['GET'])
    def list(request, **kwargs):
        
        data = models.GovernmentIssuedID.objects.all()
        
        if kwargs.get("search"):
            term = kwargs.get("search")
            data = models.GovernmentIssuedID.objects.filter(
                Q(name__icontains=term) | 
                Q(pk__iexact=term)
            )
        elif kwargs.get("entry"):
            data = models.GovernmentIssuedID.objects[:kwargs.get("entry")]
        
        serializer = serializers.GovernmentIssuedID(data, many=True)
        
        return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    
    # retrieve government issued id
    @api_view(['GET'])
    def get(request, id):
        
        try:
            data = models.GovernmentIssuedID.objects.get(pk=id)
            serializer = serializers.GovernmentIssuedID(data, many=False)
            
            return Response({  
                "message": "Success!", 
                "total": len(serializer.data),
                "data": serializer.data
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                "message": "Record not found.",
                "data": {}
            }, status=status.HTTP_404_NOT_FOUND)

    # total government issued ids
    @api_view(['GET'])
    def total(request):
        
        data = models.GovernmentIssuedID.objects.count()
        
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)

    # update government issued id
    @api_view(['PATCH'])
    def update(request, id):
        
        instance = models.GovernmentIssuedID.objects.get(pk=id)
        
        serializer = serializers.GovernmentIssuedID(
            instance=instance, 
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
            
        return Response({
            "message": "Failed to update government issued id."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # delete government issued id
    @api_view(['DELETE'])
    def delete(request, id):
        
        try:
            models.GovernmentIssuedID.objects.get(pk=id).delete()
           
            return Response({
                "message": "Deleted Successfully!"
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                "message": "Data not found!"
            }, status=status.HTTP_404_NOT_FOUND)

class GroupView:  

    # create group
    @api_view(['POST'])
    def post(request):
        if models.Group.objects.filter(name=request.data["name"]).exists():
            return Response({ 
                "message": "Group already exists."
            }, status=status.HTTP_409_CONFLICT)
        
        serializer = serializers.Group(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Group added Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({ 
                "message": "Unable to add group."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # group list
    @api_view(['GET'])
    def list(request, **kwargs):
        
        data = models.Group.objects.exclude(pk=1)
        
        if kwargs.get("search"):
            term = kwargs.get("search")
            data = models.Group.objects.exclude(pk=1).filter(
                Q(name__icontains=term) | 
                Q(pk__iexact=term)
            )
        elif kwargs.get("entry"):
            data = models.Group.objects.exclude(pk=1)[:kwargs.get("entry")]
        
        serializer = serializers.Group(data, many=True)
        
        return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    
    # retrieve group
    @api_view(['GET'])
    def get(request, id):
        
        try:
            data = models.Group.objects.get(pk=id)
            serializer = serializers.Group(data, many=False)
            
            return Response({  
                "message": "Success!", 
                "total": len(serializer.data),
                "data": serializer.data
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                "message": "Record not found.",
                "data": {}
            }, status=status.HTTP_404_NOT_FOUND)

    # total groups
    @api_view(['GET'])
    def total(request):
        
        data = models.Group.objects.count()
        
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)

    # update group
    @api_view(['PATCH'])
    def update(request, id):
        
        instance = models.Group.objects.get(pk=id)
        
        serializer = serializers.Group(
            instance=instance, 
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
            
        return Response({
            "message": "Failed to update group."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # delete group
    @api_view(['DELETE'])
    def delete(request, id):
        
        try:
            models.Group.objects.get(pk=id).delete()
            
            return Response({
                "message": "Group Deleted Successfully!"
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                "message": "Data not found!"
            }, status=status.HTTP_404_NOT_FOUND)

class GroupPermissionsView:

    # create group permission
    @api_view(['POST'])
    def post(request):
        
        if models.GroupPermissions.objects.filter(
            group=request.data["group"], 
            permission=request.data["permission"]
        ).exists():
            return Response({ 
                "message": "Permission Already Exists."
            }, status=status.HTTP_409_CONFLICT)
        
        serializer = serializers.GroupPermission(data=request.data)
       
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Permission Created Successfully!"
            }, status=status.HTTP_201_CREATED)
        
        return Response({ 
                "message": "Failed to add Role."
        }, status=status.HTTP_400_BAD_REQUEST)

    # total group permissions
    @api_view(['GET'])
    def total(request):
        
        data = models.GroupPermissions.objects.count()
        
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)

    # group permission list
    @api_view(['GET'])
    def list(request, **kwargs):
        
        if kwargs.get("user"):
            group = models.UserGroup.objects.get(user=kwargs.get("user"))
            group_serializer = serializers.UserGroup(group, many=False)
            data = models.GroupPermissions.objects.filter(group=group_serializer.data["group"]).order_by(*{
                "group__id", 
                "permission__id"
            })
        elif kwargs.get("search"):
            term = kwargs.get("search")
            data = models.GroupPermissions.objects.filter(
                Q(group__name__icontains=term) | 
                Q(permission__description__icontains=term)
            )

        elif kwargs.get("entry"):
            data = models.GroupPermissions.objects.all().order_by(*{
                "group__id", 
                "permission__id"
            })[:kwargs.get("entry")]

        elif kwargs.get("order"):
            data = models.GroupPermissions.objects.order_by(kwargs.get("order"))
        else:
            data = models.GroupPermissions.objects.all().order_by(*{
                "group__id", 
                "permission__id"
            })
        
        serializer = serializers.GroupPermissions(data, many=True)
       
        return Response({
            "message": "Success!", 
            "total": len(serializer.data), 
            "data": serializer.data
        }, status=status.HTTP_200_OK)


    # get user group permissions
    @api_view(['GET'])
    def get(request, id):
        
        try:
            data = models.GroupPermissions.objects.get(pk=id)
            serializer = serializers.GroupPermissions(data, many=False)
           
            return Response({
                "message": "Success!",
                "data": serializer.data,
            }, status=status.HTTP_200_OK) 

        except Exception as e:
            return Response({
                "message": str(e),
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # update group permission
    @api_view(['PATCH'])
    def update(request, id):
       
        if models.GroupPermissions.objects.filter(
            group=request.data["group"], 
            permission=request.data["permission"]
        ).exists():
            
            return Response({ 
                "message": "Permission Already Exists."
            }, status=status.HTTP_409_CONFLICT)
        
        instance = models.GroupPermissions.objects.get(pk=id)
        
        serializer = serializers.GroupPermission(
            instance=instance, 
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
            
        return Response({
            "message": "Data Update Failed!"
        }, status=status.HTTP_400_BAD_REQUEST)

    # delete group permission
    @api_view(['DELETE'])
    def delete(request, id):
        
        try:
            models.GroupPermissions.objects.get(pk=id).delete()
           
            return Response({
                "message": "Permission Deleted Successfully!"
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                "message": "Data not found!"
            }, status=status.HTTP_404_NOT_FOUND)

class FatherView:
    
    # create father
    @api_view(['POST'])
    def post(request):
        
        try:
            employee=models.Employee.objects.get(employee_no=request.data["employee"])
            employee_serializer = serializers.Employee(employee, many=False)
            request.data["employee"] = employee_serializer.data["id"]
            serializer = serializers.Father(data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "Updated Successfully!", 
                    "data": serializer.data 
                }, status=status.HTTP_201_CREATED)
           
            return Response({
                "message": "Success!", 
                "data": serializer.data 
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "message": "Data not found!"
            }, status=status.HTTP_404_NOT_FOUND)

    # retrieve father
    @api_view(['GET'])
    def get(request, employee):
        
        try:
            data = models.Father.objects.get(employee=employee)
            serializer = serializers.Father(data, many=False)
            
            return Response({ 
                "message": "Success!", 
                "data": serializer.data 
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                "message": "Record not found.",
                "data": {}
            }, status=status.HTTP_404_NOT_FOUND)
        
    # update father
    @api_view(['PATCH'])
    def update(request, id):
        
        instance = models.Father.objects.get(pk=id)
        
        serializer = serializers.Father(
            instance=instance, 
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Updated Successfully!", 
                "data": serializer.data 
            }, status=status.HTTP_200_OK)
        
        return Response({
            "message": "Success!", 
            "data": serializer.data 
        }, status=status.HTTP_200_OK)

    
class FileView:

    # upload file
    @api_view(['POST'])
    def post(request):
        
        try:
            serializer = serializers.File(data=request.data)
        
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "File Uploaded Successfully!", 
                    "data": serializer.data
                }, status=status.HTTP_201_CREATED)
        
            return Response({
                "message": "Failed to upload file."
            }, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({
                "message": "Data not found!"
            }, status=status.HTTP_404_NOT_FOUND)
        
    # retrieve user files
    @api_view(['GET'])
    def list(request):
        
        data = models.File.objects.all()
        
        serializer = serializers.File(data, many=True)
      
        return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # total user files
    @api_view(['GET'])
    def total(request, username):
        
        data = models.File.objects.filter(user__username=username).count()

        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)
        
    # retrieve user file
    @api_view(['GET'])
    def get(request, **kwargs):
        
        try:
            username = kwargs.get("username")   
            search_term = kwargs.get("search_term")
            order = kwargs.get("order")
            entry = kwargs.get("entry")
            
            if kwargs.get("search"):
               
                serializer = serializers.File(models.File.objects.all(), many=True)
               
                for key in serializer.data[0].keys():
                    
                    if key != "user":
                    
                        data = models.File.objects.filter(**{
                            "user__username": username, 
                            key + "__icontains": search_term
                        })

                        serializer = serializers.File(data, many=True)
                    
                        if serializer.data:
                            return Response({ 
                                "message": "Success!", 
                                "total": len(serializer.data),
                                "data": serializer.data
                            }, status=status.HTTP_200_OK)
            
            elif kwargs.get("order"):
                data = models.File.objects.filter(user__username=username).order_by(order)

            elif kwargs.get("entry"):
                data = models.File.objects.filter(user__username=username)[:int(entry)]

            else:
                data = models.File.objects.filter(user__username=username)
            
            serializer = serializers.File(data, many=True)
            
            return Response({ 
                "message": "Success!", 
                "total": len(serializer.data),
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # update user file
    @api_view(['PATCH'])
    def update(request, id):
        
        instance = models.File.objects.get(pk=id)
        
        serializer = serializers.File(
            instance=instance, 
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        return Response({
            "message": "No changes made!",
            "data": request.data
        }, status=status.HTTP_304_NOT_MODIFIED)

    # delete file
    @api_view(['DELETE'])
    def delete(request, id):
       
        models.File.objects.get(pk=id).delete()
        
        return Response({
            "message": "Deleted Successfully!"
        }, status=status.HTTP_200_OK)
        
    # delete all files
    @api_view(['DELETE'])
    def clear(request):
       
        models.File.objects.all().delete()
        
        return Response({
            "message": "Files deleted Successfully!"
        }, status=status.HTTP_200_OK)
    
class NameExtensionView:  

    # create name extension
    @api_view(['POST'])
    def post(request):
        
        if models.NameExtension.objects.filter(name=request.data["name"]).exists():
            return Response({ 
                "message": "Name extension already exists."
            }, status=status.HTTP_409_CONFLICT)

        serializer = serializers.NameExtension(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Name extension added Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({ 
            "message": "Failed to add name extension."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # name extension list
    @api_view(['GET'])
    def list(request, **kwargs):
        
        data = models.NameExtension.objects.all()
       
        if kwargs.get("search"):
            term = kwargs.get("search")
            data = models.NameExtension.objects.filter(
                Q(__icontains=term) | 
                Q(pk__iexact=term)
            )
       
        elif kwargs.get("entry"):
            data = models.NameExtension.objects.all()[:kwargs.get("entry")]
       
        serializer = serializers.NameExtension(data, many=True)
       
        return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # total name extensions
    @api_view(['GET'])
    def total(request):
        
        data = models.NameExtension.objects.count()
        
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)
    
    # retrieve name extension
    @api_view(['GET'])
    def get(request, id):
        
        try:
            data = models.NameExtension.objects.get(pk=id)
            serializer = serializers.NameExtension(data, many=False)
            
            return Response({  
                "message": "Success!", 
                "total": len(serializer.data),
                "data": serializer.data
            }, status=status.HTTP_200_OK)
       
        except Exception as e:
            return Response({
                "message": "Record not found.",
                "data": {}
            }, status=status.HTTP_404_NOT_FOUND)
        
    # update name extension
    @api_view(['PATCH'])
    def update(request, id):
       
        instance = models.NameExtension.objects.get(pk=id)
        
        serializer = serializers.NameExtension(
            instance=instance, 
            data=request.data
        )
       
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
       
        return Response({ 
            "message": "Update Failed!"
        }, status=status.HTTP_400_BAD_REQUEST)

    # delete name extension
    @api_view(['DELETE'])
    def delete(request, id):

        models.NameExtension.objects.get(pk=id).delete()

        return Response({
            "message": "Name extension Deleted Successfully!"
        }, status=status.HTTP_200_OK)


class NotificationView:
    
    # create notification
    @api_view(['POST'])
    def post(request):
        
        serializer = serializers.Notification(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Notification Created Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({ 
            "message": "Failed to Create Notification."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # notification list
    @api_view(['GET'])
    def list(request, user):
        
        if(user is None):
            data = models.Notification.objects.filter(visible_to="")
        else:
            data = models.Notification.objects.filter(
                Q(visible_to__icontains=user) | 
                Q(visible_to="")
            )

        serializer = serializers.Notification(data, many=True)

        return Response({
            "message": "Success!",
            "total": len(serializer.data),
            "data": serializer.data,
        }, status=status.HTTP_200_OK)
    
    # update notification
    @api_view(['PATCH'])
    def update(request, id):
      
        instance = models.Notification.objects.get(pk=id) 
        
        serializer = serializers.Notification(
            instance=instance, 
            data=request.data
        )
      
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Update Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        return Response({ 
            "message": "Update Failed!"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # delete notification
    @api_view(['DELETE'])
    def delete(request, id):
       
        models.Notification.objects.get(pk=id).delete()
       
        return Response({
            "message": "Deleted Successfully!"
        }, status=status.HTTP_200_OK)
    
    # clear notificiation
    @api_view(['DELETE'])
    def clear(request, user):
      
        models.Notification.objects.filter(user__username=user).delete()
      
        return Response({
            "message": "Deleted successfully!"
        }, status=status.HTTP_200_OK)
    
class CountryView:  

    # create country
    @api_view(['POST'])
    def post(request):
      
        serializer = serializers.Country(data=request.data)
      
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Country Created Successfully!",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
      
        return Response({ 
            "message": "Unable to add country."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # country list
    @api_view(['GET'])
    def list(request, **kwargs):
        
        data = models.Country.objects.all()
        
        if kwargs.get("search"):

            term = kwargs.get("search")
            
            data = models.Country.objects.filter(
                Q(name__icontains=term) | 
                Q(pk__iexact=term)
            )
        
        elif kwargs.get("entry"):
            data = models.Country.objects.all()[:kwargs.get("entry")]
        
        serializer = serializers.Country(data, many=True)
     
        return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    
    # retrieve country
    @api_view(['GET'])
    def get(request, id):
        
        try:
            data = models.Country.objects.get(pk=id)
            serializer = serializers.Country(data, many=False)
            
            return Response({  
                "message": "Success!", 
                "total": len(serializer.data),
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                "message": "Record not found.",
                "data": {}
            }, status=status.HTTP_404_NOT_FOUND)

    # total countries
    @api_view(['GET'])
    def total(request):
        
        data = models.Country.objects.count()
     
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)

    # update country
    @api_view(['PATCH'])
    def update(request, id):
       
        instance = models.Country.objects.get(pk=id)
        
        serializer = serializers.Country(
            instance=instance, 
            data=request.data
        )
       
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
       
        return Response({
            "message": "Failed to update country."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # delete country
    @api_view(['DELETE'])
    def delete(request, id):
        
        try:
            models.Country.objects.get(pk=id).delete()
          
            return Response({
                "message": "Country Deleted Successfully!"
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                "message": "Data not found!"
            }, status=status.HTTP_404_NOT_FOUND)

    
class ConversationReplyView:
    
    # create conversation reply
    @api_view(['POST'])
    def post(request):
        
        serializer = serializers.ConversationReply(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Messaged sent.", 
                "data": serializer.data 
            }, status=status.HTTP_201_CREATED)

        return Response({ 
            "message": "Failed to send message."
        }, status=status.HTTP_400_BAD_REQUEST)
    
class ConversationView:
    
    # create chat
    @api_view(['POST'])
    def post(request):

        serializer = serializers.Conversation(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Chat Created Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({ 
            "message": "Failed to Create Chat."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # check conversation
    @api_view(['GET'])
    def get(request, sender, reciever):

        if models.Conversation.objects.filter(
            sender=sender, 
            reciever=reciever
        ).exists():
            return Response({
                "message": "Conversation exists!"
            }, status=status.HTTP_200_OK)

        return Response({
            "message": "Conversation does not exist!"
        }, status=status.HTTP_404_NOT_FOUND)
    
    # conversation list
    @api_view(['GET'])
    def list(request, user):

        data = models.Conversation.objects.filter(
            Q(sender=user) | 
            Q(reciever=user)
        )

        serializer = serializers.Conversation(data, many=True)
        conversation = serializer.data
        data = []
        
        for i in range(len(conversation)):
            try:
                conversation_id = serializer.data[i]["id"]
                newData = models.ConversationReply.objects.filter(conversation=conversation_id).order_by("-date_sent")
                serializer = serializers.ConversationReply(newData, many=True)
               
                data.append({
                  "conversation": conversation[i]["id"],
                   "replies": serializer.data
                })
            
            except Exception as e:
                pass
        
        return Response({
            "message": "Success!",
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)
        
    
class JobHistoryView:

    # create job history
    @api_view(['POST'])
    def post(request):

        try:
            serializer = serializers.JobHistory(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "Job history saved Successfully!", 
                    "data": serializer.data
                }, status=status.HTTP_201_CREATED)

            return Response({
                "message": "Failed to save job history."
            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({
                "message": "Data not found!"
            }, status=status.HTTP_404_NOT_FOUND)
        
    
    # job history list
    @api_view(['GET'])
    def list(request):
        
        data = models.JobHistory.objects.all()
        serializer = serializers.JobHistory(data, many=True)

        return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    
    # employees by office
    @api_view(['GET'])
    def employees_by_office(request, username):
        
        data = models.User.objects.get(username=username)  
        office = serializers.User(data, many=False).data["office"]
        data = models.JobHistory.objects.filter(Q(office=office))  
        serializer = serializers.EmployeeByOffice(data, many=True)
        data = []
        
        for item in serializer.data:
            data.append(item["employee"])
        
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)
    
    # employees by supervisor
    @api_view(['GET'])
    def employees_by_supervisor(request, supervisor):
        
        data = models.JobHistory.objects.filter(supervisor_id=supervisor, end_date__gte=date.get_current_date())  
        serializer = serializers.JobHistories(data, many=True)
        data = []
        jobhistory = serializer.data
        
        for i in range(len(jobhistory)):
            data.append({
              "id": jobhistory[i]["employee"]["id"],  
              "name": get_name(jobhistory[i]["employee"]) + " ("+ jobhistory[i]["employee"]["employee_no"] +")"  
            })
            
        return Response({
            "message": "Success!",
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    
    # retrieve job history
    @api_view(['GET'])
    def get(request, **kwargs):
        
        try:
            employee_no = kwargs.get("employee_no")
        
            if employee_no:
                data = models.JobHistory.objects.get(employee__employee_no=employee_no)
            else:
                data = models.JobHistory.objects.get(pk=kwargs.get("id"))
        
            serializer = serializers.JobHistories(data, many=False)
            
            return Response({  
                "message": "Success!", 
                "total": len(serializer.data),
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                "message": "Data not found!"
            }, status=status.HTTP_404_NOT_FOUND)

    
    # retrieve employee id with job id
    @api_view(['GET'])
    def employee_id(request, position):
        
        try:
            data = models.JobHistory.objects.get(position=position)
            serializer = serializers.JobHistories(data, many=False)
        
            data={
                "id": serializer.data["employee"]["id"],
                "name": get_name(serializer.data["employee"]),
            }
        
            return Response({
                "message": "Success!",
                "total": len(serializer.data),
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
            "message": "Employee not found."
        }, status=status.HTTP_404_NOT_FOUND)
    
    # retrieve employee position
    @api_view(['GET'])
    def retrieve_position_title(request, employee):
        
        try:
            data = models.JobHistory.objects.get(employee=employee)
            serializer = serializers.JobHistories(data, many=False)
        
            return Response({
                "message": "Success", 
                "data": serializer.data["position"]["title"]
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                "message": date.get_current_date()
            }, status=status.HTTP_404_NOT_FOUND)


    # municipal officials
    @api_view(['GET'])
    def municipal_officials(request):

        try:
            data = models.JobHistory.objects.filter(is_staff=False)
            serializer = serializers.JobHistory(data, many=True)

            if serializer: 
                return Response({
                    "status": status.HTTP_200_OK, 
                    "message": "Data Retrieved!", 
                    "data": serializer.data
                })
          
            else: 
                return Response({
                    "status": status.HTTP_200_OK, 
                    "message": "No Data Found!", 
                    "data": serializer.data
                })

        except Exception as e:
            return Response({
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR, 
                "message": str(e)
            })

    # total job history
    @api_view(['GET'])
    def total(request):
        return Response(models.JobHistory.objects.count())

    # update job history
    @api_view(['PATCH'])
    def update(request, id):

        instance = models.JobHistory.objects.get(pk=id) 
        
        serializer = serializers.JobHistory(
            instance=instance, 
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Update Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        return Response({ 
            "message": "Update Failed!"
        }, status=status.HTTP_400_BAD_REQUEST)   
    
class LeaveTypeView:  

    @api_view(['POST'])
    def post(request):

        serializer = serializers.LeaveType(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Create Successfully!", 
                "data" : serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({
            "message": "Bad request"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['GET'])
    def list(request, **kwargs):

        sex = kwargs.get("sex")
    
        if sex is not None:
            data = models.LeaveType.objects.filter(
                Q(sex=sex) | 
                Q(sex=None)
            ).order_by("name")
        else:
            data = models.LeaveType.objects.all().order_by("name")

        serializer = serializers.LeaveType(data, many=True)

        return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    @api_view(['GET'])
    def verify(request, name):

        if models.LeaveType.objects.filter(name=name).exists():
            return Response({
                "message": "Leave Type already exists!"
            }, status=status.HTTP_409_CONFLICT)

        return Response({
            "message": ""
        }, status=status.HTTP_200_OK)

    # total leave types
    @api_view(['GET'])
    def total(request):
      
        data = models.LeaveType.objects.count()
      
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)
    
    # retrieve leave type
    @api_view(['GET'])
    def get(request, id):
       
        data = models.LeaveType.objects.get(pk=id)
        
        serializer = serializers.LeaveType(data, many=False)
      
        return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)
        
    # update leave type
    @api_view(['PATCH'])
    def update(request, id):
       
        instance = models.LeaveType.objects.get(pk=id)
        
        serializer = serializers.LeaveType(
            instance=instance, 
            data=request.data
        )
       
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        return Response({ 
            "message": "Update Failed!"
        }, status=status.HTTP_400_BAD_REQUEST)

    # delete leave type
    @api_view(['DELETE'])
    def delete(request, id):
        
        models.LeaveType.objects.get(pk=id).delete()
        
        return Response({
            "message": "Deleted Successfully!"
        }, status=status.HTTP_200_OK)

class LeaveDetailOptionView:  

    # create leave detial option
    @api_view(['POST'])
    def post(request):
       
        serializer = serializers.LeaveDetailOption(data=request.data)
       
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Created Successfully!", 
                "data" : serializer.data
            }, status=status.HTTP_201_CREATED)
       
        return Response({
            "message": "Bad request"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['GET'])
    def list(request):
       
        data = models.LeaveDetailOption.objects.order_by("name")
        
        serializer = serializers.LeaveDetailOption(data, many=True)
        return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    @api_view(['GET'])
    def verify(request, name):
       
        if models.LeaveDetailOption.objects.filter(name=name).exists():
            return Response({
                "message": "Leave option already exists!"
            }, status=status.HTTP_409_CONFLICT)
       
        return Response({
            "message": ""
        }, status=status.HTTP_200_OK)

    # total leave types
    @api_view(['GET'])
    def total(request):
        
        data = models.LeaveDetailOption.objects.count()
        
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)
    
    # retrieve leave detail option
    @api_view(['GET'])
    def get(request, id):
        
        data = models.LeaveDetailOption.objects.get(pk=id)
        
        serializer = serializers.LeaveDetailOption(data, many=False)
        
        return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)
        
    # update leave detail option
    @api_view(['PATCH'])
    def update(request, id):
        
        instance = models.LeaveDetailOption.objects.get(pk=id)
        
        serializer = serializers.LeaveDetailOption(
            instance=instance, 
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
            
        return Response({ 
            "message": "Update Failed!"
        }, status=status.HTTP_400_BAD_REQUEST)

    # delete leave detail option
    @api_view(['DELETE'])
    def delete(request, id):
      
        models.LeaveDetailOption.objects.get(pk=id).delete()
      
        return Response({
            "message": "Deleted Successfully!"
        }, status=status.HTTP_200_OK)
   

class LeaveBalanceView:  

    # create leave balance
    @api_view(['POST'])
    def post(request):
       
        serializer = serializers.LeaveBalance(data=request.data)
       
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Balance Created Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
       
        return Response({
            "message": "Bad request"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # leave balances
    @api_view(['GET'])
    def list(request):
        
        data = models.LeaveBalance.objects.order_by("employee__sur_name",)
        
        serializer = serializers.LeaveBalance(data, many=True)
        
        return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # total leave balances
    @api_view(['GET'])
    def total(request):
        
        data = models.LeaveBalance.objects.count()
        
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)
    
    # retrieve leave balance
    @api_view(['GET'])
    def get(request, id):
        
        data = models.LeaveBalance.objects.get(pk=id)
        
        serializer = serializers.LeaveBalance(data, many=False)
        
        return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # retrieve leave balance
    @api_view(['GET'])
    def available_leave(request, employee, leave_type):
        
        try:
            data = models.LeaveBalance.objects.get(employee=employee, leave_type=leave_type)
            serializer = serializers.LeaveBalance(data, many=False)
        
            return Response({
                "message": "Success!", 
                "data": serializer.data["available"]
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                "message": "Data not found!"
            }, status=status.HTTP_404_NOT_FOUND)
        
    # update leave balance
    @api_view(['PATCH'])
    def update(request, id):

        instance = models.LeaveBalance.objects.get(pk=id)
        
        serializer = serializers.LeaveBalance(
            instance=instance, 
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        return Response({ 
            "message": "Update Failed!"
        }, status=status.HTTP_400_BAD_REQUEST)

    # delete leave balance
    @api_view(['DELETE'])
    def delete(request, id):

        models.LeaveBalance.objects.get(pk=id).delete()
        
        return Response({
            "message": "Deleted Successfully!"
        }, status=status.HTTP_200_OK)
        
class LocationView:  

    # create location
    @api_view(['POST'])
    def post(request):

        serializer = serializers.Location(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Location Created Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({
            "message": "Unable to add location."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # location list
    @api_view(['GET'])
    def list(request, **kwargs):

        data = models.Location.objects.all()

        if kwargs.get("search"):
            term = kwargs.get("search")
            data = models.Location.objects.filter(
                Q(name__icontains=term) | 
                Q(pk__iexact=term)
            )
        elif kwargs.get("entry"):
            data = models.Location.objects.all()[:kwargs.get("entry")]

        serializer = serializers.Locations(data, many=True)

        return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    
    # retrieve location
    @api_view(['GET'])
    def get(request, id):

        try:
            data = models.Location.objects.get(pk=id)
            serializer = serializers.Location(data, many=False)
       
            return Response({ 
                "message": "Success!", 
                "total": len(serializer.data),
                "data": serializer.data
            }, status=status.HTTP_200_OK)
       
        except Exception as e:
            return Response({
                "message": "Record not found.",
                "data": {}
            }, status=status.HTTP_404_NOT_FOUND)

    # total countries
    @api_view(['GET'])
    def total(request):
        
        data = models.Location.objects.count()
        
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)

    # update location
    @api_view(['PATCH'])
    def update(request, id):
        
        instance = models.Location.objects.get(pk=id)
        
        serializer = serializers.Location(
            instance=instance, 
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        return Response({ 
            "message": "Failed to update location."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # delete location
    @api_view(['DELETE'])
    def delete(request, id):
        
        try:
            models.Location.objects.get(pk=id).delete()
        
            return Response({
                "message": "Location Deleted Successfully!"
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                "message": "Data not found!"
            }, status=status.HTTP_404_NOT_FOUND)
        

class LoginHistoryView:

    # create login history
    @api_view(['POST'])
    def post(request):
        
        username = request.data["username"]
        user = serializers.Users(instance=models.User.objects.get(username=username), many=False)
        userid = user.data["id"]
        
        serializer = serializers.LoginHistory(data={
            "user": userid,
            "login": date.get_datetime(),
            "ip_address": request.META.get("REMOTE_ADDR"),
            "browser": request.user_agent.browser.family + " " + request.user_agent.browser.version_string,
            "device": get_device(request),
        }, many=False)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response({
            "message": "Success!", 
            "data": serializer.data 
        }, status=status.HTTP_200_OK)


    # login history list 
    @api_view(['GET'])
    def list(request, **kwargs):
        
        try:
            if kwargs.get("search"):
                data = models.LoginHistory.objects.filter(filters.LoginHistory(kwargs.get("search")))
            else:
                data = models.LoginHistory.objects.order_by(*order_list(kwargs.get("order")))[:kwargs.get("entry")]
        
            serializer = serializers.LoginHistories(data, many=True)
            
            return Response({ 
                "message": "Success!", 
                "total": len(serializer.data),
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # total login history 
    @api_view(['GET'])
    def total(request, **kwargs):

        data = models.LoginHistory.objects.count()

        if kwargs: 
            data = models.LoginHistory.objects.filter(user__username=kwargs.get("username")).count()

        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)

    # update login history
    @api_view(['PATCH'])
    def update(request, login_id):
        
        instance = models.LoginHistory.objects.get(pk=login_id)
        login = serializers.LoginHistories(instance, many=False).data["login"]
        logout = date.get_datetime()

        serializer = serializers.LoginHistory(instance=instance, data= { 
            "logout": logout,
            "duration": get_duration(login, logout)
        })

        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Success!", 
                "total": len(serializer.data),
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        return Response({
            "message": "Success!", 
            "data": serializer.data 
        }, status=status.HTTP_200_OK)


    @api_view(['DELETE'])
    def clear(request):

        if models.LoginHistory.objects.all().delete():
            return Response({
                "message": "Deleted successfully!"
            }, status=status.HTTP_200_OK)

class EmployeeLeaveView:

    # create leave
    @api_view(['POST'])
    def post(request):

        try:
            serializer = serializers.EmployeeLeave(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "Leave Application Submitted!","data": serializer.data
                }, status=status.HTTP_201_CREATED)
            
            return Response({
                "message": "Failed to create leave."
            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({
                "message": "Data not found!"
            }, status=status.HTTP_404_NOT_FOUND)

    # total leave 
    @api_view(['GET'])
    def total(request, **kwargs):
       
        if kwargs.get("employee"): 
            data = models.EmployeeLeave.objects.filter(employee=kwargs.get("employee")).count()
        elif kwargs.get("department_head_id"): 
            data = models.EmployeeLeave.objects.filter(
                employee__position__department_id__department_head_id=kwargs.get("department_head_id")
            ).count()
        else:
            data = models.EmployeeLeave.objects.count()

        return Response({
            "message": "Success!",
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)

     # days on leave
    @api_view(['GET'])
    def days_on_leave(request, employee):
        
        data = models.EmployeeLeave.objects.filter(
            employee=employee, 
            supervisor_remarks=1, 
            hr_remarks=1
        ).order_by("id").count()

        return Response({
            "message": "Success!",
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # leave list
    @api_view(['GET'])
    def list(request, **kwargs):
        
        try:
            data = models.EmployeeLeave.objects.filter(filters.leave(kwargs)).order_by(*order_list(kwargs.get("order")))
        except Exception as e:
            data = models.EmployeeLeave.objects.all().order_by(*order_list(kwargs.get("order")))
        
        serializer = serializers.EmployeeLeaves(data, many=True)
        
        return Response({
            "message": "Success!", 
            "total": len(serializer.data), 
            "data": serializer.data
        }, status=status.HTTP_200_OK)


    # get employee leave
    @api_view(['GET'])
    def get(request, id):
        
        data = models.EmployeeLeave.objects.get(pk=id)
        
        serializer = serializers.EmployeeLeave(data, many=False)
        
        return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # update leave
    @api_view(['PATCH'])
    def update(request, id):
        
        leave = models.EmployeeLeave.objects.get(pk=id)
        
        serializer = serializers.EmployeeLeave(instance=leave, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)

    # approve leave
    @api_view(['PATCH'])
    def approve(request, id):
        
        try:
            leave = models.EmployeeLeave.objects.get(pk=id)
            serializer = serializers.EmployeeLeave(instance=leave, data=request.data)
        
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "Leave Successfully Approved!", 
                    "data": serializer.data
                }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                "message": "Data not found!"
            }, status=status.HTTP_404_NOT_FOUND)

    # decline leave
    @api_view(['PATCH'])
    def decline(request, id):
        
        try:
            leave = models.EmployeeLeave.objects.get(pk=id)
            serializer = serializers.EmployeeLeave(instance=leave, data=request.data["data"])
        
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "Leave Declined Successfully!", 
                    "data": serializer.data
                }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                "message": "Data not found!"
            }, status=status.HTTP_404_NOT_FOUND)
    
    # delete leave
    @api_view(['DELETE'])
    def delete(request, id):
      
        models.EmployeeLeave.objects.get(pk=id).delete()
       
        return Response({
            "message": "Deleted successfully!"
        }, status=status.HTTP_200_OK)

class DepartmentFileView:

    # upload office file
    @api_view(['POST'])
    def post(request):
        
        try:
            serializer = serializers.DepartmentFile(data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "File Uploaded Successfully!", 
                    "data": serializer.data
                }, status=status.HTTP_201_CREATED)
            
            return Response({
                "message": "Failed to upload file."
            }, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({
                "message": "Data not found!"
            }, status=status.HTTP_404_NOT_FOUND)
        
    # retrieve department files
    @api_view(['GET'])
    def list(request):
        
        data = models.DepartmentFile.objects.all()
        serializer = serializers.DepartmentFile(data, many=True)
        
        return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # total department files
    @api_view(['GET'])
    def total(request, **kwargs):
        
        try:
            data = models.DepartmentFile.objects.count()
            
            if kwargs.get("office"):
                data = models.DepartmentFile.objects.filter(pk=kwargs.get("office")).count()
                
            return Response({
                "message": "Success!",
                "data": data
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                "message": "Data not found!"
            }, status=status.HTTP_404_NOT_FOUND)
        
    # retrieve user files
    @api_view(['GET'])
    def get(request, **kwargs):
        
        try:
            office = kwargs.get("office")
            search_term = kwargs.get("search_term")
            order = kwargs.get("order")
            entry = kwargs.get("entry")

            if search_term:
               
                serializer = serializers.DepartmentFile(models.DepartmentFile.objects.all(), many=True)
               
                for key in serializer.data[0].keys():
               
                    if key == "office":
               
                        data = models.DepartmentFile.objects.filter(**{
                            "office": office, 
                            key + "__icontains": search_term
                        })

                        serializer = serializers.DepartmentFile(data, many=True)
               
                        if serializer.data:
                            return Response({ 
                                "message": "Success!", 
                                "total": len(serializer.data),
                                "data": serializer.data
                            }, status=status.HTTP_200_OK)

            elif kwargs.get("order"):
                data = models.DepartmentFile.objects.filter(office=office).order_by(order)
            elif kwargs.get("entry"):
                data = models.DepartmentFile.objects.filter(office=office)[:int(entry)]
            else:
                data = models.DepartmentFile.objects.filter(office=office)

            serializer = serializers.DepartmentFile(data, many=True)
            
            return Response({ 
                "message": "Success!", 
                "total": len(serializer.data),
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # delete department file
    @api_view(['DELETE'])
    def delete(request, id):
        
        try:
            models.DepartmentFile.objects.get(pk=id).delete()
            
            return Response({
                "message": "File Deleted Successfully!"
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                "message": "Data not found!"
            }, status=status.HTTP_404_NOT_FOUND)
        
    # delete all files
    @api_view(['DELETE'])
    def clear(request):
        
        models.DepartmentFile.objects.all().delete()
        
        return Response({
            "message": "File deleted."
        }, status=status.HTTP_200_OK)
    
class OfficeSupplyRequestView:

    # create office supply request
    @api_view(['POST'])
    def post(request):
        
        serializer = serializers.OfficeSupplyRequest(data=request.data)
        
        if serializer.is_valid():
            serializer.save()   
            return Response({
                "message": "Request Sent!"
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            "message": "Failed to add item."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # total office supply requests
    @api_view(['GET'])
    def total(request):
        
        data = models.OfficeSupplyRequest.objects.count()
        
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)
    
    # retrieve office supply requests
    @api_view(['GET'])
    def get(request, id):
        
        data = models.OfficeSupplyRequest.objects.get(pk=id)
        
        serializer = serializers.OfficeSupplyRequest(data, many=data)
        
        return Response({
            "message": "Success", 
            "data": serializer.data
        }, status=status.HTTP_400_BAD_REQUEST)

    # office supply requests 
    @api_view(['GET'])
    def list(request, **kwargs):
        
        try:
            if kwargs.get("employee"):
                data = models.OfficeSupplyRequest.objects.filter(requested_by=kwargs.get("employee"))

            elif kwargs.get("search"):

                data = models.OfficeSupplyRequest.objects.all()
                serializer = serializers.OfficeSupplyRequest(data, many=True)
              
                for key in serializer.data[0].keys():
              
                    data = models.OfficeSupplyRequest.objects.filter(**{key + "__icontains": kwargs.get("search")})
                    serializer = serializers.OfficeSupplyRequest(data, many=True)
              
                    if serializer.data:
                        return Response({ 
                            "message": "Success!", 
                            "total": len(serializer.data),
                            "data": serializer.data
                        }, status=status.HTTP_200_OK)
           
            elif kwargs.get("order"):
                data = models.OfficeSupplyRequest.objects.order_by(kwargs.get("order"))
            
            elif kwargs.get("entry"):
                data = models.OfficeSupplyRequest.objects.all()[:int(kwargs.get("entry"))]
            
            else:
                data = models.OfficeSupplyRequest.objects.all()
            
            serializer = serializers.OfficeSupplyRequest(data, many=True)
            
            return Response({
                "message": "Success", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # update office supply request
    @api_view(['PATCH'])
    def update(request, id):
        
        instance = models.OfficeSupplyRequest.objects.get(pk=id)
        
        serializer = serializers.OfficeSupplyRequest(
            instance=instance, 
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
            
        return Response({
            "message": "Update Failed!"
        }, status=status.HTTP_400_BAD_REQUEST)

    # approve office supply request
    @api_view(['PATCH'])
    def approve(request, id):
        
        instance = models.OfficeSupplyRequest.objects.get(pk=id)
        
        serializer = serializers.OfficeSupplyRequest(instance=instance, data={
            "is_approved": 1
        })
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Request Successfully Approved!", 
            "data": serializer.data
            }, status=status.HTTP_200_OK)
            
        return Response({
            "message": "Update Failed!"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # decline office supply request
    @api_view(['PATCH'])
    def decline(request, id):
        
        instance = models.OfficeSupplyRequest.objects.get(pk=id)
        
        serializer = serializers.OfficeSupplyRequest(instance=instance, data={
            "is_approved": -1
        })
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Request Declined!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
            
        return Response({
            "message": "Update Failed!"
        }, status=status.HTTP_400_BAD_REQUEST)


    # delete office supply requests
    @api_view(['DELETE'])
    def delete(request):
       
        models.OfficeSupplyRequest.objects.all().delete()
       
        return Response({
            "message": "Deleted Successfully!"
        }, status=status.HTTP_200_OK)

class OfficeSupplyTypeView:

    # create office supply type
    @api_view(['POST'])
    def post(request):
        if models.OfficeSupplyType.objects.filter(name=request.data["name"]).exists():
            return Response({
            "message": "Type already exists."
        }, status=status.HTTP_409_CONFLICT)
        
        serializer = serializers.OfficeSupplyType(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Type added Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            "message": "Failed to add type."
        }, status=status.HTTP_400_BAD_REQUEST)

    # total office supply transfertypes
    @api_view(['GET'])
    def total(request):
        
        data = models.OfficeSupplyType.objects.count()
       
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)
 
    # retrieve supply type
    @api_view(['GET'])
    def get(request, id):
        
        data = models.OfficeSupplyType.objects.get(pk=id)
        serializer = serializers.OfficeSupplyType(data, many=False)
        
        return Response({
            "message": "Success", 
            "data": serializer.data
        }, status=status.HTTP_200_OK)

     # office supply transfertypes
    @api_view(['GET'])
    def list(request, **kwargs):
        
        data = models.OfficeSupplyType.objects.all()
    
        if kwargs.get("search"):
            term = kwargs.get("search")
            data = models.OfficeSupplyType.objects.filter(Q(name__icontains=term) | Q(pk__iexact=term))
        elif kwargs.get("entry"):
            data = models.OfficeSupplyType.objects.all()[:kwargs.get("entry")]
       
        serializer = serializers.OfficeSupplyType(data, many=True)
       
        return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # update office supply transfertype
    @api_view(['PATCH'])
    def update(request, id):
        
        instance = models.OfficeSupplyType.objects.get(pk=id)   
        
        serializer = serializers.OfficeSupplyType(
            instance=instance, 
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
            
        return Response({
            "message": "Update Failed!"
        }, status=status.HTTP_400_BAD_REQUEST)
    
     # delete type
    @api_view(['DELETE'])
    def delete(request, id):
      
        models.OfficeSupplyType.objects.get(pk=id).delete()
      
        return Response({
            "Type Deleted Successfully!"
        }, status=status.HTTP_200_OK)

class OfficeSupplyTransferView:

    # create office supply transfer
    @api_view(['POST'])
    def post(request):
      
        serializer = serializers.OfficeSupplyTransfer(data=request.data)
      
        if serializer.is_valid():
            serializer.save()
            return Response({
            "message": "Transfer added Successfully!", 
            "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            "message": "Failed to add transfer."
        }, status=status.HTTP_400_BAD_REQUEST)

    # total office supply transfertransfers
    @api_view(['GET'])
    def total(request):
        
        data = models.OfficeSupplyTransfer.objects.count()
     
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)
 
    # retrieve supply transfer
    @api_view(['GET'])
    def get(request, id):
        
        data = models.OfficeSupplyTransfer.objects.get(pk=id)
        serializer = serializers.OfficeSupplyTransfer(data, many=False)
        
        return Response({
            "message": "Success", 
            "data": serializer.data
        }, status=status.HTTP_200_OK)

     # office supply transfertransfers
    @api_view(['GET'])
    def list(request, **kwargs):
        
        data = models.OfficeSupplyTransfer.objects.all().order_by("id")
        serializer = serializers.OfficeSupplyTransfer(data, many=True)

        return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # update office supply transfertransfer
    @api_view(['PATCH'])
    def update(request, id):
        
        instance = models.OfficeSupplyTransfer.objects.get(pk=id)   
        
        serializer = serializers.OfficeSupplyTransfer(
            instance=instance, 
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
            
        return Response({
            "message": "Update Failed!"
        }, status=status.HTTP_400_BAD_REQUEST)
    
     # delete transfer
    @api_view(['DELETE'])
    def delete(request, id):
        models.OfficeSupplyTransfer.objects.get(pk=id).delete()
        return Response({
            "Transfer Deleted Successfully!"
        }, status=status.HTTP_200_OK)
    
    # delete transfer
    @api_view(['DELETE'])
    def delete_all(request):
       
        models.OfficeSupplyTransfer.objects.all().delete()
       
        return Response({
            "Transfer Deleted Successfully!"
        }, status=status.HTTP_200_OK)

class OfficeSupplyArticleView:

    # create office supply article
    @api_view(['POST'])
    def post(request):
      
        if models.OfficeSupplyArticle.objects.filter(name=request.data["name"], type=request.data["type"]).exists():
            return Response({
            "message": "Article exists."
            }, status=status.HTTP_409_CONFLICT)
        
        serializer = serializers.OfficeSupplyArticle(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Article Created Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            "message": "Failed to Create Type."
        }, status=status.HTTP_400_BAD_REQUEST)

    # total office supply articleS
    @api_view(['GET'])
    def total(request):
        
        data = models.OfficeSupplyArticle.objects.count()
       
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)
    
    # retrieve supply article
    @api_view(['GET'])
    def get(request, id):
        
        data = models.OfficeSupplyArticle.objects.get(pk=id)
        serializer = serializers.OfficeSupplyArticle(data, many=False)
        
        return Response({
            "message": "Success", 
            "data": serializer.data
        }, status=status.HTTP_200_OK)

     # office supply articleS
    @api_view(['GET'])
    def list(request, **kwargs):
        
        data = models.OfficeSupplyArticle.objects.all()
        
        if kwargs.get("search"):
            term = kwargs.get("search")
            data = models.OfficeSupplyArticle.objects.filter(Q(name__icontains=term) | Q(pk__iexact=term))
        elif kwargs.get("entry"):
            data = models.OfficeSupplyArticle.objects.all()[:kwargs.get("entry")]
        
        serializer = serializers.OfficeSupplyArticle(data, many=True)
        
        return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # update office supply article
    @api_view(['PATCH'])
    def update(request, id):
        
        instance = models.OfficeSupplyArticle.objects.get(pk=id)   
        
        serializer = serializers.OfficeSupplyArticle(
            instance=instance, 
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
            
        return Response({
            "message": "Update Failed!"
        }, status=status.HTTP_400_BAD_REQUEST)
    
     # delete type
    @api_view(['DELETE'])
    def delete(request, id):

        if models.OfficeSupplyArticle.objects.get(pk=id).delete():
            return Response({
                "message": "Article Deleted Successfully!"
            }, status=status.HTTP_200_OK)


class OfficeSupplyView:

    # create office supply 
    @api_view(['POST'])
    def post(request):
        
        serializer = serializers.OfficeSupply(data=request.data)
      
        if serializer.is_valid():
            serializer.save()   
         
            return Response({
                "message": "Item Successfully Added!"
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            "message": "Failed to add item."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # generate stock number
    @api_view(['GET'])
    def stock_number(reques):
        
        data = models.OfficeSupply.objects.count() + 1
        
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)

    # get item quantity
    @api_view(['GET'])
    def get_quantity(request, id):
        
        data = models.OfficeSupply.objects.get(pk=id)
        
        serializer = serializers.OfficeSupply(data, many=False)
        
        return Response({
            "message": "Success", 
            "data": serializer.data
        } , status=status.HTTP_200_OK)


    # total office supplies
    @api_view(['GET'])
    def total(request, **kwargs):
       
        data = models.OfficeSupply.objects.count()
        
        serializer = serializers.OfficeSupply(models.OfficeSupply.objects.all(), many=True)
       
        if kwargs:
            for key in serializer.data[0].keys():
               
                data = models.OfficeSupply.objects.filter(**{key + "__icontains": kwargs.get("count")}).count()
               
                return Response({
                    "message": "Success!",
                    "data": data
                }, status=status.HTTP_200_OK)
        
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)

    # office supply list
    @api_view(['GET'])
    def list(request, **kwargs):
        
        try:
            if kwargs.get("search"):
               
                serializer = serializers.OfficeSupply(models.OfficeSupply.objects.all(), many=True)
               
                for key in serializer.data[0].keys():
               
                    data = models.OfficeSupply.objects.filter(**{key + "__icontains": kwargs.get("search")})
                    serializer = serializers.OfficeSupply(data, many=True)
               
                    if serializer.data:
                        return Response({ 
                            "message": "Success!", 
                            "total": len(serializer.data),
                            "data": serializer.data
                        }, status=status.HTTP_200_OK)
            
            elif kwargs.get("order"):
                data = models.OfficeSupply.objects.order_by(kwargs.get("order"))
            
            elif kwargs.get("entry"):
                data = models.OfficeSupply.objects.all()[:int(kwargs.get("entry"))]
            
            else:
                data = models.OfficeSupply.objects.all()
          
            serializer = serializers.OfficeSupply(data, many=True)
            
            return Response({ 
                "message": "Success!", 
                "total": len(serializer.data),
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # update office supply
    @api_view(['PATCH'])
    def update(request, id):
        
        instance = models.OfficeSupply.objects.get(pk=id)   
        
        serializer = serializers.OfficeSupply(
            instance=instance, 
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Updated Successfully!" 
            }, status=status.HTTP_200_OK)
            
        return Response({
            "message": "Item Update Failed!" 
        }, status=status.HTTP_400_BAD_REQUEST)  
    
    # clear office supply
    @api_view(['DELETE'])
    def clear(request,):
        
        models.OfficeSupply.objects.all().delete()   
        
        return Response({ 
            "message": "Cleared." 
        }, status=status.HTTP_200_OK)

class OfficeSupplyStockView:

    # create office supply 
    @api_view(['POST'])
    def post(request):
        
        serializer = serializers.OfficeSupplyStock(data=request.data)
        if serializer.is_valid():
            serializer.save()   
            return Response({
                "message": "New Item Added Successfully", 
                "data" : serializer.data
            }, status=status.HTTP_200_OK)
            
        return Response({
            "message": "Failed to add item."
        }, status=status.HTTP_400_BAD_REQUEST)

    # retrieve office supply stock
    @api_view(['GET'])
    def get(request, id):
        
        data = models.OfficeSupplyStock.objects.get(pk=id)
        
        serializer = serializers.OfficeSupplyStock(data, many=False)
        
        return Response({
            "message": "Success!" , "data": serializer.data
        }, status=status.HTTP_200_OK)

    # office supply stock
    @api_view(['GET'])
    def list(request, **kwargs):
        
        data = models.OfficeSupplyStock.objects.all()
        
        serializer = serializers.OfficeSupplyStock(data, many=True)
        return Response({
            "message": "Success!" , 
            "total": len(serializer.data),  
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # retrieve supply article
    @api_view(['GET'])
    def verify(request, type, article, measurement_unit):
        
        try:
            data = models.OfficeSupplyStock.objects.get(
                type=type, 
                article=article, 
                measurement_unit=measurement_unit
            )

            serializer = serializers.OfficeSupplyStock(data, many=False)
            
            return Response({
                "message": "Success!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "message": "Data not found!"
            }, status=status.HTTP_404_NOT_FOUND)
            
    # update office supply stock
    @api_view(['PATCH'])
    def update(request, id):
        
        instance = models.OfficeSupplyStock.objects.get(pk=id)   
        
        serializer = serializers.OfficeSupplyStock(
            instance=instance, 
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Item Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        return Response({
            "message": "Update Failed!"
        }, status=status.HTTP_400_BAD_REQUEST)

    # update office supply stock
    @api_view(['PATCH'])
    def update_quantity(request, id):
       
        stock = request.data["stock"]
        request = request.data["request"]
        instance = models.OfficeSupplyStock.objects.get(pk=id)   
       
        serializer = serializers.OfficeSupplyStock(instance=instance, data={
            "quantity": stock - request
        })
       
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Item Updated Successfully!, Total stocks: " + str(stock) + ", Approved request: " + str(request) +", Current stock: " + str(stock-request),
                "data": serializer.data
            }, status=status.HTTP_200_OK)
    
        return Response({
            "message": "Update Failed!"
        }, status=status.HTTP_400_BAD_REQUEST)

class InventoryTransferStatusView:  

    # create inventory transfer status
    @api_view(['POST'])
    def post(request):
        
        serializer = serializers.InventoryTransferStatus(data=request.data)
       
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Created Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({
            "message": "Failed to add inventory transfer status."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # inventory transfer status list
    @api_view(['GET'])
    def list(request, **kwargs):
     
        data = models.InventoryTransferStatus.objects.all()
     
        if kwargs.get("search"):
            term = kwargs.get("search")
            data = models.InventoryTransferStatus.objects.filter(Q(name__icontains=term) | Q(pk__iexact=term))
        elif kwargs.get("entry"):
            data = models.InventoryTransferStatus.objects.all()[:kwargs.get("entry")]
        
        serializer = serializers.InventoryTransferStatus(data, many=True)
        
        return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # total inventory transfer statuss
    @api_view(['GET'])
    def total(request):
        
        data = models.InventoryTransferStatus.objects.count()
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)
    
    # retrieve inventory transfer status
    @api_view(['GET'])
    def get(request, id):
        
        try:
            data = models.InventoryTransferStatus.objects.get(pk=id)
            serializer = serializers.InventoryTransferStatus(data, many=False)
            
            return Response({ 
                "message": "Success!", 
                "total": len(serializer.data),
                "data": serializer.data
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                "message": "Record not found.",
                "data": {}
            }, status=status.HTTP_404_NOT_FOUND)
        

    # update inventory transfer status
    @api_view(['PATCH'])
    def update(request, id):
        
        instance = models.InventoryTransferStatus.objects.get(pk=id)
        
        serializer = serializers.InventoryTransferStatus(
            instance=instance, 
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
            
        return Response({ 
            "message": "Update Failed!"
        }, status=status.HTTP_400_BAD_REQUEST)


class InventoryTransferMethodView:  

    # create inventory transfer status
    @api_view(['POST'])
    def post(request):
        
        serializer = serializers.InventoryTransferMethod(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Created Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({ 
            "message": "Failed to add inventory transfer status."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # inventory transfer status list
    @api_view(['GET'])
    def list(request, **kwargs):
        
        data = models.InventoryTransferMethod.objects.all()

        if kwargs.get("search"):
            term = kwargs.get("search")
            data = models.InventoryTransferMethod.objects.filter(
                Q(name__icontains=term) | 
                Q(pk__iexact=term)
            )
        elif kwargs.get("entry"):
            data = models.InventoryTransferMethod.objects.all()[:kwargs.get("entry")]
        
        serializer = serializers.InventoryTransferMethod(data, many=True)
        
        return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # total inventory transfer statuss
    @api_view(['GET'])
    def total(request):

        data = models.InventoryTransferMethod.objects.count()
       
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)
    
    # retrieve inventory transfer status
    @api_view(['GET'])
    def get(request, id):
        
        try:
            data = models.InventoryTransferMethod.objects.get(pk=id)
            serializer = serializers.InventoryTransferMethod(data, many=False)
            
            return Response({  
                "message": "Success!", 
                "total": len(serializer.data),
                "data": serializer.data
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                "message": "Data not found!"
            }, status=status.HTTP_404_NOT_FOUND)
        
    # update inventory transfer status
    @api_view(['PATCH'])
    def update(request, id):
        
        instance = models.InventoryTransferMethod.objects.get(pk=id)
        
        serializer = serializers.InventoryTransferMethod(
            instance=instance, 
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
            
        return Response({
            "message": "Update Failed!"
        }, status=status.HTTP_400_BAD_REQUEST)


class ImageView:

    @api_view(['GET'])
    def list(request, **kwargs):
        return Response(request.META["HTTP_HOST"] + settings.MEDIA_URL)

class DepartmentView:

    # create department
    @api_view(['POST'])
    def post(request):    
       
        try:
            if models.Department.objects.filter(name__iexact=request.data["name"]).exists():
                return Response({
                    "message": "Department already exists"
                }, status=status.HTTP_409_CONFLICT)

            elif models.Department.objects.filter(email__iexact=request.data["email"]).exists():
                return Response({
                    "message": "Email already exists"
                }, status=status.HTTP_409_CONFLICT)
           
            serializer = serializers.Department(data=request.data)
           
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "Department Added Successfully"
                }, status=status.HTTP_201_CREATED)
            
            return Response({
                "message": "Please complete the information below"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # total departmenets
    @api_view(['GET'])
    def total(request):
        
        data = models.Department.objects.count()
        
        return Response({ 
            "message": "Success!", 
            "data": data 
        }, status=status.HTTP_200_OK)

    # department list
    @api_view(['GET'])
    def list(request, **kwargs):
        
        try:
            if kwargs.get("search"):
              
                serializer = serializers.Department(models.Department.objects.all(), many=True)
              
                for key in serializer.data[0].keys():
              
                    if key == "employee": 
                        key += "__employee_no"
                    
                    data = models.Department.objects.filter(**{key + "__icontains": kwargs.get("search")})
                    serializer = serializers.Department(data, many=True)
                    
                    if serializer.data:
                        return Response({ 
                            "message": "Success!", 
                            "total": len(serializer.data),
                            "data": serializer.data
                        }, status=status.HTTP_200_OK)

            elif kwargs.get("order"):
                data = models.Department.objects.order_by(kwargs.get("order"))
            
            elif kwargs.get("entry"):
                data = models.Department.objects.all()[:int(kwargs.get("entry"))]
            
            else:
                data = models.Department.objects.all()
           
            serializer = serializers.Departments(data, many=True)
            data = serializer.data
            
            for i in range(len(data)):
                try:
                    department_head_id = data[i]["department_head_id"]
                    dept_head = models.Employee.objects.get(id=department_head_id)
                    dept_head_serializer = serializers.Employees(dept_head, many=False)
                    data[i]["department_head"] = dept_head_serializer.data
                except Exception as e:
                    data[i]["department_head"] = None
            
            return Response({
                "message": "Success!", 
                "total": len(data),"data": data
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # retrieve department
    @api_view(['GET'])
    def get(request, **kwargs):
        
        data = models.Department.objects.get(pk=kwargs.get("id"))
        serializer = serializers.Departments(data, many=False)
        
        return Response({
            "message": "Success!",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # retrieve department
    @api_view(['GET'])
    def get_department_head(request, id):
        
        data = models.Department.objects.get(pk=id)
        serializer = serializers.Departments(data, many=False)
        
        return Response({
            "message": "Success!", 
            "data": serializer.data["department_head_id"]
        }, status=status.HTTP_200_OK)

    # update department
    @api_view(['PATCH'])
    def update(request, id):
        
        instance = models.Department.objects.get(pk=id)   
        
        serializer = serializers.Department(
            instance=instance, 
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
            
        return Response({
            "message": "Update Failed!" 
        }, status=status.HTTP_400_BAD_REQUEST)   


    # delete department
    @api_view(['DELETE'])
    def delete(request, id):
       
        if models.Department.objects.get(pk=id).delete():
            return Response({
                "message": "Deleted Successfully!",
            }, status=status.HTTP_200_OK)
    
    
class ProvinceView:  

    # create province
    @api_view(['POST'])
    def post(request):
        
        serializer = serializers.Province(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Province Created Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({ 
            "message": "Unable to add province."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # province list
    @api_view(['GET'])
    def list(request, **kwargs):
        
        data = models.Province.objects.all()
      
        if kwargs.get("search"):
            term = kwargs.get("search")
            data = models.Province.objects.filter(
                Q(name__icontains=term) | 
                Q(pk__iexact=term)
            )
        elif kwargs.get("entry"):
            data = models.Province.objects.all()[:kwargs.get("entry")]
        
        serializer = serializers.Province(data, many=True)
        
        return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    
    # retrieve province
    @api_view(['GET'])
    def get(request, id):
        
        try:
            data = models.Province.objects.get(pk=id)
            serializer = serializers.Province(data, many=False)
            
            return Response({  
                "message": "Success!", 
                "total": len(serializer.data),
                "data": serializer.data
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                "message": "Record not found.",
                "data": {}
            }, status=status.HTTP_404_NOT_FOUND)

    # total countries
    @api_view(['GET'])
    def total(request):
        
        data = models.Province.objects.count()
        
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)

    # update province
    @api_view(['PATCH'])
    def update(request, id):
        
        instance = models.Province.objects.get(pk=id)
        
        serializer = serializers.Province(
            instance=instance, 
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
            
        return Response({
            "message": "Update Failed!"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # delete province
    @api_view(['DELETE'])
    def delete(request, id):
        
        try:
            models.Province.objects.get(pk=id).delete()
           
            return Response({
                "message": "Province Deleted Successfully!"
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                "message": "Data not found!"
            }, status=status.HTTP_404_NOT_FOUND)


class PositionView:

    # create position
    @api_view(['POST'])
    def post(request):
        
        try:
            serializer = serializers.Position(data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "Position added successfully",
                    "data": serializer.data
                }, status=status.HTTP_201_CREATED)
           
            return Response({
                "message": "Please complete the information below"
            }, status=status.HTTP_400_BAD_REQUEST)
       
        except Exception as e:  
            return Response({
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

    # total positions
    @api_view(['GET'])
    def total(request):
        data = models.Position.objects.count()
        return Response({ 
            "message": "Success!", 
            "data": data 
        }, status=status.HTTP_200_OK)
        

    # position list
    @api_view(['GET'])
    def list(request, **kwargs):
       
        try:
            department = kwargs.get("department")
       
            if kwargs.get("department"):
           
                if kwargs.get("search"):
           
                    data = models.Position.objects.filter(
                        Q(department=department) & (
                            Q(id__iexact=kwargs.get("search")) | 
                            Q(title__icontains=kwargs.get("search"))
                        )
                    )
                
                elif kwargs.get("order"):
                    data = models.Position.objects.filter(department=department).order_by(kwargs.get("order"))
                
                elif kwargs.get("entry"):
                    data = models.Position.objects.filter(department=department)[:int(kwargs.get("entry"))]
                
                else:
                    data = models.Position.objects.filter(department=department)
            else:
                if kwargs.get("search"):
                    data = models.Position.objects.filter(Q(id__iexact=kwargs.get("search")) | Q(title__icontains=kwargs.get("search")))
                
                elif kwargs.get("order"):
                    data = models.Position.objects.order_by(kwargs.get("order"))
                
                elif kwargs.get("entry"):
                    data = models.Position.objects.all()[:int(kwargs.get("entry"))]
                
                else:
                    data = models.Position.objects.all()

            serializer = serializers.Positions(data, many=True)
            
            return Response({
                "message": "Success!",
                "total": len(serializer.data),
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # retreive position
    @api_view(['GET'])
    def get(request, id):
 
        data = models.Position.objects.get(pk=id)
        serializer = serializers.Positions(data, many=False)
        
        return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    
    # vacant positions
    @api_view(['GET'])
    def vacant(request, **kwargs):
 
        try:
            data = models.Position.objects.filter(is_vacant=True).order_by("title")
            serializer = serializers.Positions(data, many=True)
 
            if serializer.data:
                
                data = serializer.data
                
                for i in range(len(data)):
                    try:
                        department_head_id = data[i]["department"]["department_head_id"]
                        dept_head = models.Employee.objects.get(id=department_head_id)
                        dept_head_serializer = serializers.Employees(dept_head, many=False)
                        data[i]["department"]["department_head"] = dept_head_serializer.data
                    except Exception as e:
                        data[i]["department"]["department_head"] = None
                        
            return Response({
                "message": "Success!",
                "total": len(serializer.data),
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # vacant positions by department
    @api_view(['GET'])
    def vacant_by_department(request, department):
        
        try:
           
            data = models.Position.objects.filter(
                is_vacant=True, 
                department_id=department
            ).order_by("title")

            serializer = serializers.Position(data, many=True)
            
            return Response({ 
                "message": "Success!", 
                "total": len(serializer.data),
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # total vacant positions
    @api_view(['GET'])
    def vacancies(request):
        
        data = models.Position.objects.filter(is_vacant=True).count()

        return Response({
            "message": "Success!", 
            "data": data
        }, status=status.HTTP_200_OK)


    # update position
    @api_view(['PATCH'])
    def update(request, id):
        
        instance = models.Position.objects.get(pk=id)
        
        serializer = serializers.Position(
            instance=instance, 
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Position Updated Successfully!"
            }, status=status.HTTP_200_OK)
        
        return Response({
            "message": "Failed to update position."
        }, status=status.HTTP_400_BAD_REQUEST)

    # delete position
    @api_view(['DELETE'])
    def delete(request):
        
        models.Position.objects.all().delete()
        
        return Response({
            "message": "Deleted successfully!"
        }, status=status.HTTP_200_OK)

class PermissionView:

    @api_view(['POST'])
    def post(request):
        
        try:
            serializer = serializers.Permission(data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "Permission Created Successfully!", 
                    "data": serializer.data
                }, status=status.HTTP_201_CREATED)
            
            return Response({
                "message": "Success!", 
                "data": serializer.data 
            }, status=status.HTTP_200_OK)

        except Exception as e: 
            return Response({
                "message": str(e),
            }, status=status.HTTP_409_CONFLICT)
            
    # total permissions
    @api_view(['GET'])
    def total(request):
        
        data = models.Permission.objects.count()
        
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)

    @api_view(['GET'])
    def list(request, **kwargs):
        
        try:
            if kwargs.get("search"):
                serializer = serializers.Permission(models.Permission.objects.all().order_by("description"), many=True)
               
                for key in serializer.data[0].keys():
                    data = models.Permission.objects.filter(**{key + "__icontains": kwargs.get("search")})
                    serializer = serializers.Permissions(data, many=True)
               
                    if serializer.data:
                        return Response({ 
                            "message": "Success!", 
                            "total": len(serializer.data),
                            "data": serializer.data
                        }, status=status.HTTP_200_OK)
                    
            elif kwargs.get("order"):
                data = models.Permission.objects.order_by(kwargs.get("order"))
            
            elif kwargs.get("entry"):
                data = models.Permission.objects.all()[:int(kwargs.get("entry"))]
            
            else:
                data = models.Permission.objects.all().order_by("description")
            
            serializer = serializers.Permissions(data, many=True)
            
            return Response({ 
                "message": "Success!", 
                "total": len(serializer.data),
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # update permission
    @api_view(['PATCH'])
    def update(request, id):
        
        permission = models.Permission.objects.get(pk=id)
        
        serializer = serializers.Permission(instance=permission, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        return Response({
            "message": "Success!", 
            "data": serializer.data 
        }, status=status.HTTP_200_OK)


class SettingsView:  

    # create settings
    @api_view(['POST'])
    def post(request):
        
        serializer = serializers.ReportType(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Settings Created Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({ 
            "message": "Failed to create settings."
        }, status=status.HTTP_400_BAD_REQUEST)

    # settings
    @api_view(['GET'])
    def get(request):
       
        data = models.Settings.objects.all().order_by("id")
        serializer = serializers.Settings(data, many=True)
      
        return Response({ 
            "message": "Success!", 
            "data": serializer.data[0]
        }, status=status.HTTP_200_OK)

    # update hr settings
    @api_view(['PATCH'])
    def update(request):
      
        instance = models.Settings.objects.get(pk=1)
      
        serializer = serializers.Settings(
            instance=instance, 
            data=request.data
        )
      
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Settings Updated!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        return Response({ 
            "message": "Failed to update settings."
        }, status=status.HTTP_400_BAD_REQUEST)

class ReportTypeView:  

    # create report type
    @api_view(['POST'])
    def post(request):
        
        serializer = serializers.ReportType(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Report type added Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({ 
            "message": "Failed to add report type."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # report type list
    @api_view(['GET'])
    def list(request, **kwargs):
        
        data = models.ReportType.objects.all().order_by("id")
       
        if kwargs.get("search"):
            term = kwargs.get("search")
            
            data = models.ReportType.objects.filter(
                Q(name__icontains=term) | 
                Q(pk__iexact=term)
            )
        
        elif kwargs.get("entry"):
            data = models.ReportType.objects.all()[:kwargs.get("entry")]
       
        serializer = serializers.ReportType(data, many=True)
        
        return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # total report types
    @api_view(['GET'])
    def total(request):
        
        data = models.ReportType.objects.count()
        
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)
    
    # retrieve report type
    @api_view(['GET'])
    def get(request, id):
        
        try:
            data = models.ReportType.objects.get(pk=id)
            serializer = serializers.ReportType(data, many=False)
            
            return Response({  
                "message": "Success!", 
                "total": len(serializer.data),
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                "message": "Record not found.",
                "data": {}
            }, status=status.HTTP_404_NOT_FOUND)
        
    # update report type
    @api_view(['PATCH'])
    def update(request, id):
       
        instance = models.ReportType.objects.get(pk=id)
        
        serializer = serializers.ReportType(
            instance=instance, 
            data=request.data
        )
       
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
       
        return Response({ 
            "message": "Update Failed!"
        }, status=status.HTTP_400_BAD_REQUEST)

    # delete report type
    @api_view(['DELETE'])
    def delete(request, id):
       
        models.ReportType.objects.get(pk=id).delete()
       
        return Response({
            "message": "Report type Deleted Successfully!"
        }, status=status.HTTP_200_OK)


class ReportView:

    # upload report
    @api_view(['POST'])
    def post(request):
        
        try:
            serializer = serializers.Report(data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "Report Submitted!", 
                    "data": serializer.data
                }, status=status.HTTP_201_CREATED)
            
            return Response({
                "message": "Failed to submit report!"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({
                "message": "Data not found!"
            }, status=status.HTTP_404_NOT_FOUND)

    # total reports 
    @api_view(['GET'])
    def total(request, **kwargs):
        data = models.Report.objects.count()
       
        if kwargs: 
            data = models.Report.objects.filter(employee__employee_no=kwargs.get("employee_no")).count()
       
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)

    # retrieve report
    @api_view(['GET'])
    def get(request, **kwargs):
        
        try:
            employee_no = kwargs.get("employee_no")
        
            if kwargs.get("search"):
                serializer = serializers.Report(models.Report.objects.all(), many=True)
                
                for key in serializer.data[0].keys():
                    if key == "employee": key += "__employee_no"
                    if key == "department": key += "__name"
                   
                    data = models.Report.objects.filter(**{
                        "employee__employee_no":employee_no, 
                        key + "__icontains": kwargs.get("search")
                    })

                    serializer = serializers.Report(data, many=True)
                   
                    if serializer.data:
                        return Response({ 
                            "message": "Success!", 
                            "total": len(serializer.data),
                            "data": serializer.data
                        }, status=status.HTTP_200_OK)
            
            elif kwargs.get("order"):
                data = models.Report.objects.filter(employee__employee_no=employee_no).order_by(kwargs.get("order"))
            
            elif kwargs.get("entry"):
                data = models.Report.objects.filter(employee__employee_no=employee_no)[:int(kwargs.get("entry"))]
            
            else:
                data = models.Report.objects.filter(employee__employee_no=employee_no)
            
            serializer = serializers.Report(data, many=True)
            
            return Response({ 
                "message": "Success!", 
                "total": len(serializer.data),
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # report list
    @api_view(['GET'])
    def list(request, **kwargs):
       
        try:
            if kwargs.get("search"):
                serializer = serializers.Report(models.Report.objects.all(), many=True)
                
                for key in serializer.data[0].keys():
                   
                    if key == "employee": 
                        key += "__employee_no"

                    data = models.Report.objects.filter(**{
                        key + "__icontains": kwargs.get("search")
                    })

                    serializer = serializers.Report(data, many=True)
                    
                    if serializer.data:
                        return Response({ 
                            "message": "Success!", 
                            "total": len(serializer.data),
                            "data": serializer.data
                        }, status=status.HTTP_200_OK)
                            
            elif kwargs.get("order"):
                data = models.Report.objects.order_by(kwargs.get("order"))
            
            elif kwargs.get("entry"):
                data = models.Report.objects.all()[:int(kwargs.get("entry"))]
            
            else:
                data = models.Report.objects.all()
            
            serializer = serializers.Report(data, many=True)
            
            return Response({ 
                "message": "Success!", 
                "total": len(serializer.data),
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @api_view(['GET'])
    def reports_by_employee(request, **kwargs):
        
        try:
            employee = kwargs.get("employee")
        
            if kwargs.get("search"):
                serializer = serializers.Report(models.Report.objects.all(), many=True)
               
                for key in serializer.data[0].keys():
                    if key == "employee": 
                        key += "__employee_no"
                    
                    data = models.Report.objects.filter(**{
                        key + "__icontains": kwargs.get("search")
                    })

                    serializer = serializers.Report(data, many=True)
                    
                    if serializer.data:
                        return Response({ 
                            "message": "Success!", 
                            "total": len(serializer.data),
                            "data": serializer.data
                        }, status=status.HTTP_200_OK)
            
            elif kwargs.get("order"):
                data = models.Report.objects.filter(employee=employee).order_by(kwargs.get("order"))
            
            elif kwargs.get("entry"):
                data = models.Report.objects.filter(employee=employee)[:int(kwargs.get("entry"))]
            
            else:
                data = models.Report.objects.filter(employee=employee)
            
            serializer = serializers.Report(data, many=True)
            
            return Response({ 
                "message": "Success!", 
                "total": len(serializer.data),
                "data": serializer.data
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # update report
    @api_view(['PATCH'])
    def update(request, id):
        
        try:
            report = models.Report.objects.get(pk=id)
            serializer = serializers.Report(instance=report, data=request.data)
        
            if serializer.is_valid():
                serializer.save()
                return Response({ 
                    "message": "Success!", 
                    "total": len(serializer.data),
                    "data": serializer.data
                }, status=status.HTTP_200_OK)
                
            return Response({
                "message": "No changes made!",
                "data": request.data
            }, status=status.HTTP_304_NOT_MODIFIED)
        
        except Exception as e:
            return Response({
                "message": "Data not found!"
            }, status=status.HTTP_404_NOT_FOUND)
    
    # delete report
    @api_view(['DELETE'])
    def delete(request, id):
       
        models.Report.objects.get(pk=id).delete()
       
        return Response({
            "message": "Deleted successfully!"
        }, status=status.HTTP_200_OK)

class RoleView:  

    # create role
    @api_view(['POST'])
    def post(request):
        
        if models.Role.objects.filter(title=request.data["title"]).exists():
            return Response({ 
                "message": "Role already exists."
            }, status=status.HTTP_409_CONFLICT)
        
        serializer = serializers.Role(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Role added Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({ 
            "message": "Failed to add role."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # role list
    @api_view(['GET'])
    def list(request, **kwargs):
        
        data = models.Role.objects.exclude(pk=1)
        
        if kwargs.get("search"):
            term = kwargs.get("search")
            data = models.Role.objects.exclude(pk=1).filter(Q(
                title__icontains=term) | Q(pk__iexact=term)
            )
        
        elif kwargs.get("entry"):
            data = models.Role.objects.exclude(pk=1)[:kwargs.get("entry")]
        
        serializer = serializers.Roles(data, many=True)
      
        return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # total roles
    @api_view(['GET'])
    def total(request):
      
        data = models.Role.objects.exclude(pk=1).count()
       
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)
    
    # retrieve role
    @api_view(['GET'])
    def get(request, id):
      
        try:
            data = models.Role.objects.get(pk=id)
            serializer = serializers.Role(data, many=False)
            
            return Response({  
                "message": "Success!", 
                "total": len(serializer.data),
                "data": serializer.data
            }, status=status.HTTP_200_OK)
      
        except Exception as e:
            return Response({
                "message": "Record not found.",
                "data": {}
            }, status=status.HTTP_404_NOT_FOUND)

    # update role
    @api_view(['PATCH'])
    def update(request, id):

        instance = models.Role.objects.get(pk=id)
        
        serializer = serializers.Role(
            instance=instance, 
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
      
        return Response({ 
            "message": "Update Failed!"
        }, status=status.HTTP_400_BAD_REQUEST)

    # delete role
    @api_view(['DELETE'])
    def delete(request, id):
    
        models.Role.objects.get(pk=id).delete()

        return Response({
            "message": "Role Deleted Successfully!"
        }, status=status.HTTP_200_OK)
    
class MotherView:
    
    # create mother
    @api_view(['POST'])
    def post(request):
        
        try:
            employee=models.Employee.objects.get(employee_no=request.data["employee"])
            employee_serializer = serializers.Employee(employee, many=False)
            request.data["employee"] = employee_serializer.data["id"]
            
            serializer = serializers.Mother(data=request.data)
          
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "Updated Successfully!", 
                    "data": serializer.data 
                }, status=status.HTTP_201_CREATED)
            
            return Response({
                "message": "Success!", 
                "data": serializer.data 
            }, status=status.HTTP_200_OK)

        
        except Exception as e:
            return Response({
                "message": "Data not found!"
            }, status=status.HTTP_404_NOT_FOUND)

    # retrieve mother
    @api_view(['GET'])
    def get(request, employee):
        
        try:
            data = models.Mother.objects.get(employee=employee)
            serializer = serializers.Mother(data, many=False)
        
            return Response({
                "message": "Success!", 
                "data": serializer.data 
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                "message": "Record not found.",
                "data": {}
            }, status=status.HTTP_404_NOT_FOUND)
        
    # update mother
    @api_view(['PATCH'])
    def update(request, id):
        
        instance = models.Mother.objects.get(pk=id)
        
        serializer = serializers.Mother(
            instance=instance, 
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Updated Successfully!", 
                "data": serializer.data 
            }, status=status.HTTP_200_OK)
        
        return Response({
            "message": "Success!", 
            "data": serializer.data 
        }, status=status.HTTP_200_OK)

     

class MeasurementUnitView:  

    # create measurement unit
    @api_view(['POST'])
    def post(request):
        
        if models.MeasurementUnit.objects.filter(name=request.data["name"]).exists():
            return Response({ 
                "message": "Unit already exists."
            }, status=status.HTTP_409_CONFLICT)
        
        serializer = serializers.MeasurementUnit(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Unit added Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({ 
            "message": "Failed to add measurement unit."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # measurement unit list
    @api_view(['GET'])
    def list(request, **kwargs):
        
        data = models.MeasurementUnit.objects.all()
       
        if kwargs.get("search"):
            term = kwargs.get("search")
            data = models.MeasurementUnit.objects.filter(
                Q(name__icontains=term) | Q(pk__iexact=term)
            )
        elif kwargs.get("entry"):
            data = models.MeasurementUnit.objects.all()[:kwargs.get("entry")]
        
        serializer = serializers.MeasurementUnit(data, many=True)
        return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # total measurement units
    @api_view(['GET'])
    def total(request):
        
        data = models.MeasurementUnit.objects.count()
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)
    
    # retrieve measurement unit
    @api_view(['GET'])
    def get(request, id):
      
        try:
            data = models.MeasurementUnit.objects.get(pk=id)
            serializer = serializers.MeasurementUnit(data, many=False)
            
            return Response({  
                "message": "Success!", 
                "total": len(serializer.data),
                "data": serializer.data
            }, status=status.HTTP_200_OK)
      
        except Exception as e:
            return Response({
                "message": "Record not found.",
                "data": {}
            }, status=status.HTTP_404_NOT_FOUND)

    # update measurement unit
    @api_view(['PATCH'])
    def update(request, id):
     
        instance = models.MeasurementUnit.objects.get(pk=id)
        
        serializer = serializers.MeasurementUnit(
            instance=instance, 
            data=request.data
        )
     
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        return Response({ 
            "message": "Update Failed!"
        }, status=status.HTTP_400_BAD_REQUEST)

    # delete measurement unit
    @api_view(['DELETE'])
    def delete(request, id):

        models.MeasurementUnit.objects.get(pk=id).delete()
        return Response({
            "message": "Unit Deleted Successfully!"
        }, status=status.HTTP_200_OK)

class MailView:
    @api_view(['POST'])
    def send_mail(request):
     
        try:
            send_mail(
                request.data["subject"],
                request.data["message"],
                request.data["from"],
                request.data["to"],
                fail_silently=False,
            )
     
            return Response({
                "message": "Message Sent Successfully!", 
                "data": request.data
            }, status=status.HTTP_200_OK)
       
        except Exception as e:
            return Response({
                "message": "Success!", 
                "data": serializer.data 
            }, status=status.HTTP_400_BAD_REQUEST)


class SexView:  

    # create sex
    @api_view(['POST'])
    def post(request):
        if models.Sex.objects.filter(name=request.data["name"]).exists():
            return Response({ 
                "message": "Sex already exists."
            }, status=status.HTTP_409_CONFLICT)
       
        serializer = serializers.Sex(data=request.data)
       
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Employee type added Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
       
        return Response({ 
            "message": "Failed to add sex."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # sex list
    @api_view(['GET'])
    def list(request, **kwargs):
        
        data = models.Sex.objects.all()
        
        if kwargs.get("search"):
            term = kwargs.get("search")
            data = models.Sex.objects.filter(Q(name__icontains=term) | Q(pk__iexact=term))
        elif kwargs.get("entry"):
            data = models.Sex.objects.all()[:kwargs.get("entry")]
        
        serializer = serializers.Sex(data, many=True)
        
        return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # total sexs
    @api_view(['GET'])
    def total(request):
        
        data = models.Sex.objects.count()
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)
    
    # retrieve sex
    @api_view(['GET'])
    def get(request, id):
        
        try:
            data = models.Sex.objects.get(pk=id)
            serializer = serializers.Sex(data, many=False)
            
            return Response({  
                "message": "Success!", 
                "total": len(serializer.data),
                "data": serializer.data
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                "message": "Record not found.",
                "data": {}
            }, status=status.HTTP_404_NOT_FOUND)
        

    # update sex
    @api_view(['PATCH'])
    def update(request, id):
        
        instance = models.Sex.objects.get(pk=id)
     
        serializer = serializers.Sex(
            instance=instance, 
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
            
        return Response({
            "message": "Update Failed!"
        }, status=status.HTTP_400_BAD_REQUEST)

    # delete employee type
    @api_view(['DELETE'])
    def delete(request, id):
        models.Sex.objects.get(pk=id).delete()
        return Response({
            "message": "Employee type Deleted Successfully!"
        }, status=status.HTTP_200_OK)
 
        
class SalaryView:  
    
     # create salary
    @api_view(['POST'])
    def post(request):
       
        if models.Salary.objects.filter(pay_grade=request.data["pay_grade"]).exists():
            return Response({
                "message": "Salary already exists."
            }, status=status.HTTP_409_CONFLICT)
      
        serializer = serializers.Salary(data=request.data)
      
        if serializer.is_valid():
            serializer.save()
            return Response({
            "message": "Salary added Successfully!", 
            "data": serializer.data
            }, status=status.HTTP_201_CREATED)
   
        return Response({
            "message": "Failed to add salary."
        }, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET'])
    def list(request):
        
        data = models.Salary.objects.all().order_by("pay_grade")
        
        serializer = serializers.Salary(data, many=True)
        
        return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    
    # total salaries
    @api_view(['GET'])
    def total(request):
        
        data = models.Salary.objects.count()
        return Response({
            "message": "Success!",
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    @api_view(['GET'])
    def get(request, id):
        
        data = models.Salary.objects.get(pk=id)
        
        serializer = serializers.Salary(data, many=False)
        
        return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    
    # update salary
    @api_view(['PATCH'])
    def update(request, id):
        
        instance = models.Salary.objects.get(pk=id)
        
        serializer = serializers.Salary(
            instance=instance, 
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)
            
        return Response({
            "message": "Failed to update Salary."
        }, status=status.HTTP_400_BAD_REQUEST)

    # delete salary
    @api_view(['DELETE'])  
    def delete(request, id):
        
        models.Salary.objects.get(pk=id).delete()
        
        return Response({
            "message": "Deleted Successfully!"
        }, status=status.HTTP_200_OK)

class SessionView:

    @api_view(['GET'])
    def list(request):
       
        data = models.Session.objects.all()
        
        serializer = serializers.Session(data, many=True)
    
        return Response({ 
            "message": "Success!", 
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)
        
    @api_view(['GET'])
    def get(request, session_id):
       
        try:
            data = models.Session.objects.get(session_id=session_id)
            serializer = serializers.Session(data, many=False)
            
            data={
                "session_id": serializer.data["session_id"],
                "session_data": json.loads(str(decrypt(serializer.data["session_data"]))),
            }
            
            return Response({
                "message": "Success!",
                "total": len(data),
                "data": data
            }, status=status.HTTP_200_OK)
       
        except Exception as e:
            return Response(str(e),status=status.HTTP_404_NOT_FOUND)
            
    #  user login
    @api_view(['POST'])
    def login(request):

        data=request.data
        username=data["username"]
        password=data["password"]

        if models.User.objects.filter(username=username, is_deactivated=1):
            return Response({
                "message": "Account has been deactivated!"
            }, status=status.HTTP_401_UNAUTHORIZED)

        for key in data:
            if not data[key]:
                return Response({
                    "message": key.capitalize() + " is required"
                }, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = models.User.objects.get(username=username)
            user_info = serializers.Users(user, many=False).data
            
            if(checkPassword(password, user_info["password"] ) == True):

                if username == password:
                    return Response({
                        "message": "You are using a default password, please reset your password",
                        "data": request.data
                    }, status=status.HTTP_409_CONFLICT)

                user_info["password"] = password

                session_data={
                    "user_info": user_info,
                    "ip_address": request.META.get("REMOTE_ADDR"),
                    "browser": request.user_agent.browser.family,
                    "os": request.user_agent.os.family,
                    "device": request.user_agent.device.family,
                    "login_time": date.get_datetime(),
                    "expiry": date.get_expiry()
                }
                
                serializer = serializers.Session(data={
                    "session_id": generated_session_id(),
                    "session_data": encrypt(stringify(session_data)),
                })

                
                if serializer.is_valid():
                    serializer.save()
                    return Response({
                        "message": "Login Success!",
                        "data": {
                            "session_id": serializer.data['session_id'],
                        }
                    }, status=status.HTTP_201_CREATED)
            
            return Response({
                "message": "Incorrect username or password.",
                "data": request.data
            }, status=status.HTTP_404_NOT_FOUND)

        except Exception as e: 
            return Response({
                "message": "Incorrect username or password."
            }, status=status.HTTP_404_NOT_FOUND)
        

    @api_view(['PATCH'])  
    def update(request):
  
        try:
            instance = models.Session.objects.get(session_id=request.data["session_id"])
           
            serializer = serializers.Session(
                instance=instance, 
                data=request.data
            )
  
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "Updated.", 
                    "data": serializer.data
                }, status=status.HTTP_200_OK)
  
            return Response({
                "message": "Success!", 
                "data": serializer.data 
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "message": "Data not found!"
            }, status=status.HTTP_404_NOT_FOUND)

    # logout
    @api_view(['DELETE'])  
    def logout(request, **kwargs):
      
        if kwargs.get("session_id"):
            models.Session.objects.get(session_id=kwargs.get("session_id")).delete()
          
            return Response({
                "message": "You are logged out."
            }, status=status.HTTP_200_OK)
        
        elif kwargs.get("session_id"):
            models.Session.objects.get(username=kwargs.get("username")).delete()
           
            return Response({
                "message": "User logged out."
            }, status=status.HTTP_200_OK)
 
    # clear session
    @api_view(['DELETE'])  
    def clear(request):
      
        models.Session.objects.all().delete()
        
        return Response({
            "message": "Cleared."
        }, status=status.HTTP_200_OK)

class SpouseView:
    
    # create spouse
    @api_view(['POST'])
    def post(request):
        
        try:
            employee=models.Employee.objects.get(employee_no=request.data["employee"])
            employee_serializer = serializers.Employee(employee, many=False)
            request.data["employee"] = employee_serializer.data["id"]
            serializer = serializers.Spouse(data=request.data)
       
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "Updated Successfully!", 
                    "data": serializer.data 
                }, status=status.HTTP_201_CREATED)
       
            return Response({
                "message": "Success!", 
                "data": serializer.data 
            }, status=status.HTTP_200_OK)
       
        except Exception as e:
            return Response({
                "message": "Data not found!"
            }, status=status.HTTP_404_NOT_FOUND)

    # retrieve spouse
    @api_view(['GET'])
    def get(request, employee):
        
        try:
            data = models.Spouse.objects.get(employee=employee)
            serializer = serializers.Spouse(data, many=False)
   
            return Response({
                "message": "Success!", 
                "data": serializer.data 
            }, status=status.HTTP_200_OK)
   
        except Exception as e:
            return Response({
                "message": "Record not found.",
                "data": {}
            }, status=status.HTTP_404_NOT_FOUND)
        
    # update spouse
    @api_view(['PATCH'])
    def update(request, id):
     
        instance = models.Spouse.objects.get(pk=id)
        
        serializer = serializers.Spouse(
            instance=instance, 
            data=request.data
        )
     
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Updated Successfully!", 
                "data": serializer.data 
            }, status=status.HTTP_200_OK)
     
        return Response({
            "message": "Success!", 
            "data": serializer.data 
        }, status=status.HTTP_200_OK)

    
# class TokenView:

    # # create token
    # @api_view(['POST'])
    # def post(request):
    #     try:
    #         # user instance
    #         user =  models.User.objects.get(username=request.data["user"]) 
    #         # get user id
    #         request.data["user"] = serializers.Users(user).data["id"]
    #         # token serializer
    #         serializer = serializers.Token(data=request.data)
    #         # if token serializer is valid
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response({
                    # "status": status.HTTP_201_CREATED, "message": "Key created successfully!", 
            # "data": serializer.data})
    #         else:
    #             return Response({
                    # "status": status.HTTP_409_CONFLICT, "message": "User has a key already!"})
    #     except Exception as e:
    #         return Response({
                    # "status": status.HTTP_401_UNAUTHORIZED, "message": "User does not exists!!" +str(e)})
    
    # # authenticate token
    # @api_view(['GET'])
    # def authenticate(request):
    #     try:    
    #         key = request.headers.get("Authorization").replace("Token ", 
            # "")
    #         models.Token.objects.get(key = key)
    #         return Response({
                    # "status": status.HTTP_202_ACCEPTED, "message": "Key validated!"})
    #     except KeyError as e:
    #         return Response({
                    # "status": status.HTTP_500_INTERNAL_SERVER_ERROR, "message": str(e)})
    #     except Exception as e:
    #         return Response({
                    # "status": status.HTTP_500_INTERNAL_SERVER_ERROR, "message": "Invalid Key!"})
# 
    # # update token
    # @api_view(['PATCH'])
    # def update(request):
    #     try:
    #         models.Token.objects.get(user = request.data["user"])
    #         data={
    #         "key": generated_token(),
    #         }
    #         query = serializers.Token(data = data, many=False)
    #         if query.is_valid():
    #             query.save()
    #             return Response({
                    # "status": status.HTTP_201_CREATED, "message": "User Key Updated Successfully!!", 
            # "data": query.data})
    #     except Exception as e:
    #         return Response({
                    # "status": status.HTTP_409_CONFLICT, "message": "User not found!"})

class UserActivityView:

    @api_view(['POST'])
    def post(request):
        
        request.data["ip_address"] = request.META.get("REMOTE_ADDR")
        
        serializer = serializers.UserActivity(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
           
            return Response({
                "message": "Created Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
      
        return Response({
            "message": "Failed to Create User Activity!"
        }, status=status.HTTP_400_BAD_REQUEST)

    # total user activities
    @api_view(['GET'])
    def total(request):  
        
        data = models.UserActivity.objects.count()
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)

    # total user activities by user
    @api_view(['GET'])
    def total_by_user(request, username):  
        
        data = models.UserActivity.objects.filter(user__username=username).count()

        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)

    # user activity list
    @api_view(['GET'])
    def list(request, **kwargs):

        try:
            data = models.UserActivity.objects.filter(filters.leave(kwargs)).order_by(*order_list(kwargs.get("order")))
        except Exception as e:
            data = models.UserActivity.objects.all().order_by(*order_list(kwargs.get("order")))

        serializer = serializers.UserActivities(data, many=True)
        
        return Response({
            "message": "Success!", 
            "total": len(serializer.data), 
            "data": serializer.data
        }, status=status.HTTP_200_OK)

class UserGroupView:

    # create user group
    @api_view(['POST'])
    def post(request):

        if models.UserGroup.objects.filter(user=request.data["user"]).exists():
       
            return Response({
                "message": "User group exists!"
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer = serializers.UserGroup(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Group added Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({
            "message": "Failed to add group.", 
            "data": request.data
        }, status=status.HTTP_400_BAD_REQUEST)

    # total user groups
    @api_view(['GET'])
    def total(request):
        
        data = models.UserGroup.objects.count()

        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)

    # user groups
    @api_view(['GET'])
    def list(request, **kwargs):

        try:
            data = models.UserGroup.objects.exclude(pk=1).order_by("user")

            if kwargs.get("search"):
                term = kwargs.get("search")
                data = models.UserGroup.objects.filter(
                    Q(group__name__icontains=term) | 
                    Q(user__username__icontains=term)
                )
            elif kwargs.get("entry"):
                data = models.UserGroup.objects.all().order_by("user")[:kwargs.get("entry")]

            serializer = serializers.UserGroups(data, many=True)
            return Response({
            "message": "Success!",
            "data": serializer.data,
        }, status=status.HTTP_200_OK) 

        except Exception as e:
            return Response({
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    # user group list
    @api_view(['GET'])
    def get(request, **kwargs):

        if kwargs.get("id"):
            data = models.UserGroup.objects.get(pk=kwargs.get("id"))
        elif kwargs.get("username"):
            data = models.UserGroup.objects.get(user__username=kwargs.get("username"))

        serializer = serializers.UserGroups(data, many=False)

        return Response({
            "message": "Success!",
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # update user group
    @api_view(['PATCH'])
    def update(request, **kwargs):

        if kwargs.get("id"):
            instance = models.UserGroup.objects.get(pk=kwargs.get("id"))
        elif kwargs.get("user"):
            instance = models.UserGroup.objects.get(user=kwargs.get("user"))

        serializer = serializers.UserGroup(
            instance=instance, 
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "User group updated.", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        return Response({
            "message": "Failed to update Data", 
            "data": request.data
        }, status=status.HTTP_400_BAD_REQUEST)

    # delete user group
    @api_view(['DELETE'])
    def delete(request, id):

        models.UserGroup.objects.get(pk=id).delete()

        return Response({
            "message": "Deleted Successfully!"
        }, status=status.HTTP_200_OK)


class UserTypeView: 

    # create user type
    @api_view(['POST'])
    def post(request):

        serializer = serializers.UserType(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "User Type added Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({ 
            "message": "Failed to add User Type."
        }, status=status.HTTP_400_BAD_REQUEST) 

    # total user types
    @api_view(['GET'])
    def total(request):
        
        data = models.UserType.objects.exclude(pk=1).count()
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)

    
    @api_view(['GET'])
    def list(request, **kwargs):

        data = models.UserType.objects.exclude(pk=1)

        if kwargs.get("entry"):
            data = models.UserType.objects.exclude(pk=1)[:kwargs.get("entry")]

        serializer = serializers.UserType(data, many=True)

        return Response({
            "message": "Success!",
            "total": len(serializer.data),
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # update user type
    @api_view(['PATCH'])
    def update(request, id):

        instance = models.UserType.objects.get(pk=id)
       
        serializer = serializers.UserType(
            instance=instance, 
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        return Response({ 
            "message": "Updated Failed!"
        }, status=status.HTTP_400_BAD_REQUEST)

    # delete user type
    @api_view(['DELETE'])
    def delete(request, id):

        try:
            models.UserType.objects.get(pk=id).delete()
           
            return Response({
                "status": status.HTTP_200_OK, 
                "message": "User type Deleted Successfully!"
            })
        
        except Exception as e:
            return Response({
                "status": status.HTTP_404_NOT_FOUND, 
                "message": "Unable to delete user type."
            })

class UserView:

    # register user
    @api_view(['POST'])
    def post(request):   

        try:   
            user_type = request.data["user_type"] 
            role = request.data["role"] 
            first_name = request.data["first_name"] 
            sur_name = request.data["sur_name"] 
            username = request.data["username"] 
            password = request.data["password"] 

            if not user_type:
                return Response({
            "message": "Please select a user type."
                }, status=status.HTTP_400_BAD_REQUEST)

            elif not role:
                return Response({
            "message": "Please select a role."
                }, status=status.HTTP_400_BAD_REQUEST)

            elif not sur_name:
                return Response({
            "message": "Surname is required."
                }, status=status.HTTP_400_BAD_REQUEST)

            elif has_illegal_chars(sur_name):
                return Response({
            "message": "Surname contains invalid characters."
                }, status=status.HTTP_411_LENGTH_REQUIRED)

            elif not first_name:
                return Response({
            "message": "Firsrt name is required."
                }, status=status.HTTP_400_BAD_REQUEST)

            elif has_illegal_chars(first_name):
                return Response({
            "message": "First name contains invalid characters."
                }, status=status.HTTP_411_LENGTH_REQUIRED)

            elif not username:
                return Response({
            "message": "Username required."
                }, status=status.HTTP_400_BAD_REQUEST)

            elif models.User.objects.filter(username__exact=username).exists():
                return Response({
            "message": "Username exists!"
                }, status=status.HTTP_411_LENGTH_REQUIRED)

            elif not password:
                return Response({
            "message": "Passsword required."
                }, status=status.HTTP_400_BAD_REQUEST)
            
            request.data["password"] = str(hashedPassword(password))
            serializer = serializers.User(data=request.data)

            if serializer.is_valid():
                serializer.save()
              
                return Response({
            "message": "User Created Successfully!", 
                    "data": serializer.data 
                }, status=status.HTTP_201_CREATED)
            
            return Response({
                "message": "Bad request."
            }, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    # total number of users
    @api_view(['GET'])
    def total(request, **kwargs):
        
        data = models.User.objects.filter(is_deactivated=0).exclude(pk=1).count()
        
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)

    # validate user email
    @api_view(['GET'])
    def validate_email(request, email):

        if models.User.objects.filter(email=email).exists():
            return Response({
                "message": "Email already exists."
            }, status=status.HTTP_409_CONFLICT)

        return Response({
            "message": "Email Available!"
        }, status=status.HTTP_200_OK)

    # list of employee emails
    @api_view(['GET'])
    def emails(request):
        
        data = models.User.objects.all(); 
        serializer = serializers.UserEmails(data, many=True)
       
        return Response({
            "message": "Success!",
            "data": serializer.data,
        }, status=status.HTTP_200_OK) 

    # user list 
    @api_view(['GET'])
    def list(request, **kwargs):
        
        try:
            if kwargs.get("search"):
               
                serializer = serializers.User(models.User.objects.exclude(pk=1), many=True)
                
                for key in serializer.data[0].keys():
                  
                    data = models.User.objects.exclude(pk=1).filter(**{ 
                        key + "__icontains": kwargs.get("search")
                    })
                    
                    serializer = serializers.Users(data, many=True)
                    
                    return Response({
                        "message": "Success!",
                        "data": serializer.data
                    }, status=status.HTTP_200_OK)
        
            else:
                data = models.User.objects.exclude(pk=1).order_by(*order_list(kwargs.get("order")))[:kwargs.get("entry")]
            
            serializer = serializers.Users(data, many=True)
            
            return Response({
                "message": "Success!",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
    # user list 
    @api_view(['GET'])
    def unused_accounts(request):
        
        data = models.User.objects.filter(employee=None).exclude(pk=1)
        
        serializer = serializers.Users(data, many=True)
        
        if serializer.data:
            return Response({ 
                "message": "Success!", 
                "total": len(serializer.data),
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        return Response(
            serializer.data, 
            status=status.HTTP_404_NOT_FOUND
        )

    # usernames 
    @api_view(['GET'])
    def no_user_group(request):
        
        user = []
        data = models.User.objects.all()
        
        serializer = serializers.User(data, many=True)
        
        for i in range(len(serializer.data)):
            try:
                models.UserGroup.objects.get(user=serializer.data[i]["id"])
            except Exception as e: 
                user.append(serializer.data[i])
        
        return Response(
            user, 
            status=status.HTTP_200_OK
        )

    # retrieve user
    @api_view(['GET'])
    def get(request, **kwargs):
        
        try:
            if kwargs.get("employee") is not None:
                data = models.User.objects.get(employee=kwargs.get("employee"))
            elif kwargs.get("username") is not None:
                data = models.User.objects.get(username=kwargs.get("username"))
            else:
                data = models.User.objects.get(pk=kwargs.get("id"))

            serializer = serializers.Users(data, many=False)
            userid = serializer.data["id"]
            data = serializer.data
            
            return Response({
                "message": "Success!",
                "total": len(serializer.data),
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                "message": "Data not found!"
            }, status=status.HTTP_404_NOT_FOUND)

    # update user
    @api_view(['PATCH'])
    def update(request, **kwargs):
        
        try:    
            if models.User.objects.filter(
                Q(username=request.data["username"]) & 
                ~Q(pk=request.data["id"])
            ).exists():
                return Response({
            "message": "Username exists!"
                }, status=status.HTTP_409_CONFLICT)

            if kwargs.get("id"):
                instance = models.User.objects.get(pk=kwargs.get("id"))
            else:
                instance = models.User.objects.get(username=kwargs.get("username"))
            
            serializer = serializers.User(
                instance=instance, 
                data=request.data
            )
            
            if serializer.is_valid():
                serializer.save() 
                return Response({
            "message": "Updated Successfully!", 
                    "data": serializer.data
                }, status=status.HTTP_200_OK)

            return Response({
                "message": "Update Failed!"
            }, status=status.HTTP_400_BAD_REQUEST)
                
        except Exception as e:
            return Response({
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # activate user
    @api_view(['PATCH'])
    def activate(request, **kwargs):
        
        try:    
            if kwargs.get("id"):
                instance = models.User.objects.get(pk=kwargs.get("id"))
            elif kwargs.get("employee"):
                instance = models.User.objects.get(employee=kwargs.get("employee"))
            elif kwargs.get("username"):
                instance = models.User.objects.get(username=kwargs.get("username"))
            
            serializer = serializers.User(instance=instance, data={
                "is_deactivated": 0
            })
            
            if serializer.is_valid():
                serializer.save() 
                
                return Response({
            "message": "Account Activated Successfully!", 
                    "data": serializer.data
                }, status=status.HTTP_200_OK)

            return Response({
                "message": "Update Failed!"
            }, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response({
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # de-activate user
    @api_view(['PATCH'])
    def deactivate(request, **kwargs):

        try:    
            if kwargs.get("id"):
                instance = models.User.objects.get(pk=kwargs.get("id"))
            elif kwargs.get("employee"):
                instance = models.User.objects.get(employee=kwargs.get("employee"))
            elif kwargs.get("username"):
                instance = models.User.objects.get(username=kwargs.get("username"))
            
            serializer = serializers.User(instance=instance, data={
                "is_deactivated": 1
            })

            if serializer.is_valid():
                serializer.save() 
                
                return Response({
            "message": "Account Deactivated Successfully!", 
                    "data": serializer.data
                }, status=status.HTTP_200_OK)

            return Response({
                "message": "Update Failed!"
            }, status=status.HTTP_400_BAD_REQUEST)
                
        except Exception as e:
            return Response({
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # update password
    @api_view(['PATCH'])
    def update_password(request):

        data=request.data
        
        username=request.data["username"]
        password=request.data["password"]
        new_password=request.data["new_password"]

        for key in request.data:
            if not request.data[key]:
                return Response({
            "message": capitalize(key) + " is required"
                }, status=status.HTTP_400_BAD_REQUEST)

        try:    
            user = models.User.objects.get(username=username)
            serializer = serializers.Users(user, many=False)

            if(checkPassword(password, serializer.data["password"]) == True):

                if has_illegal_chars(new_password):
                    return Response({
                        "message": "Password contains invalid characters."
                    }, status=status.HTTP_411_LENGTH_REQUIRED)
                
                elif not starts_with_capital_letter(new_password):
                    return Response({
                        "message": "Password must start with capital letter."
                    }, status=status.HTTP_411_LENGTH_REQUIRED)
                
                elif not password_length_valid(new_password):
                    return Response({
                        "message": "Password must be at least 8 to 16 characters."
                    }, status=status.HTTP_411_LENGTH_REQUIRED)
               
                serializer = serializers.UpdatePassword(
                    instance=user, 
                    data={
                        "password": str(hashedPassword(new_password))
                    }
                )
              
                if serializer.is_valid():
                    serializer.save()  
                    return Response({
                        "message": "Password changed successfully"
                    }, status=status.HTTP_200_OK)
              
                return Response({       
                    "message": "Incorrect username or password"
                }, status=status.HTTP_304_NOT_MODIFIED)
            
            else: 
                return Response({
            "message": "Incorrect username or password"
                }, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            return Response({
                "message": "Incorrect username or password"
            }, status=status.HTTP_404_NOT_FOUND)

    # reset password
    @api_view(['PATCH'])
    def reset_password(request):
        
        try:    
            username = request.data["username"]
            user = models.User.objects.get(username=username)
            
            serializer = serializers.UpdatePassword(
                instance=user, 
                data={
                    "password": hashedPassword(username)
                }
            )
          
            if serializer.is_valid():
                serializer.save()  
               
                return Response({
            "message": "Password Updated Successfully!!"
                }, status=status.HTTP_200_OK)
          
            return Response({
                "message": "Password Update Failed!"
            }, status=status.HTTP_304_NOT_MODIFIED)
        
        except Exception as e:
            return Response({
                "message": "Data not found!"
            }, status=status.HTTP_404_NOT_FOUND)

    # update active status
    @api_view(['PATCH'])
    def login(request, username):        
    
        try:
            instance = models.User.objects.get(username=username)
    
            serializer = serializers.User(
                instance=instance, 
                data={
                    "is_active": 1
                }
            )
    
            if serializer.is_valid():
                serializer.save()  
                return Response({
                    "message": "Login Success!"
                }, status=status.HTTP_200_OK)
    
            return Response({
                "message": "Failed to update active status"
            }, status=status.HTTP_304_NOT_MODIFIED)
    
        except Exception as e:
            return Response({
                "message": "Data not found!"
            }, status=status.HTTP_404_NOT_FOUND)
            
    # update active status
    @api_view(['PATCH'])
    def logout(request, username):        
        
        try:
            instance = models.User.objects.get(username=username)

            serializer = serializers.User(
                instance=instance, 
                data={
                "is_active": 0
                }
            )
        
            if serializer.is_valid():
                serializer.save()  
                return Response({
            "message": "Logged Out Successfully!"
                }, status=status.HTTP_200_OK)
       
            return Response({
                "message": "Failed to update active status"
            }, status=status.HTTP_304_NOT_MODIFIED)
       
        except Exception as e:
            return Response({
                "message": "Data not found!"
            }, status=status.HTTP_404_NOT_FOUND)

class UserPermissionsView:    

    # create user permission
    @api_view(['POST'])
    def post(request):
        
        if models.UserPermissions.objects.filter(
            user=request.data["user"], 
            permission=request.data["permission"]
        ).exists():
            return Response({ 
                "message": "Permission already exists."
            }, status=status.HTTP_409_CONFLICT)
        
        serializer = serializers.UserPermission(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Permission Added Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({ 
            "message": "Failed to Add Permission."
        }, status=status.HTTP_400_BAD_REQUEST)

    # total user permissions
    @api_view(['GET'])
    def total(request):
        
        data = models.UserPermissions.objects.count()
        return Response({
            "message": "Success!",
            "data": data
        }, status=status.HTTP_200_OK)

    # get user permissions
    @api_view(['GET'])
    def get(request, id):
        
        try:
            data = models.UserPermissions.objects.get(pk=id)
            serializer = serializers.UserPermissions(data, many=False)
            return Response({
            "message": "Success!",
            "data": serializer.data,
        }, status=status.HTTP_200_OK) 

        except Exception as e:
            return Response({
                "message": "Data not found!"
            }, status=status.HTTP_404_NOT_FOUND)

    # user permission list
    @api_view(['GET'])
    def list(request, **kwargs):
        
        try:
            if kwargs.get("user"):
                data = models.UserPermissions.objects.filter(user=kwargs.get("user"))
            elif kwargs.get("search"):
                term = kwargs.get("search")
                data = models.UserPermissions.objects.filter(
                    Q(permission__description__icontains=term) | 
                    Q(permission__description__icontains=term)
                )
            elif kwargs.get("entry"):
                data = models.UserPermissions.objects.all().order_by("user")[:kwargs.get("entry")]
            else:
                data = models.UserPermissions.objects.all().order_by("user")
            
            serializer = serializers.UserPermissions(data, many=True)
            return Response({
            "message": "Success!",
            "data": serializer.data,
        }, status=status.HTTP_200_OK) 
            
        except Exception as e:
            return Response({
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # update group permission
    @api_view(['PATCH'])
    def update(request, id):
        
        if models.UserPermissions.objects.filter(
            user=request.data["user"], 
            permission=request.data["permission"]
        ).exists():
            return Response({ 
                "message": "Permission Already Exists."
            }, status=status.HTTP_409_CONFLICT)
        
        instance = models.UserPermissions.objects.get(pk=id)
        
        serializer = serializers.UserPermission(
            instance=instance, 
            data=request.data
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({ 
                "message": "Permission Updated Successfully!", 
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        return Response({ 
            "message": "Failed to update Permission."
        }, status=status.HTTP_400_BAD_REQUEST)


    # delete user permission
    @api_view(['DELETE'])
    def delete(request, **kwargs):
       
        try:
            if kwargs.get("id"):
                models.UserPermissions.objects.get(pk=kwargs.get("id")).delete()
            elif kwargs.get("user"):
                models.UserPermissions.objects.get(user=kwargs.get("user")).delete()
            else:
                models.UserPermissions.objects.all().delete()
       
            return Response({
                "message": "Permission Deleted Successfully!"
            }, status=status.HTTP_200_OK)
       
        except Exception as e:
            return Response({
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# validate email
@api_view(['GET'])
def is_new_email_available(request, email):
   
    if models.Employee.objects.filter(email=email).exists():
        return Response({
            "message": str(e)
        }, status=status.HTTP_409_CONFLICT)
   
    if models.User.objects.filter(email=email).exists():
        return Response({
            "message": str(e)
        }, status=status.HTTP_409_CONFLICT)
   
    return Response({
            "message": "Email is available!"
        }, status=status.HTTP_200_OK)


