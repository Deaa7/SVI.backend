from rest_framework import serializers
from .models import DoneExams

class DoneExamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoneExams
        fields =  '__all__'

class GetSolvedSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoneExams
        fields = ('exam_id',)

 