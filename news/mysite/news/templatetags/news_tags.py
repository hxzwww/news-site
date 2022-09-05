from django import template
from ..models import Category
from django.db.models import Count, F


register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.annotate(cnt=Count('news', filter=F('news__is_published'))).filter(cnt__gt=0)