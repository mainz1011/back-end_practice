#the filename 'apps' is confusing. It's actually a config module, that's why we have a class called 'ProductsConfig'
from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
