 
from django.db import models
from django.dispatch import receiver
from django.core.validators import MinValueValidator
from django.db import connection
 
 
import os

 
subject_name_choices =[
      ('math_12',' رياضيات بكلوريا'),
      ('science_12',' علوم بكلوريا'),
      ('english_12','انكليزي بكلوريا'),
      ('arabic_12','عربي بكلوريا'),
      ('physics_12','فيزياء بكلوريا'),
      ('chemistry_12','كيمياء بكلوريا'),
      ('national_12',' وطنية بكلوريا'),
      ('france_12','فرنسي بكلوريا') ,
      
      ('math_9','رياضيات تاسع') ,
      ('science_9','علوم تاسع') ,
      ('english_9','انكليزي تاسع') ,
      ('arabic_9','عربي تاسع') ,
      ('physics_chemistry_9','فيزياء و كيمياء تاسع') ,
      ('geography_9','اجتماعيات تاسع') ,
      ('france_9','فرنسي تاسع') ,

]

class TestPackage(models.Model):

    package_name = models.CharField( max_length=500 , help_text=" هون منحط شو محتوى الاختبار , متل مثلا اختبار في وحدة الأعصاب , وفي وحدة الهرمونات أو شامل" )
    publisher_name = models.CharField(max_length=255 , default='SVI' , blank=True)
    units = models.CharField(max_length=800 , help_text="هون منحط الوحدات بالاسم يلي الاختبار عم يحكي عنهم , اذا في اكتر من وحدة افصل بينهم بفاصلةعادية  ")
    subject_name = models.CharField( max_length=25,choices=subject_name_choices ,default='math_12' , blank=True)
    premium = models.BooleanField( default = False , blank=True)
    price = models.IntegerField(default = 0 , blank=True)
    number_of_apps =models.IntegerField( verbose_name='number of applications', default= 0 , editable= False)
    date_added = models.DateField(  auto_now_add=True )
   
    def __str__(self):
        return    self.package_name + ' , '+  str(self.id) 
  
   
    @property 
    def current_number_of_tests(self):
      res = []
      with connection.cursor() as cursor:
        curr = self.id
        cursor.execute(f"""
 select  count(*)  from   tests_tests
 where package_id = {curr} ; """)

        res  = cursor.fetchall()
     
      return  res[0][0]

    
    