# Generated by Django 5.0.3 on 2024-04-09 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0002_alter_currency_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='currency',
            options={'ordering': ['symbol', '-added_at'], 'verbose_name': 'Currency', 'verbose_name_plural': 'Currencies'},
        ),
        migrations.AlterUniqueTogether(
            name='currency',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='currency',
            name='current_price',
        ),
        migrations.RemoveField(
            model_name='currency',
            name='name',
        ),
    ]
