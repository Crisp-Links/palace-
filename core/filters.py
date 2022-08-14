from dataclasses import fields
import django_filters
from .models import *

class PropertyFilter(django_filters.FilterSet):
    class Meta:
        model = Property
        fields = ('region', 'district', 'town')
        # exclude = ['user']