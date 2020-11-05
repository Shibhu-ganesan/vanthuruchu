from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ['Name','Email','Field','Query']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1', 'password2']
        

# class PersonForm(ModelForm):
#     class Meta:
#         model = Person


# class PetForm(ModelForm):
#     class Meta:
#         model = Pet
#         exclude = ('owner',)
