from django.test import Client
from django.test import TestCase
from django.db.utils import IntegrityError
from .models import Product, Category


class ProductUnitTestCase(TestCase):
    def setUp(self):
        pass
        
    def test_product_can_not_save_without_category(self):
        product = Product(name="Candy", size=1, price=2.5)
        self.assertRaises(IntegrityError, product.save)


# class ProductIntegrationTestCase(TestCase):
#     def setUp(self):
#         self.httpClient = Client()
#
#     def test_endpoint_products_must_retrieve_all_products(self):
#         category = Category(name="Eletronics")
#         category.save()
#         product = Product(name="Phone", size=1, price=2.5, category=category)
#         product.save()
#
#         response = self.client.get('/products/')
#
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(len(response), 1)


class CategoryUnitTestCase(TestCase):
    def setUp(self):
        self.httpClient = Client()
    
    def test_category_can_not_save_without_name(self):
        category = Category(name=None)
        self.assertRaises(IntegrityError, category.save)

