import secrets

from django.test import TestCase
from rest_framework import status

from api.models.product import Product


def save_product():
    product = Product(
        id=1,
        name=secrets.token_hex(16),
        cost='{:.2f}'.format(secrets.randbelow(1000))
    )
    product.save()
    return product


class TestProductViewSet(TestCase):
    path = '/product/'

    def test_create_product_should_pass(self):
        new_product = {
            'name': secrets.token_hex(16),
            'cost': '{:.2f}'.format(secrets.randbelow(1000))
        }
        response = self.client.post(self.path, data=new_product, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], new_product['name'])
        self.assertEqual(response.data['cost'], new_product['cost'])

    def test_create_product_should_fail_when_name_is_null(self):
        new_product = {
            'cost': '{:.2f}'.format(secrets.randbelow(1000))
        }
        response = self.client.post(self.path, data=new_product, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_product_should_fail_when_name_is_duplicate(self):
        saved_product = save_product()
        new_product = {
            'name': saved_product.name,
            'cost': '{:.2f}'.format(secrets.randbelow(1000))
        }
        response = self.client.post(self.path, data=new_product, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_product_should_fail_when_cost_is_null(self):
        new_product = {
            'name': secrets.token_hex(16)
        }
        response = self.client.post(self.path, data=new_product, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_product_should_pass(self):
        saved_product = save_product()
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], saved_product.name)
        self.assertEqual(response.data[0]['cost'], saved_product.cost)

    def test_view_product_should_pass(self):
        saved_product = save_product()
        response = self.client.get(f'{self.path}{saved_product.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], saved_product.name)
        self.assertEqual(response.data['cost'], saved_product.cost)

    def test_view_product_should_fail_when_id_is_not_found(self):
        response = self.client.get(f'{self.path}1/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_product_should_pass(self):
        saved_product = save_product()
        new_product = {
            'name': secrets.token_hex(16),
            'cost': '{:.2f}'.format(secrets.randbelow(1000))
        }
        response = self.client.put(f'{self.path}{saved_product.id}/', data=new_product, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], new_product['name'])
        self.assertEqual(response.data['cost'], new_product['cost'])

    def test_update_product_should_fail_when_id_is_not_found(self):
        new_product = {
            'name': secrets.token_hex(16),
            'cost': '{:.2f}'.format(secrets.randbelow(1000))
        }
        response = self.client.put(f'{self.path}1/', data=new_product, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_product_should_pass(self):
        saved_product = save_product()
        response = self.client.delete(f'{self.path}{saved_product.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_product_should_fail_when_id_is_not_found(self):
        response = self.client.delete(f'{self.path}1/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)