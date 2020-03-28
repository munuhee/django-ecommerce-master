# Generated by Django 2.2.10 on 2020-03-18 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_subcategory_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=20)),
                ('Last_Name', models.CharField(max_length=20)),
                ('Birth_Day', models.DateField()),
                ('Email', models.EmailField(max_length=254)),
                ('Message', models.TextField()),
            ],
        ),
    ]