from django import forms

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from gallery.models import Customer, Profile

User_type = [('artist', 'Artist'), ('customer', 'Customer')]

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    #user_type = forms.RadioSelect(choices = User_type)

    class Meta:
        model = User
        fields = [ 'username', 'email', 'password1', 'password2']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'username', 'email']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [ 'username', 'email']