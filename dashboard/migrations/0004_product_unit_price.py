# Generated by Django 4.1.7 on 2023-04-08 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_product_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='unit_price',
            field=models.PositiveBigIntegerField(null=True),
        ),
    ]
