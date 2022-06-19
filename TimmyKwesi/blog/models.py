from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
	Title 	= models.CharField(max_length=200)
	Text = models.TextField(blank=False)
	Author 	= models.ForeignKey(User,default=None, on_delete=models.CASCADE,)
	Created_date = models.DateTimeField(default=datetime.now, blank=True)
	Published_date = models.DateTimeField(auto_now=True, null=True)