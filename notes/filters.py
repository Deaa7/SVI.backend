import django_filters
from .models import Notes

class NoteFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    price = django_filters.NumberFilter(field_name="price" or 1000000 , lookup_expr="lte")
    class Meta :
       model = Notes
       fields = ['publisher_name','price']