# Generated by Django 3.2.9 on 2021-12-12 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish', models.CharField(max_length=64)),
                ('ingredients', models.TextField()),
            ],
            options={
                'verbose_name': 'Dish',
                'verbose_name_plural': 'Dishes',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('post', models.CharField(choices=[('administrator', 'Administrator'), ('bartender', 'Bartender'), ('waiter', 'Waiter'), ('chef', 'Chef'), ('cleaner', 'Cleaner')], max_length=50)),
                ('phone', models.IntegerField(blank=True, max_length=20)),
            ],
            options={
                'verbose_name': 'Staff',
                'verbose_name_plural': 'Staff',
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('opened', 'Opened'), ('closed', 'Closed')], default='opened', max_length=64)),
                ('name', models.CharField(max_length=64)),
                ('owner', models.CharField(max_length=64)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='project_restaurant.city')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_restaurant.country')),
                ('staff', models.ManyToManyField(to='project_restaurant.Staff')),
            ],
            options={
                'verbose_name': 'Restaurant',
                'verbose_name_plural': 'Restaurants',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('season_dish', models.CharField(blank=True, choices=[('winter', 'Winter'), ('spring', 'Spring'), ('summer', 'Summer'), ('autumn', 'Autumn')], default='summer', max_length=64)),
                ('list_of_dishes', models.ManyToManyField(to='project_restaurant.Dish')),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menus',
            },
        ),
    ]