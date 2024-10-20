from django.shortcuts import get_object_or_404, render
from rest_framework import generics  
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Notes , NoteImages
from .serializers import NoteFilterSerializer, NoteSerializer , NoteImagesSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .filters import NoteFilter
from rest_framework import status


#GET , POST
# لاضافة ملاحظات من خلال ادخال بيانات او لعرض الملاحظات بدون ادخالها
class add_note(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer


#GET , POST
class add_noteImages(generics.ListCreateAPIView):
    # parser_classes =(MultiPartParser , FormParser)
    # permission_classes = (IsAuthenticated,)
    queryset = NoteImages.objects.all()
    serializer_class = NoteImagesSerializer


# id بيعرض الملاحظات مع المحتوى من خلال
@api_view(['GET']) 
def get_all_notes(request , id): # gets a single note by its id
    obj = Notes.objects.get(id = id) 
    serial = NoteSerializer(obj )
    return Response(serial.data)


# عرض الملاحظات بدون المحتوى مع فلترة حسب اسم الناشر والسعر
# عرض الملاحظات بدون المحتوى مع فلترة حسب اسم الناشر والسعر
@api_view(['GET'])
def get_by_filter(request , all = 0):

    if all == 0:
        num = 8
    else:
        num = 1000000

    subject_name = request.GET.get('subject_name', None)
    queryset = Notes.objects.filter(subject_name=subject_name).order_by('id')

    filterset = NoteFilter(request.GET, queryset=queryset)
    serializer = NoteFilterSerializer(filterset.qs[:num] , many=True)
    return Response(serializer.data)

# id بيعرض الملاحظات بدون المحتوى من خلال 
@api_view(['GET'])  # single note view
def getNote(request , id):
    obj = Notes.objects.filter(id = id) 
    print('here i am :',obj)
    serializer = NoteFilterSerializer(obj , many=True)
    return Response(serializer.data)

#زيادة عدد القراء بمقدر واحد
@api_view(['PUT'])
def inc_numRead(request , id):

    note = get_object_or_404(Notes , id = id)
    note.number_of_reads += 1 
    note.save()
    serializer = NoteSerializer(note)
    return Response('increase is done successfully' ,status = 200)

    