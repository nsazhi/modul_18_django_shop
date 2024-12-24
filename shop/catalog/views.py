from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import Product

# Create your views here.
products = [
    {'id': 1, 'name': 'Смартфон Samsung Galaxy', 'category': 'телефоны', 'price': 15000},
    {'id': 2, 'name': 'Планшет Apple iPad', 'category': 'планшеты', 'price': 45000},
    {'id': 3, 'name': 'Наушники Sony WH-1000XM4', 'category': 'аксессуары', 'price': 25000},
    {'id': 4, 'name': 'Ноутбук Dell XPS 13', 'category': 'ноутбуки', 'price': 95000},
    {'id': 5, 'name': 'Смарт-часы Xiaomi Mi Band', 'category': 'аксессуары', 'price': 3000},
]


def index(request):
    # products = []
    products = [
        {"name": "Смартфон", "price": 15000},
        {"name": "Ноутбук", "price": 55000},
        {"name": "Планшет", "price": 25000},
    ]
    return render(request, 'catalog/index.html', {'products': products})


# class IndexView(View):
#     def get(self, request):
#         return HttpResponse("Добро пожаловать в интернет-магазин!")


# def product_list(request):
#     product_items = "<br>".join([f"{p['name']}: {p['price']} руб." for p in products])
#     return HttpResponse(product_items)


# class ProductListView(View):
#     def get(self, request):
#         product_items = "<br>".join([f"{p['name']}: {p['price']} руб." for p in products])
#         return HttpResponse(product_items)


# def product_list(request):
#     # Получаем параметр 'category' из строки запроса
#     category = request.GET.get('category')
#
#     # Если категория указана, фильтруем товары
#     if category:
#         filtered_products = [product for product in products if product['category'] == category]
#     else:
#         filtered_products = products
#
#     # Передаем товары в шаблон
#     return render(request, 'catalog/product_list.html', {'products': filtered_products})


def add_product(request):
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.POST.get('name')
        category = request.POST.get('category')
        price = request.POST.get('price')

        # Добавляем новый товар в список
        products.append({
            'id': len(products) + 1,
            'name': name,
            'category': category,
            'price': int(price),
        })

        # Перенаправляем на список товаров
        return redirect('product_list')  # Имя маршрута списка товаров

    # Если GET-запрос, отображаем форму
    return render(request, 'catalog/add_product.html')


def product_list(request):
    products = Product.objects.all() # Получаем все товары из базы данных
    return render(request, 'catalog/product_list.html', {'products': products})


def phones_list(request):
    # Фильтрация товаров по категории "Телефоны"
    products = Product.objects.filter(category__name="Телефоны")
    return render(request,'catalog/phones_list.html',{'products': products})