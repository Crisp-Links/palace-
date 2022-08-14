from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User
from core.models import *


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
    class Meta:
        model = User
        fields = ('first_name' , 'last_name', 'phone','email')



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone')

       