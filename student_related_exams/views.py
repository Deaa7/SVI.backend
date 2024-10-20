from django.shortcuts import render
from .models import DoneExams
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from .serializers import DoneExamsSerializer
from django.db import connection



 

class ExamDoneRecord(ListCreateAPIView): 
  queryset = []
  serializer_class = DoneExamsSerializer
  



