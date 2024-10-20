from django.db import models
from django.dispatch import receiver 
from users.models import User
from django.db.models.signals import post_save

# Create your models here.

# Profile_student
class Profile_Student(models.Model):
    user = models.OneToOneField(User, primary_key = True  , on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50 , default="" , blank=True)
    last_name = models.CharField(max_length=50 , default="" , blank=True)
    city = models.CharField(max_length=50 , default="" , blank=True)
  
    def __str__(self):
     return str(self.user)

@receiver(post_save, sender = User )
def save_profile(sender,instance, created, **kwargs):

    # print('instance',instance)
    user = instance
 
    if created and  user.is_teacher == 'False':
        profile = Profile_Student(user = user)
        profile.save()
    

#Profile_Teacher
class Profile_Teacher(models.Model):
    user = models.OneToOneField(User , primary_key = True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50 , default="" , blank=True)
    last_name = models.CharField(max_length=50 , default="" , blank=True)
    studying_subjects = models.CharField(max_length=500 )
    phone_number = models.CharField(max_length = 15 ,default='-',blank=True)
    another_phone_number = models.CharField(max_length = 15 ,default='-',blank=True)
    total_net = models.IntegerField(default=0 , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=50 , default="" , blank=True)
    image = models.ImageField( blank=True , null= True)
    
    def __str__(self):
     return self.first_name + ' ' + self.last_name


@receiver(post_save, sender = User )
def save_profile_teacher(sender,instance, created, **kwargs):

    # print('instance',instance)
    user = instance

    if created and user.is_teacher == 'True' :
        profile = Profile_Teacher(user = user)
        profile.save()
    