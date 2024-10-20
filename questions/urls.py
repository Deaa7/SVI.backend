

from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('all_tests/<int:package_id>', views.get_all_questions),
    path('add_questions/', views.add_questions.as_view()),
    path('add_TestImages/', views.add_QuestionImages.as_view()),
    path('get_test_images/<int:test_id>/', views.get_question_images),
    path('edit_questions/<int:pk>/', views.edit_questions.as_view()),
]
