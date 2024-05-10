from django.db import models

# Create your models here.
class Purchases(models.Model):
    goods = models.CharField('Оборудование', max_length=50)
    amount = models.CharField('Количество', max_length=250)
    price = models.CharField('Цена за штуку', max_length=50)
    vendor = models.CharField('Поставщик', max_length=50)
    date = models.DateField('Дата поставки')

    def __str__(self):
        return self.goods

    class Meta:
        verbose_name = 'Закупки'
        verbose_name_plural = 'Закупки'