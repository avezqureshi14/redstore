# Generated by Django 4.0.2 on 2022-02-19 02:55

from django.db import migrations, models
import eapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0026_alter_product_image_delete_addcat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to=eapp.models.filepath),
        ),
    ]
