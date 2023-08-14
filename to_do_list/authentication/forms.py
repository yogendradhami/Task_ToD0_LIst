from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms


# form for chagepassword
class PasswordChangingForm(PasswordChangeForm):
    old_password= forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password1=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password2=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))

    class Meta:
        model=User
        field="__all__"