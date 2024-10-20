from django.db import models
from profiles.models import Profile_Student

# Create your models here.

class PremiumExams(models.Model): # exams paid by a student
 
 student = models.ForeignKey(Profile_Student , on_delete = models.CASCADE)
 exam_id = models.CharField(max_length = 10)
 date_of_expiration = models.DateField()
 subject_name = models.CharField(max_length=25)
 exam_name = models.CharField(max_length=50)



class DoneExams(models.Model): # exams done by a student
 
 student = models.ForeignKey(Profile_Student , on_delete = models.CASCADE)
 subject_name = models.CharField(max_length=25)
 exam_name = models.CharField(max_length=50)
 exam_id = models.CharField(max_length = 10)
 date_of_application = models.DateField(auto_now_add=True ,blank=True )
 result = models.DecimalField( max_digits = 5 , decimal_places = 2 )
