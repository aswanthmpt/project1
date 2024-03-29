# Generated by Django 5.0.2 on 2024-02-27 07:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_category_desc_2_category_image_3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='categoris')),
                ('image_2', models.ImageField(blank=True, upload_to='categoris')),
                ('image_3', models.ImageField(blank=True, upload_to='categoris')),
                ('banner', models.ImageField(blank=True, upload_to='categoris')),
                ('desc', models.TextField(blank=True)),
                ('desc_2', models.TextField(blank=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.subcategory'),
        ),
    ]
