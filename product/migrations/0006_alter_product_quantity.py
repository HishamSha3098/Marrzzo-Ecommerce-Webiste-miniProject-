# Generated by Django 4.1.5 on 2023-03-04 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_delete_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]
