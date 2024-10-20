from django.shortcuts import render
from .models import TestPackage
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from .serializers import TestPackageSerializer , CreatePackages
from student_related_exams.models import DoneExams
from student_related_exams.serializers import  GetSolvedSerializer
from django.db import connection
from rest_framework import generics  
from rest_framework.permissions import IsAuthenticated
from users.models import User
from django.shortcuts import get_object_or_404 

 


@api_view(['GET']) 
def get_all_packages(request, subject_name):


 publisher_name = request.GET.get('publisher_name')
 
 price = request.GET.get('price')
 user_id =request.GET.get('user_id')
 
 obj = TestPackage.objects.filter( subject_name = subject_name , price__lte = price)
 user_solved_exams = DoneExams.objects.filter( student =user_id )
 


 if publisher_name !='عرض الكل':
  obj = obj.filter(publisher_name = publisher_name)  

 serial = TestPackageSerializer( obj , many = True )
 serial2 = GetSolvedSerializer( user_solved_exams , many = True )

 return Response( { 'packages':serial.data , 'solved':serial2.data } ,status =200)

@api_view(['GET']) 
def get_package_info(request , id):
 
 obj = TestPackage.objects.filter( id = id )

 serial = TestPackageSerializer(obj , many=True)

 return Response( serial.data ,status =200)
 
@api_view(['PUT']) 
def increase_num_of_apps(request , id):
 
 obj = TestPackage.objects.get( id = id )
 obj.number_of_apps += 1
 obj.save()

 return Response( 'update number of app is done' ,status =200)
 
@api_view() 
def testing_all(request):

 obj = TestPackage.objects.all()
 serial = TestPackageSerializer(obj , many=True)
 
 return Response( serial.data,status = status.HTTP_200_OK)

class TestingIn(APIView):
  def get(self, request  , id):
    td = TestPackage.objects.filter( id = id)
    serial = TestPackageSerializer(td , many=True)
    return Response(serial.data,200)
   
  
  def post(self, request , id):
    serial = TestPackageSerializer(data = request.data)
    if serial.is_valid(raise_exception=True): 
        print(request.data)
        serial.save()
        return Response("all good ",200)
    return Response(serial.errors )


class GetAllPackages(ListCreateAPIView): 
  queryset = TestPackage.objects.all()
  serializer_class = TestPackageSerializer



    
#1 GET , POST
class create_test_packages(generics.ListCreateAPIView):
   # permission_classes = (IsAuthenticated,)
    queryset = TestPackage.objects.all()
    serializer_class = CreatePackages
   # return Response(serial. )

#2 GET PUT and DELETE 
class edit_test_packages(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = TestPackage.objects.all()
    serializer_class = CreatePackages

