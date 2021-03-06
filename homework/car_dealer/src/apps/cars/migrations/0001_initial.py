# Generated by Django 3.0.6 on 2021-12-17 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Color',
                'verbose_name_plural': 'Colors',
            },
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.ImageField(blank=True, max_length=255, null=True, upload_to='static/pictures')),
                ('position', models.IntegerField()),
                ('metadata', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Picture',
                'verbose_name_plural': 'Pictures',
            },
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, unique=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.Brand')),
            ],
            options={
                'verbose_name': 'Model',
                'verbose_name_plural': 'Models',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engine_type', models.CharField(choices=[('straight', 'Straight'), ('inline', 'Inline'), ('flat', 'Flat'), ('v', 'V')], default='straight', max_length=75)),
                ('pollutant_class', models.CharField(blank=True, choices=[('class A+', 'A+'), ('class A', 'A'), ('class B', 'B'), ('class C', 'C'), ('class D', 'D'), ('class E', 'E'), ('class F', 'F'), ('class G', 'G')], default='class A+', max_length=40)),
                ('price', models.PositiveIntegerField(default=0)),
                ('category', models.CharField(blank=True, choices=[('Quadricycle', 'Quadricycle'), ('Mini', 'Mini'), ('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large'), ('Executive', 'Executive'), ('Luxury', 'Luxury'), ('Multi purpose', 'Multi purpose'), ('Sport utility', 'Sport utility')], default='Quadricycle', max_length=75)),
                ('fuel_type', models.CharField(choices=[('petrol', 'Petrol'), ('diesel', 'Diesel'), ('electric', 'Electric')], default='petrol', max_length=25)),
                ('slug', models.SlugField(max_length=75)),
                ('status', models.CharField(blank=True, choices=[('pending', 'Pending Car Sell'), ('published', 'Published'), ('sold', 'Sold'), ('archived', 'Archived')], default='pending', max_length=15)),
                ('doors', models.SmallIntegerField(default=4)),
                ('capacity', models.PositiveIntegerField(default=0)),
                ('gear_case', models.CharField(choices=[('mechanical', 'Mechanical'), ('automatic', 'Automatic'), ('variator', 'Variator'), ('robotic', 'Robotic')], default='automatic', max_length=75)),
                ('number', models.CharField(max_length=30)),
                ('sitting_place', models.PositiveSmallIntegerField(default=4)),
                ('first_registration_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('engine_power', models.PositiveIntegerField(default=0)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.Color')),
                ('dealer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.Model')),
                ('picture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cars.Picture')),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
            },
        ),
    ]
