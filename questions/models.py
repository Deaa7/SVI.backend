from django.db import models
from test_packages.models import TestPackage

class Questions(models.Model):
 
 possible_answers = {'A' :'A' ,'B':'B','C':'C','D':'D','E':'E'}
 
 package = models.ForeignKey(TestPackage,on_delete=models.CASCADE)

 test_content =  models.TextField()
 
 option_A = models.TextField(  null = True , blank = True)
 option_B = models.TextField(  null = True , blank = True)
 option_C= models.TextField(  null = True , blank = True)
 option_D = models.TextField(  null = True , blank = True)
 option_E = models.TextField(  null = True , blank = True)
 right_answer = models.CharField(max_length = 1 , choices=possible_answers, default ='A')
 explanation = models.TextField( help_text='شرح الإجابة الصحيحة'  , default='لا يتوفر شرح للإجابة')
 
 def __str__(self):
  return  str(self.id)

class QuestionImages(models.Model):
 field_name_choices =[
      ('test_content',' test_content'),
      ('option_A',' option_A'),
      ('option_B','option_B'),
      ('option_C','option_C'),
      ('option_D','option_D'),
      ('option_E','option_E'),
      ('explanation','explanation'),
 ]

 test_id = models.ForeignKey(Questions , on_delete=models.CASCADE)
 field_name = models.CharField(max_length = 100 ,choices  =field_name_choices ,default='test_content' , blank=True)
 images = models.ImageField(upload_to="ImagesForTests/", verbose_name = 'إضافة صورة', null=True , blank = True)
