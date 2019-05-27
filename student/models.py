from django.db import models

# Create your models here.
class Students(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	date_of_birth=models.DateField()
	registeration_number=models.CharField(max_length=50)
	place_of_residence=models.CharField(max_length=50)
	phone_number=models.CharField(max_length=50)
	email=models.EmailField(max_length=50)
	guardian_no=models.CharField(max_length=50)
	id_no=models.CharField(max_length=50)
	date_joined=models.IntegerField()


