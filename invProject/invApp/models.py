from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      dels.AutoField(primary_key=True)
    name = models.CharField(max=100)
    sku = models.CharField(max=100, unique=True) # Stock keeping unit
    price = models.FloatField()
    quantity = models.IntegerField()
    Supplier = models.CharField(max=100)

    def __str__(self):
        return self.name