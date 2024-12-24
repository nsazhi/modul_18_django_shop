from django.urls import path
from . import views


urlpatterns = [
    # path('', index, name='index'),
    # path('', IndexView.as_view(), name='index'), # Метод as_view() подключает класс
    # path('products/', product_list, name='product_list'), # Функциональное представление
    # path('products-class/', ProductListView.as_view(), name='product_list_class'), # Классовое представление
    path('products/', views.product_list, name='product_list'),
    path('add/', views.add_product, name='add_product'),
    path('phones/', views.phones_list, name='phones_list'),
]
