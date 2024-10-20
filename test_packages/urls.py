from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('testing_get_all', views.GetAllPackages)

urlpatterns = [
    path('get_packages/<str:subject_name>/', views.get_all_packages),
    path('get_single_package/<int:id>/', views.get_package_info   ),
    path('increase_num_of_apps/<int:id>/', views.increase_num_of_apps   ),
    path('create_test_packages/', views.create_test_packages.as_view()   ),
    path('edit_test_packages/<int:pk>/', views.edit_test_packages.as_view()),

    # path('testing1/', views.testing_all   ),
    # path('testing2/<int:id>/', views.TestingIn.as_view()   ),
    # path('testing_get_all/', views.GetAllPackages.as_view()   ),
]
