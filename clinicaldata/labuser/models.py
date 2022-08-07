from django.db import models
Gender=[('Male','MALE'),('Female','FEMALE')]
# Create your models here.
class patient(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    age=models.IntegerField()
    gender=models.CharField(max_length=10,choices=Gender)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    email=models.EmailField(null=True)

class patientclinicaldata(models.Model):
    height=models.FloatField()
    height_date=models.DateTimeField(auto_now_add=True)
    weight=models.FloatField()
    weight_date=models.DateTimeField(auto_now_add=True)
    bp=models.PositiveIntegerField()
    bp_date=models.DateTimeField(auto_now_add=True)
    heartrate=models.PositiveIntegerField()
    heartrate_date=models.DateTimeField(auto_now_add=True)
    Patient=models.OneToOneField(patient,on_delete=models.CASCADE)
