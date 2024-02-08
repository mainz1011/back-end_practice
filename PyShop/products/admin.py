from django.contrib import admin
from .models import Product, Offer


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
#all the functionalities of 'ProductAdmin' are inherited from 'admin.ModelAdmin'
 #in the body of the class 'ProductAdmin', we can overwrite/change some of the functionalities.
  #for example, the class 'ProductAdmin' has an attribute 'list_display' which specifies the columns that should be visible in the 'Product' table.
   #so we set the attribute 'list_display' to a tuple in which we add one or more attributes of the 'Product' class.


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')
# Register your models here.
admin.site.register(Product, ProductAdmin)     #here we pass the class 'Product' as the arg. And we pass the 2nd arg 'ProductAdmin'
 #here 'admin' is an object, which has an attribute called 'site' (and 'site' is an object itself which has a method called 'register')
 #we're telling Django to manage 'Product' in the 'admin' area.
admin.site.register(Offer, OfferAdmin)

 #Templates  5:48