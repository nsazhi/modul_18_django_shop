from django.urls import path
from . import views
from .views import IndexView
from .views import ProductListView, product_list

# urlpatterns = [
#     path('', views.index, name='index'),  # Главная страница
# ]

urlpatterns = [
    path('', IndexView.as_view(), name='index'), # Метод as_view() подключает класс
    path('products/', product_list, name='product_list'), # Функциональное представление
    path('products-class/', ProductListView.as_view(), name='product_list_class'), # Классовое представление
]
