# Generated by Django 4.0.2 on 2022-02-22 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0031_rename_image_product_image1_product_image2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
