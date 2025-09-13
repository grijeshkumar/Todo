from django.db import models

# Create your models here.

class Transaction(models.Model):
   title = models.CharField(max_length=250)
   description = models.CharField(max_length=100)
   created_at = models.DateTimeField(auto_now=True)
   update_at = models.DateTimeField(auto_now_add=True)
