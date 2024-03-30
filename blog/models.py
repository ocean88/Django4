from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(verbose_name='Текст статьи')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
