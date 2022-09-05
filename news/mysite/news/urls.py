from django.urls import path
from .views import *

urlpatterns = [
    path('', ShowNews.as_view(), name='news'),
    path('category/<int:category_id>/', ShowCategorizedNews.as_view(), name='category'),
    path('<int:news_id>/', view_news, name='view_news'),
    path('add-news/', CreateNews.as_view(), name='add_news'),
]
