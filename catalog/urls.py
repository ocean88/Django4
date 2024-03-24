from django.urls import path
from catalog.views import index, contacts, page_item
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/', page_item, name='item_detail')
]