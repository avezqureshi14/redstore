# Generated by Django 4.0.2 on 2022-02-18 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0024_remove_product_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddCat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='eapp.topic')),
            ],
        ),
    ]
