from django.db import models

# Create your models here.

class Payments(models.Model):
	name = models.CharField(max_length=255)
	branch = models.CharField(max_length=3)
	amount = models.FloatField()
	status = models.BooleanField()
	date = models.DateTimeField(null=True)



