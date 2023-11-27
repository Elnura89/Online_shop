# Generated by Django 4.2.6 on 2023-11-23 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop_site', '0010_shoppingcart'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productObject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_site.products')),
            ],
        ),
    ]
