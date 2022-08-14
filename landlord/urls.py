from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashbord'),
    path('createProperty/<str:ref>', views.createProperty, name='createProperty'),

    path('getDistrict/', views.getDistrict, name='getDistrict'),
    path('property-update/<str:pk>/', views.updateProperty, name='update'),
    path('property-delete/<str:pk>/', views.deleteProperty, name='delete'),
    path('userupdate/', views.updateUser, name='updateuser')

]
