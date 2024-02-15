from django.db import models


# Create your models here.
#create a class called 'Product' and for which we define a few attributes
class Product(models.Model):     #in the module 'models', we have a class called 'Model' which defines all the common characteristics & behaviors for models in the Django app.
                                 #e.g., store/read/delete these models in the db, which are all the common operations we're gonna perform on the 'Model' object
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=16)
    description = models.CharField(max_length=255)
    discount = models.FloatField()
