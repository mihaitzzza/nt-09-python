# Generated by Django 4.0.4 on 2022-05-23 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_hdd_type_alter_product_memory_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=8, null=True),
        ),
    ]
