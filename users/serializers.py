from rest_framework import serializers
from .models import User

class SingUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email', 'password','is_teacher')
 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','is_teacher') 