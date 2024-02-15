from django.http import HttpResponse    #here 'django' is a package, '.http' is a module, 'HttpResponse' is a class
                                         #(with this class we can create an HTTP response to return to the client/browser)
from django.shortcuts import render     #here '.shortcuts' is a module, 'render' is a function to render a template
from .models import Product


#Create your views here.
 #Let's create our 1st 'views' function, so we call it 'index' (by convention, we use 'index' to name the main page of an app)
  #this's the HTTP request that's passed to the 'views' function.
   #when we navigate to  '/products' (http://127.0.0.1:8000/products), our browser sends an HTTP request to our web server,
   #and then Django takes this HTTP request and sends it our 'views'(aka, 'index') function
   #and with this 'request' object, we can find info about the client
def index(request):
    products = Product.objects.all()    #other methods like .objects.filter() for filtering among products, .objects.get() for getting a single product, .objects.save() for inserting a new product or updating
    #return HttpResponse('Hi Customer')   #here we return an 'HTTPResponse' object. Now as an arg to the constructor, we pass 'Hi Customer'
    return render(request, 'index.html',                          #the 2nd arg is the filename of the index template
                {'products': products})                                 #the 3rd arg is a dictionary to which we add a key value pair (the value is the product objects we defined in L14),
                 #this 'products' (left) is a property                           #and the dictionary contains the data to be passed to the template 'index.html' (the 2nd arg),
                  #that's why we can access 'products' in L3 of 'index.html'      #the dictionary is called the 'context' as it provides data to use in our templates


 #URL mapping:
  #here we need to tell Django: whenever there's a request to  '/products' , we should call the 'index' function (so we need to map this URL to this function)
  #and then we create 'urls.py'


def new(request):
    return HttpResponse('New Products')

 #Models (create 'models.py')

 #Migrations
  #db.sqlite3   (Django supports all the db engines like SQLite, SQL Server, MySQL, Oracle, PostgreSQL, etc.)
  #'DB Browser for SQLite' https://sqlitebrowser.org/ offers a free app for opening SQLite databases
  #Now we need to create the migrations, so in Terminal, type:  python manage.py makemigrations
   #now let's register a 'Product' app in the list (L33-40) of 'INSTALLED_APPS' in 'pyshop/settings.py',
    #how to do that? - we go to 'products/apps.py', and at the end of the 'INSTALLED_APPS' list, we type 'products.apps.ProductsConfig'
  #Now we need to run migrate to generate the 'Product' table, again in Terminal, type: python manage.py migrate

 #Admin
  #in Terminal, type:  python manage.py createsuperuser
   #(Username: admin    Email: (own email))

 #Customizing the Admin
  #in 'admin.py', we create a class called 'ProductAdmin'



