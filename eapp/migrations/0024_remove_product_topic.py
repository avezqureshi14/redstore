# Generated by Django 4.0.2 on 2022-02-18 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0023_remove_product_digital'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='topic',
        ),
    ]
