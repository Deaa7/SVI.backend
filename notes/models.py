from django.db import models

class Notes(models.Model):
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

    title = models.CharField(max_length=2000)
    subject_name = models.CharField( max_length=25,choices=subject_name_choices ,default='math_12' , blank=True)
    publisher_name = models.CharField(max_length=255 , default='SVI' , blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=False)
    premium = models.BooleanField(default=False)
    price = models.IntegerField(default=0)
    number_of_reads =models.IntegerField( verbose_name='number of reads', default= 0 , editable= False ,null= True, blank = True)


    def __str__(self):
        return self.title

class NoteImages(models.Model):
    note_id = models.ForeignKey(Notes , on_delete=models.CASCADE)
    images = models.ImageField(upload_to="ImagesForTests/", verbose_name = 'إضافة صورة', null=True , blank = True)
