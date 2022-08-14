
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .views import ResetPasswordView



urlpatterns = [   
    # authentication start
    path('landlord/', views.dashboard, name='dashboard'),
    path('signup/', views.registerPage, name='signup'),
    path('', views.signin, name='login'),
    path('signout/', views.signout, name='signout'),
    path('registration_success/', views.registerPage, name='registration_success'),
    # for activation by email
    path('activate/<uidb64>/<token>/',views.activate, name='activate'),  
    
    # password reset
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='authentication/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='authentication/password_reset_complete.html'),
         name='password_reset_complete'),
    # end of authentication
]
