import os
import json
import random
import shutil

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction, IntegrityError
from products.models import Category, Product, Store


class Command(BaseCommand):
    help = 'Import products from web scrapped application.'

    def add_arguments(self, parser):
        parser.add_argument('--import_file', type=str, help='Give the path to JSON file.')
        parser.add_argument('--images_folder', type=str, help='Give the path to images folder.')

    @staticmethod
    def get_price_from_string(value):
        try:
            price_str = value.split(' ')[0]
            return float(price_str.replace('.', '').replace(',', '.')) or 0.00
        except:
            return 0.00

    @staticmethod
    def get_number_from_string(value):
        try:
            return value.split(' ')[0] or None
        except:
            return None

    def handle(self, *args, import_file, images_folder, **options):
        print('Here is my first Django command.')

        if import_file is None:
            raise CommandError('`import_file` parameter is mandatory.')

        if images_folder is None:
            raise CommandError('`images_folder` parameter is mandatory.')

        # Assuming the parameter values are valid continue with the import.

        with open(import_file) as json_file:
            categories_with_products = json.load(json_file)

        shutil.copytree(images_folder, os.path.join(settings.MEDIA_ROOT, 'products'))

        try:
            with transaction.atomic():
                for category_index, category_data in enumerate(categories_with_products):
                    store = Store.objects.get(id=category_index + 1)

                    try:
                        category = Category.objects.get(name=category_data['name'])
                    except Category.DoesNotExist:
                        category = Category(name=category_data['name'])
                        category.save()

                    for product_data in category_data['products']:
                        normal_price = self.get_price_from_string(product_data['price']) or random.choice(range(1200, 9000))
                        specifications = product_data['specifications']

                        try:
                            Product.objects.get(name=product_data['title'])
                        except Product.DoesNotExist:
                            Product.objects.create(
                                store=store,
                                category=category,
                                name=product_data['title'],
                                normal_price=normal_price,
                                price=normal_price,
                                processor_owner=specifications['processor_owner'],
                                cores_number=specifications['cores_number'],
                                processor_technology=(
                                    self.get_number_from_string(
                                        specifications['processor_technology']
                                    ) or random.choice(range(2, 28))
                                ),
                                memory_capacity=(
                                    self.get_number_from_string(
                                        specifications['memory_capacity']
                                    ) or random.choice(range(4, 128))
                                ),
                                memory_type=specifications['memory_type'],
                                hdd_type=specifications['hdd_type'],
                                weight=self.get_number_from_string(specifications['weight']),
                                stock=random.choice(range(0, 2000)),
                                image=f'products/{product_data["id"]}.jpg',
                            )
        except IntegrityError as e:
            raise CommandError(e)
