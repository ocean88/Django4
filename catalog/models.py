from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='product_images/', verbose_name="Изображение", **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name="Категория")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="Обновлено")

    def __str__(self):
        return f"Название: {self.name}"

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-created_at',]


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return f'Название: {self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']