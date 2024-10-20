from django.contrib import admin
from django.urls import path  , include, reverse_lazy
from rest_framework_simplejwt import views as jwt_views
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
  path('register/',views.register , name='register'),
  path('login/',views.login , name='login'),
  path('logout/',views.LogoutView.as_view() , name='logout'),
  path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

  path('password-reset/' ,auth_views.PasswordResetView.as_view(template_name= "reset_Password/password_reset.html") , name="reset_password"),
  path('password-reset/done/' ,auth_views.PasswordResetDoneView.as_view(template_name= "reset_Password/password_reset_sent.html") , name="password_reset_done"),
  path('password-reset-confirm/<uidb64>/<token>/' ,auth_views.PasswordResetConfirmView.as_view(template_name= "reset_Password/password_reset_form.html") , name="password_reset_confirm"),
  path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name= "reset_Password/password_reset_done.html") , name="password_reset_complete"),
]