from rest_framework import serializers
from .models import Notes , NoteImages

#عرض الملاحظات مع المحتوى
class NoteSerializer(serializers.ModelSerializer):
    class Meta :
       model = Notes
       fields = '__all__'

#عرض صور الملاحظات
class NoteImagesSerializer(serializers.ModelSerializer):
    class Meta :
       model = NoteImages
       fields = '__all__'

#عرض الملاحظات بدون المحتوى 
class NoteFilterSerializer(serializers.ModelSerializer):
    class Meta:
       model = Notes
       fields = ['id','title','subject_name','publisher_name','date_uploaded','premium','price','number_of_reads']





