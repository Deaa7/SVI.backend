from rest_framework import serializers
from .models import TestPackage
from questions.models import Questions


class TestPackageSerializer(serializers.ModelSerializer):

 class Meta:
  model = TestPackage 
  fields =['id','package_name','units','subject_name','premium','number_of_apps','publisher_name' ,'price','number_of_tests','date_added']
 
 number_of_tests = serializers.SerializerMethodField(method_name='calc')

 def calc(self, testPackage: TestPackage):
    return Questions.objects.filter(package_id = testPackage.id).count()
 
class CreatePackages(serializers.ModelSerializer):
  
  class Meta :
    model = TestPackage
    fields = ['id','package_name' , 'units' , 'subject_name' , 'premium' , 'price' , 'publisher_name']