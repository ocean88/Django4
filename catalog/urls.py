from django.urls import path
from catalog.views import contacts, CatalogListView, CatalogDetailView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', CatalogListView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/', CatalogDetailView.as_view(), name='item_detail')
]