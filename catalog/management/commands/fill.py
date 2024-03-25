from django.core.management import BaseCommand
from catalog.models import Product, Category
import json


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Очистить базу данных
        Category.objects.all().delete()
        Product.objects.all().delete()

        # Загрузить данные из data.json в базу данных
        with open('data.json', 'r', encoding='UTF-8') as f:
            data = json.load(f)

            # Создать категории
            for item in data:
                if item['model'] == 'catalog.category':
                    Category.objects.create(id=item['pk'], name=item['fields']['name'], description=item['fields']['description'])

            # Создать продукты
            for item in data:
                if item['model'] == 'catalog.product':
                    category_id = item['fields']['category']
                    category = Category.objects.get(pk=category_id)
                    Product.objects.create(id=item['pk'], name=item['fields']['name'], description=item['fields']['description'], category=category, price=item['fields']['price'], created_at=item['fields']['created_at'], last_updated=item['fields']['last_updated'])

        print("Data loaded successfully.")
