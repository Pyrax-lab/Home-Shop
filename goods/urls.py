from django.urls import path
from . import views

app_name = "goods"

urlpatterns=[
    #path("", views.index, name="index"),
    path("search/", views.product_slugg, name="search"),
    path("<slug:category_slug>", views.product_slugg, name="prod_slug"),
    
    #path("product", views.product, name="product"),
    path("item/<slug:product_id>", views.item_id, name="item"),

    
]