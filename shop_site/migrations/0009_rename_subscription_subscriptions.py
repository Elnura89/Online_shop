# Generated by Django 4.2.6 on 2023-11-09 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_site', '0008_subscription_delete_e_mails'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subscription',
            new_name='Subscriptions',
        ),
    ]