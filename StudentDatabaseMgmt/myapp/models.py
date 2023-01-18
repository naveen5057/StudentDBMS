from django.db import models
from django.contrib.auth.models import User
class Students(models.Model):

    First_Name = models.CharField(max_length=20, blank=True, null=True)
    Last_Name = models.CharField(max_length=20, blank=True, null=True)
    Employee_ID = models.CharField(max_length=20, blank=True, null=True)
    Country = models.CharField(max_length=20, blank=True, null=True)
    Phone_Number = models.CharField(max_length=45, blank=True, null=True)
    Email_ID = models.CharField(max_length=45, blank=True, null=True)
    User_Name = models.CharField(max_length=20, blank=True, null=True)
    Password = models.CharField(max_length=20, blank=True, null=True)


    def __str__(self):
        return self.First_Name
