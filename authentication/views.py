
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
# from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str 
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .tokens import account_activation_token
from django.core.mail import EmailMessage 
from .models import *
from landlord.views import *



def registerPage(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            
            current_site = get_current_site(request)  
            mail_subject = 'Confirm your account creation'  
            message = render_to_string('authentication/confirm-email.html', {  
                'user': user,  
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)), 
                'token':account_activation_token.make_token(user),  
            })  
            to_email = form.cleaned_data.get('email') 
             
            email = EmailMessage(  
                        mail_subject, message, to=[to_email]  
            )  
            email.send()   

            return render(request, 'authentication/registration_success.html')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'authentication/signup.html', {'form': form})

def activate(request, uidb64, token):  
    User = get_user_model()
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        
        user.save()  
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')  
    else:  
        return HttpResponse('Activation link is invalid!')  

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'authentication/password_reset.html'
    email_template_name = 'authentication/password_reset_email.html'
    subject_template_name = 'authentication/password_reset_subject.html'
    success_message = "We've emailed you instructions for setting your password. if an account exists with the email you entered. You should receive them shortly. if an account exists with the email you entered. You should receive them shortly. if an account exists with the email you entered. You should receive them shortly. If you don't receive an email, please make sure you've entered the address you registered with, and check your spam folder. if you have not received the email, check the email you've provieded for errors"    
    success_url = reverse_lazy('login')

def signin(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        
        user = authenticate(email=email, password=password1)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successfull')
            return redirect( 'dashboard')
            
        else:
            messages.error(request, 'Wrong credentials! Please try again.')

            return redirect('login')
        
    return render(request, 'authentication/signin.html')

def signout(request):
    logout(request)
    messages.success(request, 'logout successfully')
    return redirect('login')




