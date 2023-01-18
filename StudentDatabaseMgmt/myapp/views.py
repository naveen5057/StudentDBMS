from django.http import HttpResponse
from django.shortcuts import *
from .models import *
from .forms import *
from django.http import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.urls.base import reverse

def hellow(request):

   return render(request,'hellow.html')

def friend(request):

   return render(request,'friend.html')

def data_from_db(request):
   obj = Students.objects.all()
   return render(request, 'index.html', {'obj1': obj})

def forms(request):
   if request.method == 'POST':
      form= Student_form(request.POST)
      if form.is_valid():
         form.save()
         return HttpResponseRedirect('/myapp/RegSuccessful/')
   else:
      form = Student_form()
   return render(request, 'form.html', {'for': form})

def RegSuccessful(request):

   return render(request,'RegSuccessful.html')
def registration(request):
   if request.method  == 'POST':
      form1= Student_form2(request.POST)
      if form1.is_valid():
         user = form1.cleaned_data['Username']
         pas = form1.cleaned_data['Password']
         frst = form1.cleaned_data['First_Name']
         last = form1.cleaned_data['Last_Name']
         emailid = form1.cleaned_data['Email_ID']
         User.objects.create_user(username=user, password=pas, first_name=frst, last_name=last,email=emailid)
         return HttpResponseRedirect('/myapp/RegSuccessful/')
   else:
      form1=Student_form2()
      return render(request, 'registration.html', {'for1': form1})
from myapp.forms import Student_form
def user_login(request):
   context={}
   if request.method == "POST":
      username = request.POST["username"]
      password = request.POST["password"]
      user = authenticate(request, username=username, password= password)
      if user:
         login(request, user)
         return HttpResponseRedirect("/myapp/success/")
      else:
         context["error"]="Invalid credentails !!"
         return render(request,"login.html", context)
   else:
      return render(request, "login.html", context)

def success(request):
   context = {}
   context['user']= request.user
   return render(request, "success.html", context)

def logout(request):
      return render(request, "logout.html")

#def home(request):
 #  return render(request, "hellow.html")