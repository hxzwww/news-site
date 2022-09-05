from django.shortcuts import render, get_object_or_404
from .forms import *
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import F
from django.contrib.auth.mixins import LoginRequiredMixin


# def default_news(request):
#     news = News.objects.filter(is_published=True)
#     context = {'news': news, 'title': 'Список новостей'}
#     return render(request, template_name='news/news.html', context=context)
class ShowNews(ListView):
    model = News
    template_name = 'news/news.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новости'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     return render(request, template_name='news/news.html', context={'news': news, 'title': category})
class ShowCategorizedNews(ShowNews):

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True, category_id=self.kwargs['category_id']).select_related('category')


def view_news(request, news_id):
    item = get_object_or_404(News, pk=news_id)
    item.views = F('views') + 1
    item.save()
    return render(request, template_name='news/view_news.html', context={'item': item})
# class ViewNews(DetailView):
#     model = News
#     pk_url_kwarg = 'news_id'
#     template_name = 'news/view_news.html'
#     context_object_name = 'item'


# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             return redirect(form.save())
#     else:
#         form = NewsForm()
#     return render(request, template_name='news/news_form.html', context={'form': form})
class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/news_form.html'
    login_url = '/admin/'