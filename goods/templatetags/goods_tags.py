# Создаем наш шаблоный тег позволяющий показывать Список категории на любой страничке на сайте
from django.utils.http import urlencode
from goods.models import Category

from django import template

register = template.Library()


# cоздаем тег для отображение коментариев 
@register.simple_tag()
def load_category():
    return Category.objects.all()


@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context["request"].GET.dict()
    query.update(kwargs)
    return urlencode(query)