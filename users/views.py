from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404 
from django.contrib.auth import logout
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .serializers import SingUpSerializer,UserSerializer
from .models import User

@api_view(['POST'])
def register(request):
 
    data = request.data
    user = SingUpSerializer(data = data)
   
    if user.is_valid():
     
        if not User.objects.filter(username=data['email']).exists():
                   
            user = User.objects.create(
                username = data['username'] , 
                email = data['email'] ,
                password = make_password(data['password']),
                is_teacher = 'False'
             ) 
            return Response(
                {'details':'Your account registered successfully!' },
                    status=status.HTTP_201_CREATED
                    )
        else:
            return Response(
                {'error':'This email already exists!' },
                    status=status.HTTP_400_BAD_REQUEST
                    )
    else:
        return Response(user.errors)

@api_view(['POST'])
def login(request):
        
        user = get_object_or_404(User , username = request.data['username'])

        if not user.check_password(request.data['password']):
            return Response({"Error" : "Invlid Password"} , status=status.HTTP_400_BAD_REQUEST)
        
        if user.number_of_login_sessions == 1 :
             return Response({"There is someone else using this account"} , status=status.HTTP_400_BAD_REQUEST)

        user.number_of_login_sessions = 1
        user.save() 

        refresh = RefreshToken.for_user(user)

        data = {"username": request.data['username'], "password": request.data['password']}

        serializer = UserSerializer(instance = user)

        return Response({"access_token": str(refresh.access_token) ,"refresh_token" : str(refresh) , "user" : serializer.data} , status = status.HTTP_200_OK)

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh_token")
            if not refresh_token:
                return Response('refresh_token is required', status=status.HTTP_400_BAD_REQUEST)
            
            token = RefreshToken(refresh_token)
            token.blacklist()

            user = get_object_or_404(User, username=request.data['username'])
            user.number_of_login_sessions = 0
            user.save()
            return Response('logout is done', status=status.HTTP_202_ACCEPTED)
        
        except Exception as e:
            return Response(f"{e}  logout is failed", status=status.HTTP_406_NOT_ACCEPTABLE)
