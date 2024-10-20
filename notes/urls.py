from django.urls import path
from . import views

urlpatterns = [
    path('get_all_notes/<int:id>/', views.get_all_notes),    # id بيعرض الملاحظات مع المحتوى من خلال
    path('getNote/<int:id>/', views.getNote),                # id بيعرض الملاحظات بدون المحتوى من خلال 
    path('add_note/', views.add_note.as_view()),             # لاضافة ملاحظات من خلال ادخال بيانات او لعرض الملاحظات بدون ادخالها
    path('add_noteImages/', views.add_noteImages.as_view()), # اضافة صور للملاحظات 
    path('get_by_filter/<int:all>/', views.get_by_filter),   # عرض الملاحظات بدون المحتوى مع فلترة حسب اسم الناشر والسعر
    path('inc_numRead/<int:id>/', views.inc_numRead),        #زيادة عدد القراء بمقدر واحد
]
