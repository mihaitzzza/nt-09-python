# Generated by Django 4.0.4 on 2022-06-06 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_rename_title_product_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('-id',), 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',)},
        ),
    ]
