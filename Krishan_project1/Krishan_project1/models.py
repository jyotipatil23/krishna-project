
from django.db import models
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.models import User

class Krishna_Project(models.Model) :
    Name = models.CharField(max_length=100)
    Email_ID = models.EmailField()
    country_name = models.CharField(max_length=60)
    phone_no = models.IntegerField()
    message = models.CharField(max_length=400)

def __str__(self):
      return u'%s, %s, %s, %s'%(self.Name, self.country_name, self.Email_ID, self.phone_no, self.message)
