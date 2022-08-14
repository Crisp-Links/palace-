from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Payment
from django.contrib import messages
from . import forms
from django.conf import settings

from core.models import Property

def initiate_payment(request: HttpRequest) -> HttpResponse:
    email = request.user.email
    first_name = request.user.first_name
    last_name = request.user.last_name
    
    if request.method == 'POST':
        payment_form = forms.PaymentForm(request.POST)
        if payment_form.is_valid():
            payment_form.save(commit=False)
            payment_form.instance.email = request.user
            
            payment = payment_form.save()
            phone = request.user.phone
            return render (request, 'pay/make_payment.html', {
                'payment': payment, 
                'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY, 
                'email':email, 'phone':phone,
                'last_name':last_name,
                'first_name':first_name,
                }
                )
    else:
        payment_form = forms.PaymentForm()
    return render(request, 'pay/initiate_payment.html', {'payment_form':payment_form})

def verify_payment(request: HttpRequest, ref) -> HttpResponse:
    payment = get_object_or_404(Payment, ref=ref)
    verified = payment.verify_payment()
    if verified:
        messages.success(request, 'Verification Successfull')
        return redirect('createProperty', ref=ref)
    else:
        messages.error(request, 'Verification Failed')
        return redirect('initiate_payment')

    