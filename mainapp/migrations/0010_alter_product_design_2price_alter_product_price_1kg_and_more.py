# Generated by Django 5.0.2 on 2024-02-29 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_ads_desc_3_ads_desc_4'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='design_2price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_1kg',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_2kg',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
    ]
