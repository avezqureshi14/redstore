# Generated by Django 4.0.2 on 2022-02-13 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0005_product_digital'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='delivery_days',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
