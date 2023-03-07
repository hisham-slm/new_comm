from django.db import models
from common.models import Customer
from seller.models import Product

# Create your models here.


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.BigIntegerField()

    class Meta:
        db_table = 'cart'
