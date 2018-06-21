# -*- coding: UTF-8 -*-
from django.db import models


class Menu(models.Model):
    CATE_CHOICES = (
        ('cold', '冷菜类' ),
        ('soup', '汤煲类',),
        ('meat', '荤菜小炒'),
        ('vege', '素菜小炒'),
        ('rice', '主食'),
    )
    name = models.CharField(max_length=15, null=False, unique=True)
    price = models.DecimalField(max_digits=4, decimal_places=2, null=False)
    category = models.CharField(max_length=20, choices=CATE_CHOICES, default='cold', null=True)
    image = models.ImageField(upload_to='img', max_length=255, null=True)


class Order(models.Model):
    m_id = models.ForeignKey(Menu, on_delete=True)
    amount = models.IntegerField(default=0)


class Ticket(models.Model):
    o_id = models.ManyToManyField(Order)
    tot_price = models.DecimalField(max_digits=6, decimal_places=2)