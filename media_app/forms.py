from django import forms

from media_app.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email']
        widgets={'password':forms.PasswordInput}


class ProfileForm(forms.ModelForm):
    class Meta:
        model=profile
        fields=['address','profile_pic']