# Generated by Django 4.1.5 on 2023-02-23 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='order',
        ),
    ]
