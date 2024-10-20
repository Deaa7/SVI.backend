from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status
from .models import Questions , QuestionImages
from .serializers import  QuestionSerializer , QuestionImageSerializer
from rest_framework import generics  
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.
 
@api_view(['GET']) 
def get_all_questions( request , package_id):

    obj = Questions.objects.filter(package_id = package_id).order_by('id') # only one row

    serial = QuestionSerializer(obj,many=True) #

    return Response( serial.data)

#1 GET , POST
class add_questions(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer


#2 GET PUT and DELETE 
class edit_questions(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer

#1 GET , POST
class add_QuestionImages(generics.ListCreateAPIView):
    parser_classes =(MultiPartParser , FormParser)
    queryset = QuestionImages.objects.all()
    serializer_class = QuestionImageSerializer

@api_view(['GET'])
def get_question_images( request , test_id):
  field_name = request.GET.get('field_name')
  obj = QuestionImages.objects.filter( test_id = test_id , field_name = field_name )
  serial = QuestionImageSerializer(obj , many = True)
  return Response( serial.data , status = 200)
 
