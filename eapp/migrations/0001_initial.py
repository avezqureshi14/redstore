# Generated by Django 4.0.2 on 2022-02-05 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading1', models.CharField(max_length=200)),
                ('description1', models.CharField(max_length=180)),
                ('heading2', models.CharField(max_length=200)),
                ('description2', models.CharField(max_length=180)),
                ('ReviewName', models.CharField(max_length=200)),
                ('ReviewDescription', models.CharField(max_length=180)),
                ('aboutUs', models.CharField(max_length=230)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='eapp/images')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
    ]
