# Generated by Django 4.1.3 on 2022-12-06 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerseapp', '0003_product_available'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='dscrptn',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='dscrptn',
            new_name='description',
        ),
    ]
