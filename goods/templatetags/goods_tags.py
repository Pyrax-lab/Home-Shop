# Создаем наш шаблоный тег позволяющий показывать Список категории на любой страничке на сайте
from goods.models import Category

from django import template

register = template.Library()

@register.simple_tag()
def load_category():
    return Category.objects.all()

