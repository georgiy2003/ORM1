
from django.test import TestCase
from django.urls import reverse
from phones.models import Phone
from django.utils.text import slugify


class PhoneModelTest(TestCase):
    def setUp(self):
        self.phone = Phone.objects.create(
            name='Test Phone',
            price=499.99,
            image='https://example.com/test.jpg',
            release_date='2023-01-01',
            lte_exists=True
        )

    def test_slug_is_generated(self):
        self.assertEqual(self.phone.slug, slugify(self.phone.name))


class CatalogViewTest(TestCase):
    def setUp(self):
        Phone.objects.create(
            name='Phone A', price=100, image='a.jpg', release_date='2022-01-01', lte_exists=True
        )
        Phone.objects.create(
            name='Phone B', price=200, image='b.jpg', release_date='2022-01-01', lte_exists=False
        )

    def test_catalog_page_status_code(self):
        response = self.client.get(reverse('catalog'))
        self.assertEqual(response.status_code, 200)

    def test_catalog_sort_by_name(self):
        response = self.client.get(reverse('catalog') + '?sort=name')
        phones = response.context['phones']
        self.assertEqual(phones[0].name, 'Phone A')

    def test_catalog_sort_by_min_price(self):
        response = self.client.get(reverse('catalog') + '?sort=min_price')
        phones = response.context['phones']
        self.assertEqual(phones[0].price, 100)

    def test_catalog_sort_by_max_price(self):
        response = self.client.get(reverse('catalog') + '?sort=max_price')
        phones = response.context['phones']
        self.assertEqual(phones[0].price, 200)

    def test_phone_detail_view(self):
        phone = Phone.objects.first()
        response = self.client.get(reverse('phone_detail', kwargs={'slug': phone.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, phone.name)