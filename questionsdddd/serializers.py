from rest_framework import serializers
from .models import Questions , QuestionImages

class TestSerializer(serializers.ModelSerializer):

  class Meta:
    model = Questions 
    fields ='__all__'
  # id = serializers.IntegerField()
  # publisher_name = serializers.CharField(max_length=255 , default='SVI')
 
class Questions(serializers.ModelSerializer):

  class Meta:
    model = Questions 
    fields ='__all__'


class TestImageSerializer(serializers.ModelSerializer):

  class Meta:
    model = QuestionImages 
    fields ='__all__'


