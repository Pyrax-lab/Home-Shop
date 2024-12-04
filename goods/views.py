from unicodedata import category
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator

from django.db.models import Q

from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector, SearchHeadline

# Create your views here.
from goods.models import Product, Category



def product_slugg(request, category_slug=None):

    order = request.GET.get("order_by", "default")
    page = request.GET.get("page",1)
    query_search = request.GET.get("q")

    if category_slug == "all":
        products_category = Product.objects.all()
        
        
    elif query_search:

        # 1. Фильтрация по id 
        if query_search.isdigit() and len(query_search) <= 6:
            result = Product.objects.filter(id = int(query_search))
            products_category = result

        elif not query_search.isdigit():
           
        # ------- 1-ая Версия поиска на сайте -------
        #     words = [word for word in query_search.split() if len(word) > 2]
        #     q_object_search = Q()
        #     for token in words:
        #     # & - and, | - or
        #         q_object_search |= Q(description__icontains = token)  # тоесть мы добавляем в обьект q_object_search другие обьекты которые имеют знак или тоесть добавилось слово например стол или стул или кровать 
        #         q_object_search |= Q(name__icontains=token)
        #     products_category = Product.objects.filter(q_object_search)

        # ИСПОЛЬЗУЮТСЯ ТОЛЬКО С POSTGRESQL
            
        # ------- 2-рая Версия поиска на сайте (для использование __search нужно в settings INSTALED_APPS добавить django.contrib.postgres) --------   
            #products_category = Product.objects.filter(name__search = query_search)
        

        # ------- 3-ия версия поиска на сайте -------
            vector = SearchVector("name", "description") # создаём вектор и поля по которым будет вестись поиск
            query = SearchQuery(query_search) # Cоздаем запрос
            result = Product.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by("-rank") # Сдесь создаем анотированный запрос с добавлением к каждому обьекту поле rank тоесть ранг по которому оценивыается релевантность с последуший филтрацие этого ранга чтоб был больше > 0 с сортировкой по рангу


            result = result.annotate(
                headline=SearchHeadline("name",
                                        query,
                                        start_sel='<span style="background-color: orange;">',
                                        stop_sel="</span>",
                )
            )#headline — будет содержать название продукта (name) с подсвеченными совпадениями по поисковому запросу. которые используется в html шаблонах
            


            result = result.annotate(
                bodyline=SearchHeadline("description",
                                        query,
                                        start_sel='<span style="background-color:orange;">',
                                        stop_sel="</span>",
                )
            )#bodyline — будет содержать описание продукта (description) с такими же выделениями.

            products_category = result

    else:
        products_category = get_list_or_404(Product.objects.filter(category__slug = category_slug))

   


    
    

    if order != 'default':
        products_category = products_category.order_by(order)

    

    goods = Paginator(products_category, 3)
    
    products_category = goods.page(page)
    
    


    data = {
        "product" : products_category,
        "page_range": goods.page_range,
        "url_page": category_slug,
        
        
    }

    return render(request, "goods/catalog.html", context=data)

# def product(request):
#     #return HttpResponse("Hello product")
#     return render(request, "goods/product.html")


def item_id(request, product_id):

    #item = Product.objects.get(slug = product_id)

    item = Product.objects.get(slug = product_id)

    return render(request, "goods/product.html", context={"item":item})