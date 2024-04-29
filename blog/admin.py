from django.contrib import admin
from django.utils.safestring import mark_safe

from blog.models import Blog


# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'creation_date')
    list_filter = ('is_published', 'creation_date')
    search_fields = ('title', 'body')
    readonly_fields = ('creation_date',)  # Если вы хотите, чтобы поле creation_date было только для чтения

    # Если вы хотите отобразить поле preview в админке как превью, вы можете переопределить метод get_preview
    def get_preview(self, obj):
        if obj.preview:
            return mark_safe(f'<img src="{obj.preview.url}" width="100" height="100">')
        return "No Preview"

    get_preview.short_description = "Preview"  # Название столбца в админке