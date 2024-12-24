from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Название категории

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)  # Название товара
    description = models.TextField(blank=True)  # Описание товара (опционально)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена товара
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Связь с категорией
    created_at = models.DateTimeField(auto_now_add=True)  # Дата добавления товара

    def __str__(self):
        return self.name
