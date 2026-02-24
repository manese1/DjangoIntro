from django.db import models

# Create your models here.
class Product(models.Model):
    productname = models.CharField(max_length = 100)
    quantity = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    def __str__(self):
        return self.productname