from django.shortcuts import render
from django.urls import reverse_lazy

from catalog.models import Category, Product
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
class CatalogListView(ListView):
    model = Category
    extra_context = {
        'title': 'Тест магазин'
    }


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk'] = category_item.pk

        return context_data


class ProductCreateView(CreateView):
    model = Product
    fields = ('name','description','price','image','category')
    success_url = reverse_lazy('catalog:index')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name','description','price','image','category')
    success_url = reverse_lazy('catalog:index')

    def get_success_url(self):
        return reverse_lazy('catalog:category_list', kwargs={'pk': self.object.category.pk})


class ProductDeleteView(DeleteView):
    model = Product

    def get_success_url(self):
        return reverse_lazy('catalog:category_list', kwargs={'pk': self.object.category.pk})


class CatalogDetailView(DetailView):
    model = Product


class ProductTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'


def contacts(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']
        print(name, phone, message)
    return render(request, 'catalog/contacts.html')
