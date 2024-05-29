# Generated by Django 5.0.3 on 2024-05-26 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_category_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='product',
            name='stock_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='ProductDetail',
        ),
    ]
