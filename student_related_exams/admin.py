from django.contrib import admin
from .models import PremiumExams,DoneExams

# Register your models here.


class PremiumExamsAdmin(admin.ModelAdmin):
    
    list_display = ['student','subject_name','date_of_expiration','exam_name','exam_id' ]
    search_fields = ['student']
    list_filter = ['student']   
   
class DoneExamsAdmin(admin.ModelAdmin):
    
    list_display = ['student','subject_name','date_of_application','exam_name','exam_id','result' ]
    search_fields = ['student']
    list_filter = ['student']   
   



#  pass
admin.site.register(PremiumExams ,PremiumExamsAdmin)
admin.site.register(DoneExams , DoneExamsAdmin)