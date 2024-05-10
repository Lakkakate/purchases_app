# Generated by Django 4.2.11 on 2024-05-07 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Purchases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods', models.CharField(max_length=50, verbose_name='Оборудование')),
                ('amount', models.CharField(max_length=250, verbose_name='Количество')),
                ('price', models.CharField(max_length=50, verbose_name='Цена за штуку')),
                ('vendor', models.CharField(max_length=50, verbose_name='Поставщик')),
                ('date', models.DateField(verbose_name='Дата поставки')),
            ],
        ),
    ]