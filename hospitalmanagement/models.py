from __future__ import unicode_literals
from django.db import models

#create your models here


#   doctor Model
class Doctor(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    desgination = models.CharField(max_length=50)
    adress = models.CharField(max_length=50)

# patient model
class Patient(models.Model):
    patient_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    adress = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)

# appointment model
class Appointment (models.Model):
    doctor_id = models.ForeignKey(
        Doctor, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(
        Patient,  on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    time = models.CharField(max_length=50)
