from django.urls import path
from .views import product_list, add_product # index, IndexView, ProductListView


urlpatterns = [
    # path('', index, name='index'),
    # path('', IndexView.as_view(), name='index'), # Метод as_view() подключает класс
    # path('products/', product_list, name='product_list'), # Функциональное представление
    # path('products-class/', ProductListView.as_view(), name='product_list_class'), # Классовое представление
    path('', product_list, name='product_list'),
    path('add/', add_product, name='add_product'),
]
