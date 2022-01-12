# Generated by Django 3.0.6 on 2021-12-27 13:31


from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('newemails', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsletter',
            options={'verbose_name': 'Email', 'verbose_name_plural': 'Emails'},
        ),
        migrations.AddField(
            model_name='newsletter',
            name='email',
            field=models.EmailField(default='s@s', max_length=254),
            preserve_default=False,
        ),
    ]