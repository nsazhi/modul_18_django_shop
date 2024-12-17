from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def index(request):
    return render(request, 'catalog/index.html')

class IndexView(View):
    def get(self, request):
        return HttpResponse("Добро пожаловать в интернет-магазин!")


products = [
    {"name": "Смартфон", "price": 15000},
    {"name": "Ноутбук", "price": 55000},
    {"name": "Планшет", "price": 25000},
]

def product_list(request):
    product_items = "<br>".join([f"{p['name']}: {p['price']} руб." for p in products])
    return HttpResponse(product_items)

class ProductListView(View):
    def get(self, request):
        product_items = "<br>".join([f"{p['name']}: {p['price']} руб." for p in products])
        return HttpResponse(product_items)