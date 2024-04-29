from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.forms import inlineformset_factory, RadioSelect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from catalog.models import Category, Product, Version
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import VersionForm


def get_active_version(product):
    active_version = Version.objects.filter(product=product, is_active=True).first()
    return active_version


class ModeratorAccessMixin(AccessMixin):
    """
    Миксин для проверки доступа модератора или выше к неопубликованным материалам.
    """
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.groups.filter(name__in=['moderator']).exists():
                return super().dispatch(request, *args, **kwargs)
            else:
                # Пользователь не в группе "модератор" или "администратор",
                # поэтому мы фильтруем только опубликованные материалы
                self.queryset = self.get_queryset().filter(is_published=True)
                return super().dispatch(request, *args, **kwargs)
        else:
            return self.handle_no_permission()

    def test_func(self):
        user = self.request.user
        return user.is_superuser or user.groups.filter(name='moderator').exists()


# Create your views here.
class CatalogListView(ListView):
    model = Category
    extra_context = {
        'title': 'Тест магазин'
    }


class ProductListView(LoginRequiredMixin,ModeratorAccessMixin, ListView):
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        # Добавляем логику для получения активной версии для каждого продукта
        products = context_data['products']
        for product in products:
            active_version = get_active_version(product)
            product.active_version = active_version

        # Добавляем логику для получения информации о категории, если требуется
        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk'] = category_item.pk

        # Добавляем флаг для модераторов, указывающий, является ли текущий пользователь модератором
        context_data['is_moderator'] = self.request.user.groups.filter(name='moderator').exists()

        return context_data


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        if self.object is not None:
            self.object.owner = self.request.user
            self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('catalog:index')  # Redirect to some other URL


class ProductUpdateView(LoginRequiredMixin, ModeratorAccessMixin, UpdateView):
    model = Product
    form_class = ProductForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormSet = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormSet(self.request.POST, instance=self.object)
        else:
            formset = VersionFormSet(instance=self.object)
        context_data['formset'] = formset
        active_version = get_active_version(self.object)
        context_data['active_version'] = active_version
        return context_data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            formset.save()
        return super().form_valid(form)

    def get_form_class(self):
        user = self.request.user
        if user.is_superuser or user.groups.filter(name='moderator').exists():
            return ProductModeratorForm
        else:
            return ProductForm

    def get_success_url(self):
        return reverse_lazy('catalog:index')  # Redirect to some other URL

    def test_func(self):
        product = self.get_object()
        user = self.request.user
        return product.owner == user or user.is_superuser or user.groups.filter(name='moderator').exists()


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
