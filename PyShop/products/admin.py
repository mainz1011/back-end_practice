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

 #Templates
  #now the 'index' function in 'views.py' returns the 'Hi Customer' msg, but we wanna replace it with the info of products in our db.
   #so, the 1st step: to get the products stored in our db (e.g., using one of the methods '.objects.all' which returns all the products we have in our db);
       #the 2nd step: format them with an HTML template to present to the user.
        #Now: in 'views.py', import the 'Product' class from the 'models' module in the current folder, and in the 'index' function, create a variable 'products': 'products = Product.objects.all()'
        #and then, create a new directory/folder 'templates' in the current folder (from which Django looks for to load templates)
        #now in the 'templates' folder we need to create a template 'index.html' for the 'index' function
         #and then in the 'index.html' template we replace the items with our products

 #Adding Bootstrap

 #Rendering Cards

 #Final touches
