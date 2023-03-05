from django.db import models

# Create your models here.
from django.db import models
import uuid

# Create your models here.
class AllUsers(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.first_name
    

class contactModel(models.Model):
    full_name=models.CharField(max_length=50)
    relationship=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone_number=models.EmailField(max_length=14)
    address=models.EmailField(max_length=50)

    def __str__(self):
        return self.full_name
    class Meta:
        db_table = 'contactModel'
