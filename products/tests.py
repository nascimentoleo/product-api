from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.test import Client
from django.test import TestCase
from rest_framework.test import APIClient

from .models import Product, Category


class ProductUnitTestCase(TestCase):
    
    def setUp(self):
        pass
        
    def test_product_can_not_save_without_category(self):
        product = Product(name="Candy", size=1, price=2.5)
        self.assertRaises(IntegrityError, product.save)


class CategoryUnitTestCase(TestCase):
    def setUp(self):
        self.httpClient = Client()
    
    def test_category_can_not_save_without_name(self):
        category = Category(name=None)
        self.assertRaises(IntegrityError, category.save)


class ProductIntegrationTestCase(TestCase):
    
    def setUp(self):
        self.httpClient = APIClient()
        self.__fake_data()
        self.httpClient.credentials(HTTP_AUTHORIZATION='Bearer ' + self.__get_access_token())
        
    def __fake_data(self):
        self.category = Category(name="Eletronics")
        self.category.save()
        self.product = Product(name="Phone", size=1, price=2.5, category=self.category)
        self.product.save()
        
    def __get_access_token(self):
        User.objects.create_user(username='testuser', password='test123')
        response = self.client.post('/api/token/', {'username': 'testuser', 'password': 'test123'})
        return response.data["access"]

    def test_endpoint_products_must_retrieve_all_products(self):
        response = self.httpClient.get('/products/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)
        
    def test_endpoint_products_must_create_product(self):
        response = self.httpClient.post(
            '/products/', {"name": "Notebook", "size": 15, "price": 3700.90, "category_id": self.category.id})

        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(response.data["id"])
        
    def test_endpoint_products_must_retrieve_product_by_id(self):
        response = self.httpClient.get('/products/{}/'.format(self.product.id))

        self.assertEqual(response.status_code, 200)
        self.assertEquals(response.data["id"], self.product.id)
        
    def test_endpoint_products_must_delete_product_by_id(self):
        response = self.httpClient.delete('/products/{}/'.format(self.product.id))
        self.assertEqual(response.status_code, 204)
        
        response = self.httpClient.get('/products/{}/'.format(self.product.id))
        self.assertEquals(response.status_code, 404)


class CategoryIntegrationTestCase(TestCase):
    
    def setUp(self):
        self.httpClient = APIClient()
        self.__fake_data()
        self.httpClient.credentials(HTTP_AUTHORIZATION='Bearer ' + self.__get_access_token())
    
    def __fake_data(self):
        self.category = Category(name="Eletronics")
        self.category.save()
        
    def __get_access_token(self):
        User.objects.create_user(username='testuser', password='test123')
        response = self.client.post('/api/token/', {'username': 'testuser', 'password': 'test123'})
        return response.data["access"]
    
    def test_endpoint_categories_must_retrieve_all_categories(self):
        response = self.httpClient.get('/categories/')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)
    
    def test_endpoint_categories_must_create_categorie(self):
        response = self.httpClient.post(
            '/categories/', {"name": "Food"})
        
        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(response.data["id"])
    
    def test_endpoint_categories_must_retrieve_category_by_id(self):
        response = self.httpClient.get('/categories/{}/'.format(self.category.id))
        
        self.assertEqual(response.status_code, 200)
        self.assertEquals(response.data["id"], self.category.id)
    
    def test_endpoint_categories_must_delete_category_by_id(self):
        response = self.httpClient.delete('/categories/{}/'.format(self.category.id))
        self.assertEqual(response.status_code, 204)
        
        response = self.httpClient.get('/categories/{}/'.format(self.category.id))
        self.assertEquals(response.status_code, 404)
