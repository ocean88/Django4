from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import CatalogListView, CatalogDetailView, ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView, ProductTemplateView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', CatalogListView.as_view(), name='index'),
    path('category/<int:pk>/', ProductListView.as_view(), name='category_list'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('contacts/', ProductTemplateView.as_view(), name='contacts'),
    path('<int:pk>/', cache_page(60)(CatalogDetailView.as_view()), name='item_detail')
]