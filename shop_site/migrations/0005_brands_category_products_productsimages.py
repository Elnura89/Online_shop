# Generated by Django 4.2.6 on 2023-10-21 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop_site', '0004_blogs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='')),
                ('price', models.FloatField()),
                ('color', models.CharField(max_length=250)),
                ('weight', models.FloatField()),
                ('barcode', models.CharField(max_length=250)),
                ('brandObject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_site.brands')),
                ('categoryObject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_site.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductsImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('productObject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_site.products')),
            ],
        ),
    ]
