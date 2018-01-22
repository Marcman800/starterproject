from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=250)
	description = models.CharField(max_length=500, default=None)
	timestamp = models.DateTimeField(auto_now=True)
