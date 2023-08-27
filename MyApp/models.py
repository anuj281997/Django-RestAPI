from django.db import models

# Create your models here.
class Product(models.Model):
    pname = models.CharField(max_length=20)
    price = models.FloatField(default=100)
    brand = models.CharField(max_length=20)
    quantity = models.IntegerField()

    def __str__(self):
        return self.pname

    class Meta:
        db_table = "Product"