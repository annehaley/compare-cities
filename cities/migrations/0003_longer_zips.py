# Generated by Django 3.2.13 on 2022-06-04 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0002_city_economics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='zips',
            field=models.CharField(max_length=2000),
        ),
    ]