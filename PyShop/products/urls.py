#by convention, we should define a variable called 'urlpatterns' and set it to a list object
 #and in the list object below, we map various urls to their 'views' functions (or: map the funtion to the url endpoint)
 #so, to reference a url, we need to import the 'path' function
from django.urls import path
from . import views
#here . means the current folder. We import the 'views' module from 'views.py'
#and the 'views' module ends up being an object, see below, and here we wanna reference the 'index' function
 #code: views.index()

#the 1st arg is a string that specifies our url endpoint
                                #here we pass an empty string '' that has no characters inside and it represents the root of this app
                                 #in this case, the root is '/products'
                              #the 2rd arg 'view.index' specifies the 'views' function, see L5-7
                               #note:here we shouldn't call the 'index' function, we simply pass a reference to it as Django will call it at runtime (when the client sends an HTTP request to the server)
   #here it tells Django: map the roots url ''  to the 'views.index' function
urlpatterns = [
    path('', views.index),
    path('new', views.new)
]

