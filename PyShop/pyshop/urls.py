#This 'urls.py' module is like the root/parent urls module in our Django project.
"""
URL configuration for pyshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include   #we also need to import the 'include' function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls'))
]
 #the 1st arg tells Django that: delegate any urls starting with 'admin/' to the 'admin' app (admin.site.urls)
 #here we should also tell Django about our 'products' app, so once again we call the 'path' function in L23


