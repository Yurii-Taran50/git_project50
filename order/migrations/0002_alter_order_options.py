# Generated by Django 5.1.7 on 2025-04-16 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created',), 'verbose_name': 'Замовлення', 'verbose_name_plural': 'Замовлення'},
        ),
    ]
