from django.db import models


class Product(models.Model):
    user_id = models.IntegerField(blank=True, null=True, verbose_name='USER_ID')
    date = models.DateField(blank=True, null=True, verbose_name='Дата')
    brand = models.CharField(max_length=255, blank=True, null=True, verbose_name='Бренд')
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название')
    status = models.IntegerField(blank=True, null=True, verbose_name='Статус')
    status_vikup = models.IntegerField(blank=True, null=True, verbose_name='Уведомление по выкупу [0-нет, 1-да]')
    status_dostavka = models.IntegerField(blank=True, null=True, verbose_name='Уведомление доставке [0-нет, 1-да]')
    description = models.TextField(max_length=255, blank=True, null=True, verbose_name='Описание')
    size = models.CharField(max_length=255, blank=True, null=True, verbose_name='Размер')
    price_dollar = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True,
                                       verbose_name='Стоимость в валюте')
    kurs = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, verbose_name='Курс выкупа')
    price_vikup = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True,
                                      verbose_name='Cтоимость выкупа')
    koef_vikup = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True,
                                     verbose_name='Коэффициент выкупа')
    price_vikup_client = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True,
                                             verbose_name='Cтоимость выкупа для клиента')
    dohod_vikup = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True,
                                      verbose_name='Доход по выкупу')
    ves = models.IntegerField(blank=True, null=True, verbose_name='Вес товара(г)')
    price_dostavki_za_kg = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True,
                                               verbose_name='Стоимость доставки за 1кг (1000г)')
    price_dostavki = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True,
                                         verbose_name='Cебестоимость доставки')
    koef_dostavka = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True,
                                        verbose_name='Коэффициент доставка')
    price_dostavki_klienty = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True,
                                                 verbose_name='Cтоимость доставки для клиента')
    dohod_dostavka = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True,
                                         verbose_name='Доход по доставке')
