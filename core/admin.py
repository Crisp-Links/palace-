
from django.contrib import admin

from .models import *


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    '''Admin View for Property'''

    list_display = ('user', 'region', 'town')
    list_filter = ('user', 'upload_date', 'region',)
    search_fields = ('region', 'town')
    ordering = ('region',)

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    '''Admin View for Amenity'''

    list_display = ('name',)

    search_fields = ('name',)

@admin.register(Carocel)
class CarocelAdmin(admin.ModelAdmin):
    '''Admin View for Carocel'''

    list_display = ('image',)
    search_fields = ('image',)

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    '''Admin View for Region'''

    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

    ordering = ('name',)

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for Category'''

    list_display = ('name',)
    list_filter = ('name',)

    search_fields = ('name',)
    ordering = ('-name',)