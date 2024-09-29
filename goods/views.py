from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from goods.models import Product

def index(request):

    product = Product.objects.all()

    data={
        
        "product": product,
    
    }
    
    return render(request, "goods/catalog.html", context=data)

def product(request):
    #return HttpResponse("Hello product")
    return render(request, "goods/product.html")


