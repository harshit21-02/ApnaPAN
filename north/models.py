from asyncio.windows_events import NULL
from curses.ascii import NUL
from distutils.command.upload import upload
import email
from email.policy import default
from tkinter import CENTER
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import ImageField
from django.contrib.auth.models import User 

from django.db import models
from django.utils import timezone
import os
from uuid import uuid4
# # Create your models here.

def path_and_rename(instance, filename):
        upload_to = 'static/'
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid4().hex, ext)
        return os.path.join(upload_to,str(instance.category), filename)

class nculture(models.Model):
    pid=models.BigAutoField(primary_key=True)
    pname=models.TextField('PRODUCT NAME',max_length=30,default='')
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    image=models.ImageField(upload_to=path_and_rename,null=True,blank=True)
    category = models.TextField('category',max_length=100)

    def __str__(self):
        return self.pname
