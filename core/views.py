from .filters import PropertyFilter
from multiprocessing import context
from django.core.paginator import Paginator
from random import random
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import ListView
from urllib3 import Retry
from .models import *



def search(request):
    regions = Region.objects.all()
    if request.method == 'POST':
        searched = request.POST['searched']
        properties = Property.objects.filter(
            Q(region__name__contains=searched)|
            Q(town__contains=searched)|
            Q(district__name__contains=searched)|
            Q(address__contains=searched)
        )
        context = {
            'searched': searched, 
            'properties': properties,
            'regions':regions,
            }
        return render(request, 'core/search.html', context)
    else:
        return redirect('index')

def sidebarFilter(request):
    property = Property.objects.all()
    filterForm =  PropertyFilter()
    context = {'property':property, 'filterForm':filterForm}
    return render(request, 'sidebar.html', context)

def region_filter(request, pk):
    property = Property.objects.all()
    category = Category.objects.all()
    regions = Region.objects.all()
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    region = Region.objects.filter(name__icontains=q, id=pk)
    reg = Region.objects.get(id=pk)
    context = {'region':region,
                'regions':regions,
                'reg':reg,
                'property':property,
                'category':category,
            
            }
    return render(request, 'core/region-filter.html', context)



def category(request):
    property = Property.objects.all()
    category = Category.objects.all()[:10]
    regions = Region.objects.filter()
    carocel = Carocel.objects.all()
    filterForm = PropertyFilter()
    context = {'filterForm':filterForm, 'carocel':carocel, 'property':property,'category': category, 'regions':regions}
    return render(request, 'core/index.html', context)

def cat_item(request, pk):
    category = Category.objects.get(id=pk)
    property = category.property_set.all()
    regions = Region.objects.all()
    context = {
        'category':category,
        'property':property,
        'regions':regions
        }
    return render(request, 'core/home.html', context)




class PropertyView(ListView):
    model = Property
    paginate_by = 2
    context_object_name = 'property'
    template_name = "core/home.html"
    ordering = ['-upload_date']

    def get_queryset(self):
        queryset = super(PropertyView, self).get_queryset()
        queryset = queryset[0:4]
        return queryset
    
    def get_context_data(self, *args, **kwargs):        
        context = super(PropertyView, self).get_context_data(*args,**kwargs)
        context['carocel'] = Carocel.objects.all()
        context['region'] = Region.objects.all()
        context['district'] = District.objects.all()
        return context


def detail(request, pk):
    prop = Property.objects.get(id=pk)
    context = {'prop':prop}
    return render(request, 'core/detail.html', context)    


def booking(request, pk):
    prop = Property.objects.get(id=pk)
    context = {'prop':prop}
    return render(request, 'core/booking.html', context)  

def about(request):
    context = {}
    return render(request, 'core/about.html', context)


