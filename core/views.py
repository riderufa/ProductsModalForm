import json
import datetime

from django.http import JsonResponse
from django.shortcuts import render

from core.models import Product


def index(request):
    context = {}
    return render(request, 'index.html', context)


def save_products(request):
    products = request.POST.getlist('products[]')[0]
    products = json.loads(products)
    for product in products:
        print(product)
        date = product['date'] if product['date'] != '' else datetime.date.today()
        status = product['status'] if product['status'] != '' else 0
        price_dollar = product['currency_price'] if product['currency_price'] != '' else 0
        kurs = product['redemption_rate'] if product['redemption_rate'] != '' else 0
        koef_vikup = product['redemption_ratio'] if product['redemption_ratio'] != '' else 0
        ves = product['weight'] if product['weight'] != '' else 0
        price_dostavki = product['send_price'] if product['send_price'] != '' else 0
        koef_dostavka = product['send_ratio'] if product['send_ratio'] != '' else 0
        Product.objects.create(
            date=date,
            brand=product['brand'],
            name=product['title'],
            status=status,
            description=product['description'],
            size=product['size'],
            price_dollar=price_dollar,
            kurs=kurs,
            koef_vikup=koef_vikup,
            ves=ves,
            price_dostavki=price_dostavki,
            koef_dostavka=koef_dostavka,
        )
    return_dict = dict()
    return JsonResponse(return_dict)
