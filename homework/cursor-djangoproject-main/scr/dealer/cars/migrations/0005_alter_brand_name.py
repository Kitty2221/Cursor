# Generated by Django 3.0.6 on 2021-12-25 13:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('cars', '0004_auto_20210806_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=70, unique=True),
        ),
    ]