from rest_framework import serializers
from .models import Questions , QuestionImages

class QuestionSerializer(serializers.ModelSerializer):

  class Meta:
    model = Questions 
    fields ='__all__'
  # id = serializers.IntegerField()
  # publisher_name = serializers.CharField(max_length=255 , default='SVI')
 
 

class QuestionImageSerializer(serializers.ModelSerializer):

  class Meta:
    model = QuestionImages 
    fields ='__all__'


