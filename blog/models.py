from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(verbose_name='Текст статьи')
    views_count = models.IntegerField(default=0, verbose_name='Просмотры')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    slug = models.CharField(max_length=200, verbose_name='slug', **NULLABLE)
    preview = models.ImageField(upload_to='blog_previews/', verbose_name='Превью', **NULLABLE)
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', **NULLABLE)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
