from django.shortcuts import render

from catalog.models import Category, Product


# Create your views here.
def index(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Каталог - товаров'
    }
    return render(request, 'catalog/index.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']
        print(name, phone, message)
    return render(request, 'catalog/contacts.html')


def page_item(request, pk):
    item = Product.objects.get(pk=pk)
    context = {
        'object': item
    }
    return render(request, 'catalog/page_item.html', context)

