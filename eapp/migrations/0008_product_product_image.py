# Generated by Django 4.0.2 on 2022-02-14 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0007_customer_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]