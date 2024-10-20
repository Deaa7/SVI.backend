from django.contrib import admin
from .models import TestPackage
from questions.models import Questions
from django.db import connection
# Register your models here.
class QuestionsInline(admin.StackedInline):
    model =Questions 
    extra = 0

 
class TestPackageAdmin(admin.ModelAdmin): 
    list_display = ['package_name','id','subject_name','publisher_name','premium','units','current_number_of_tests','number_of_apps' ]
    search_fields = ['package_name','subject_name','premium','publisher_name']
    list_filter =['package_name' ,'subject_name','premium','publisher_name']   
    inlines = [QuestionsInline] 
   


admin.site.register(TestPackage ,TestPackageAdmin)
