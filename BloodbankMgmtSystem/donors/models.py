from django.db import models

# Create your models here.

class Donors(models.Model):
  Name = models.CharField(max_length=255)
  MobileNumber = models.IntegerField()
  Age = models.CharField(max_length=255)
  BloodGroup = models.CharField(max_length=255)
  Address = models.CharField(max_length=255)
  Volumedonated = models.CharField(max_length=255)
  Dateofdonation = models.DateField()

  def __str__(self):
    return f"{self.Name} {self.BloodGroup}"

