# Generated by Django 3.0.6 on 2021-12-27 13:27


from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('newemails', '0002_auto_20210810_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
