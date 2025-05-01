import csv
from django.core.management.base import BaseCommand
from .models import Phone
from django.utils.text import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        file_path = options['file']

        try:
            with open(file_path, 'r', encoding='utf-8') as csvfile:
                phone_reader = csv.reader(csvfile, delimiter=';')
                next(phone_reader)

                for row in phone_reader:
                    name = row[0]
                    price = row[1]
                    image = row[2]
                    release_date = row[3]
                    lte_exists = row[4].lower() == 'true'
                    slug = slugify(name)

                    phone, created = Phone.objects.get_or_create(
                        name=name,
                        price=price,
                        image=image,
                        release_date=release_date,
                        lte_exists=lte_exists,
                        slug=slug
                    )
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"File {file_path} not found."))
            pass
