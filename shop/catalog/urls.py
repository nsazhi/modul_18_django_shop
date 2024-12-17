from django.urls import path
from .views import IndexView, ProductListView, product_list, index


urlpatterns = [
    path('', index, name='index'),
    # path('', IndexView.as_view(), name='index'), # Метод as_view() подключает класс
    path('products/', product_list, name='product_list'), # Функциональное представление
    path('products-class/', ProductListView.as_view(), name='product_list_class'), # Классовое представление
]
