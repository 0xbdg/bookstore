from django import forms
from django.forms.widgets import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from phonenumber_field.formfields import PhoneNumberField

class SignUp(UserCreationForm):
    firstname = forms.CharField(required=True, widget=TextInput(attrs={"class":"form-control", "placeholder":"Enter firstname"}))
    lastname = forms.CharField(required=True, widget=TextInput(attrs={"class":"form-control", "placeholder":"Enter lastname"}))
    username = forms.CharField(required=True, widget=TextInput(attrs={"class":"form-control", "placeholder":"Enter username"}))
    email = forms.EmailField(required=True, widget=EmailInput(attrs={"class":"form-control", "placeholder":"Enter email"}))
    password1 = forms.CharField(required=True, widget=PasswordInput(attrs={"class":"form-control", "placeholder":"Enter password"}))
    password2 = forms.CharField(required=True, widget=PasswordInput(attrs={"class":"form-control", "placeholder":"Confirm password"}))
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ["firstname","lastname", "username", "email","password1","password2", "captcha"]

class SignIn(AuthenticationForm):
    username = forms.CharField(required=True, widget=TextInput(attrs={"class":"form-control", "placeholder":"Enter username"}))
    password = forms.CharField(required=True, widget=PasswordInput(attrs={"class":"form-control", "placeholder":"Enter password"}))
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ["username","password","captcha"]

class ProfileUpdate(UserChangeForm):
    firstname = forms.CharField(required=True, widget=TextInput(attrs={"class":"form-control", "placeholder":"Enter firstname"}))
    lastname = forms.CharField(required=True, widget=TextInput(attrs={"class":"form-control", "placeholder":"Enter lastname"}))
    username = forms.CharField(required=True, widget=TextInput(attrs={"class":"form-control", "placeholder":"Enter username"}))
    email = forms.EmailField(required=True, widget=EmailInput(attrs={"class":"form-control", "placeholder":"Enter email"}))
    phonenumber = PhoneNumberField(region="ID")

    class Meta:
        model = User
        fields=["firstname","lastname","username","email"]