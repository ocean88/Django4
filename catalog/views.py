from django.shortcuts import render
from catalog.models import Category, Product
from django.views.generic import ListView, DetailView


# Create your views here.
class CatalogListView(ListView):
    model = Product
    template_name = 'catalog/index.html'


def contacts(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']
        print(name, phone, message)
    return render(request, 'catalog/contacts.html')


class CatalogDetailView(DetailView):
    model = Product
    template_name = 'catalog/page_item.html'



