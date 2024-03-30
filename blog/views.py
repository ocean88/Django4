from django.views.generic import CreateView
from django.views.generic.list import ListView
from blog.models import Blog
from django.urls import reverse_lazy


# Create your views here.


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'body')
    success_url = reverse_lazy('catalog:index')


class BlogListView(ListView):
    model = Blog


class BlogDetailView(ListView):
    model = Blog
