from django.db import models

# Create your models here.

class Products(models.Model):
    picture = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    quantity = models.IntegerField()


def __str__(self):
    return self.description


class Cart(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()





