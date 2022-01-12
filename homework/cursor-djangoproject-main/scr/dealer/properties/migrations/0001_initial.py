# Generated by Django 3.0.6 on 2021-12-27 15:27


from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('cars', '0003_auto_20210806_1600'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=120)),
                ('name', models.CharField(max_length=50)),
                ('carproperty', models.ManyToManyField(related_name='carpropery', to='cars.Car')),
            ],
        ),
    ]