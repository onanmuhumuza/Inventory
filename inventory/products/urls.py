from django.urls import path
from .views  import  index,product_list_create

urlpatterns=[
    path("", index, name="home"),
    path("create", product_list_create, name="create_list"),
]