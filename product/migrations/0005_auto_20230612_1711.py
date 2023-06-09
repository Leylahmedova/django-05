# Generated by Django 3.2 on 2023-06-12 13:11

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='company_image',
            field=models.ImageField(upload_to=product.models.upload_to2),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to=product.models.upload_to),
        ),
    ]
