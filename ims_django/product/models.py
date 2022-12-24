from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.TextField(blank=False, null=False)
    category = models.TextField(blank=False, null=False)
    price = models.FloatField(blank=False, null=False)
    stock = models.IntegerField(default=0, blank=False, null=False)
    description = models.TextField()
    available = models.BooleanField(default=True)