
from django.urls import path

# from .views import PropertyView
from . import views 

urlpatterns = [
    # path('property/<int:pk>/', views.property, name='home'),
    path('', views.category, name='index'),
    path('category/<int:pk>/', views.cat_item, name='home'),

    # path('', PropertyView.as_view(), name='home'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('booking/<int:pk>/', views.booking, name='booking'),
    path('about/', views.about, name='about'),
    path('search-result/', views.search, name='search-result'),
    path('regoion-filter/<str:pk>/', views.region_filter, name='region-filter'),
    # path('filterForm', views.sidebarFilter, name='filterForm'),
]