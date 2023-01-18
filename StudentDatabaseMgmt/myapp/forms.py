from django import forms
from .models import *
from django.contrib.auth.models import User;

class Student_form(forms.ModelForm):
    First_Name =forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter first name'}), required=True, max_length=100)
    Last_Name =forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter last name'}), required=True, max_length=100)
    Employee_ID =forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Enter employee ID'}), required=True, max_length=10)
    Email_ID =forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter E-mail ID'}),required=True,max_length=30)
    Phone_Number = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Enter Phone Number'}), required=True, max_length=100)
    Country = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Country'}),required=True, max_length=100)
    User_Name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'User name'}),required=True, max_length=100)
    Password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}),required=True, max_length=100)
    class Meta():
        model = Students
        fields = ['First_Name', 'Last_Name','Employee_ID', 'Phone_Number','Country','Email_ID', 'User_Name', 'Password']

class Student_form2(forms.ModelForm):
    Username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','style': "background-color:LightGray", 'placeholder': ' Enter User name'}), required=True, max_length=100)
    Password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'style':"background-color:LightGray",'placeholder': ' Enter Password'}),required=True, max_length=100)
    First_Name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','style':"background-color:LightGray", 'placeholder': 'Enter first name'}), required=True,max_length=100)
    Last_Name = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control','style':"background-color:LightGray", 'placeholder': 'Enter last name'}), required=True, max_length=100)
    Email_ID =forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','style':"background-color:LightGray", 'placeholder':'Enter E-mail ID'}),required=True,max_length=30)
    class Meta():
        model = User
        fields = ['Username','Password','First_Name','Last_Name','Email_ID']