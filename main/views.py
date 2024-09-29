from django.shortcuts import render

# Create your views here.
from goods.models import Category, Product # Импортируем Category из друго приложения

def index(request):

    data = {
        "product": Product.objects.all()
    }

    return render(request, "main/index.html", context=data)
  
def about(request):

    return render(request, "main/about.html")