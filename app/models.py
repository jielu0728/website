from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Marques(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.TextField()
	imgpath = models.TextField()
	web = models.TextField()