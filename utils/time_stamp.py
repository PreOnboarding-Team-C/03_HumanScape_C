<<<<<<< HEAD
from django.db.models import Model, DateTimeField


class TimeStampModel(Model):
    created_datetime = DateTimeField(auto_now_add=True)
    
=======
from django.db import models

class TimeStampModel(models.Model):
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

>>>>>>> 0bb680528e5db086dd9e37128e9e35d4e436d0ce
    class Meta:
        abstract = True
