from typing import Sized
from django.db import models
from django.db import models
from django_resized import ResizedImageField
from authentication.models import User

from pay.models import *


class Region(models.Model):
    name = models.CharField(max_length=50, null=True)
    
    
    def __str__(self):
        return self.name

class District(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

class Amenity(models.Model):
     """Model definition for Amenity."""
     name = models.CharField(max_length=50)

     class Meta:
         """Meta definition for Amenity."""

         verbose_name = 'Amenity'
         verbose_name_plural = 'Amenities'

     def __str__(self):
         """Unicode representation of Amenity."""
         return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Property(models.Model):
     """Model definition for Property."""
     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
     category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
     price = models.PositiveIntegerField(null=True, blank=True)
     address = models.CharField(max_length=10)
     amenities = models.CharField(max_length=500, null=True)
     region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
     district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
     town = models.CharField(max_length=15)
     ref = models.CharField(max_length=20, null=True, unique=True, blank=True)
     image1 = ResizedImageField(size=[200, 150], 
                                          crop=['middle', 'center'],
                                          default='media/brightpalace.png', 
                                        upload_to='media/propertyImages')
     image2 = ResizedImageField(size=[200, 150], 
                                          crop=['middle', 'center'],
                                          default='media/brightpalace.png', 
                                        upload_to='media/propertyImages')
     image3 = ResizedImageField(size=[200, 150], 
                                          crop=['middle', 'center'],
                                          default='media/brightpalace.png', 
                                        upload_to='media/propertyImages')
    #  favourite = models.ManyToManyField(User, related_name='favourite', blank=True)
     description = models.TextField()
     upload_date = models.DateTimeField(auto_now_add=True)

     def get_price(self):
        price = self.price
        return price
    
     class Meta:
         """Meta definition for Property."""

         verbose_name = 'Property'
         verbose_name_plural = 'Properties'

     def __str__(self):
         """Unicode representation of Property."""
         return self.address

     @property
     def imageURL(self):
        try:
            url = self.image1.url
        except:
            url = self.image1.url
        return url
        # for image url (product.imageURL)

class Carocel(models.Model):
    image = ResizedImageField(size=[1366, 768], 
                                          crop=['middle', 'center'],
                                          
                                          default='media/brightpalace.png', 
                                        upload_to='media/carocel')
