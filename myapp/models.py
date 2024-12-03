from django.db import models

# Create your models here.
class Invoice(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    item=models.CharField(max_length=200)
    summary=models.TextField()