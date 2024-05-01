import json
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = 'Export groups and their permissions'

    def handle(self, *args, **options):
        groups_data = []

        # Получаем все группы пользователей
        groups = Group.objects.all()

        # Проходимся по каждой группе пользователей
        for group in groups:
            group_permissions = list(group.permissions.values_list('codename', flat=True))
            group_data = {
                'name': group.name,
                'permissions': group_permissions
            }
            groups_data.append(group_data)

        # Записываем данные в JSON файл
        with open('groups_export.json', 'w') as json_file:
            json.dump(groups_data, json_file, indent=4)

        self.stdout.write(self.style.SUCCESS('Groups exported successfully to groups_export.json'))
