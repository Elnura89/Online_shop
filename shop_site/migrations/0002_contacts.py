# Generated by Django 4.2.6 on 2023-10-14 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('firstname', models.CharField(max_length=250)),
                ('lastname', models.CharField(max_length=250)),
                ('number', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('message', models.CharField(max_length=250)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]