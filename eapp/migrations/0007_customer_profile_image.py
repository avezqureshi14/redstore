# Generated by Django 4.0.2 on 2022-02-14 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0006_product_delivery_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
