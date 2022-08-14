
import json
from multiprocessing import context
from xmlrpc.client import Boolean
from django.http import HttpRequest, HttpResponse
from django.db.models import Q

from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404, redirect, render
from authentication.forms import CustomUserChangeForm
from core.models import *
from .forms import PropertyForm
from authentication.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from pay.forms import *
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

@login_required(login_url='login')
def dashboard(request):
    user = User.objects.all
    properties = Property.objects.filter(user=request.user)
    region = Region.objects.all()
    context ={
        'properties':properties,
        'region':region,
        'user':user}
    return render(request, 'landlord/dashboard.html', context)


# @login_required(login_url='login')
# def createProperty(request):
#     payment_form = PaymentForm()
#     form = PropertyForm()
#     if request.method == 'POST':
        # if request.POST.get('form_type') == 'formA':
        #     form = PropertyForm(request.POST, request.FILES)
        #     if form.is_valid():
        #         form.save(commit=False)
        #         form.instance.user = request.user
        #         form.save()
        #         form.save_m2m()
        #         return redirect('dashboard')
#         elif request.POST.get('form_type') == 'formB':
#             payment_form = PaymentForm(request.POST)
#             if payment_form.is_valid():
#                 payment_form.save(commit=False)
#                 payment_form.instance.email = request.user
#                 payment = payment_form.save()
#                 return render (request, 'landlord/createProperty.html', {'payment': payment, 'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY})
#     return render(request, 'landlord/createProperty.html', {'form': form, 'payment_form': payment_form})

@login_required(login_url='login')
def createProperty(request, ref):
    payment = get_object_or_404(Payment, ref=ref)
    # property = get_object_or_404(Property, ref=ref)
    # properties = get_object_or_404(Property, ref=ref)
    # prop = Property.objects.get(ref=ref)

    form = PropertyForm()
    
    try:
        if request.method == 'POST':
            if request.POST.get('form_type') == 'formA':
                form = PropertyForm(request.POST, request.FILES)
                if form.is_valid():
                    form.save(commit=False)
                    form.instance.user = request.user
                    form.instance.ref = payment.ref
                    form.save()
                    form.save_m2m()
                    return redirect('dashboard')
    except:
           return HttpResponse('Apartmnet ale')     
    context = {
        'form':form
    }
    return render(request, 'landlord/createProperty.html', context)
    
def verify_payment(request: HttpRequest, ref:str) -> HttpResponse:
    payment = get_object_or_404(Payment, ref=ref)
    verified = payment.verifiy_payment()
    if verified:
        messages.success(request, 'Verification Successfull')
    else:
        messages.error(request, 'Verification Failed')
    return redirect('dashboard')


@login_required(login_url='login')
def updateProperty(request, pk):
    property = get_object_or_404(Property, id=pk)
    form = PropertyForm(request.POST or None, request.FILES or None, instance=property)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form': form}
    return render(request, 'landlord/property-update.html', context)


@login_required(login_url='login')
def deleteProperty(request, pk):
    property = Property.objects.get(id=pk)
    if request.user != property.user:
        return redirect('login')
    if request.method == 'POST':
        property.delete()
        return redirect('dashboard')
    context = {'obj': property}
    return render(request, 'landlord/delete-obj.html', context)


@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = CustomUserChangeForm(instance=user)

    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            messages.error(request, 'Something went wrong. Try again')
            # return redirect('updateuser')

    return render(request, 'landlord/update-user.html', {'form': form})


def getDistrict(request):
    data = json.loads(request.body)
    region_id = data['id']
    print(region_id)
    districts = District.objects.filter(region__id=region_id)
    return JsonResponse(list(districts.values("id", "name")), safe=False)




        # if request.headers.get('x-requested-with') == 'XMLHttpRequest':
    #     print('Ajax')
    #     amount = json.load(request)['amount']
    #     payment = Payment.objects.create(amount=amount, email=request.user)
    #     payment.save()

    #     data ={'amount':payment.amount}
    #     return JsonResponse(data, status=200)