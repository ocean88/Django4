from django.core.cache import cache
from catalog.models import Category
from config.settings import CACHE_ENABLED


def get_product_from_cache():
    """Получает данные из кеша, если кэш пуст, то выбирает из БД"""
    if not CACHE_ENABLED:
        return Category.objects.all()

    key = 'category_list'  # Создаем ключ для хранения
    category = cache.get(key)  # Пытаемся получить данные
    if category is None:
        category = Category.objects.all()
        cache.set(key, category)
    return category
