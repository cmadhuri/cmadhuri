from django import forms
from django.forms import fields, models
from django.forms.widgets import Textarea
from app_blog.models import blogpage,login
from django.contrib.auth.models import User


class loginform(forms.ModelForm): 
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields =('username','email', 'password')  

class profileinfoform(forms.ModelForm):
    class Meta():
        model = login
        fields = ('profile_pic',)

class blog_form(forms.ModelForm):
    title= forms.CharField()
    blogs = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = blogpage
        fields ="__all__"
