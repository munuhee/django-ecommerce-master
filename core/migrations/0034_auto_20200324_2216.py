# Generated by Django 2.2.10 on 2020-03-24 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_remove_contact_form_upload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='discount_price_ar',
        ),
        migrations.RemoveField(
            model_name='item',
            name='discount_price_en',
        ),
        migrations.RemoveField(
            model_name='item',
            name='price_ar',
        ),
        migrations.RemoveField(
            model_name='item',
            name='price_en',
        ),
    ]