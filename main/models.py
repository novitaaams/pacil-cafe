from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)
    description = models.TextField()

