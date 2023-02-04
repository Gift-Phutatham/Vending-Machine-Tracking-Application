import secrets

from django.test import TestCase
from rest_framework import status

from api.models.product import Product
from api.models.stock import Stock
from api.models.vending_machine import VendingMachine


def save_vending_machine():
    vending_machine = VendingMachine(
        id=1,
        name=secrets.token_hex(16),
        location=secrets.token_hex(16),
        is_active=True
    )
    vending_machine.save()
    return vending_machine


def save_product():
    product = Product(
        id=1,
        name=secrets.token_hex(16),
        cost='{:.2f}'.format(secrets.randbelow(1000))
    )
    product.save()
    return product


def save_stock():
    vending_machine = save_vending_machine()
    product = save_product()
    stock = Stock(
        id=1,
        vending_machine=vending_machine,
        product=product,
        quantity=secrets.randbelow(100)
    )
    stock.save()
    return stock


class TestStockViewSet(TestCase):
    path = '/stock/'

    def test_create_stock_should_pass(self):
        saved_vending_machine = save_vending_machine()
        saved_product = save_product()
        new_stock = {
            'vending_machine': saved_vending_machine.id,
            'product': saved_product.id,
            'quantity': secrets.randbelow(100)
        }
        response = self.client.post(self.path, data=new_stock, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['vending_machine'], new_stock['vending_machine'])
        self.assertEqual(response.data['product'], new_stock['product'])
        self.assertEqual(response.data['quantity'], new_stock['quantity'])

    def test_create_stock_should_fail_when_vending_machine_is_null(self):
        saved_product = save_product()
        new_stock = {
            'product': saved_product.id,
            'quantity': secrets.randbelow(100)
        }
        response = self.client.post(self.path, data=new_stock, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_stock_should_fail_when_vending_machine_is_not_found(self):
        saved_product = save_product()
        new_stock = {
            'vending_machine': 1,
            'product': saved_product.id,
            'quantity': secrets.randbelow(100)
        }
        response = self.client.post(self.path, data=new_stock, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_stock_should_fail_when_product_is_null(self):
        saved_vending_machine = save_vending_machine()
        new_stock = {
            'vending_machine': saved_vending_machine.id,
            'quantity': secrets.randbelow(100)
        }
        response = self.client.post(self.path, data=new_stock, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_stock_should_fail_when_product_is_not_found(self):
        saved_vending_machine = save_vending_machine()
        new_stock = {
            'vending_machine': saved_vending_machine.id,
            'product': 1,
            'quantity': secrets.randbelow(100)
        }
        response = self.client.post(self.path, data=new_stock, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_stock_should_fail_when_quantity_is_null(self):
        saved_vending_machine = save_vending_machine()
        saved_product = save_product()
        new_stock = {
            'vending_machine': saved_vending_machine.id,
            'product': saved_product.id
        }
        response = self.client.post(self.path, data=new_stock, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_stock_should_fail_when_quantity_is_invalid(self):
        saved_vending_machine = save_vending_machine()
        saved_product = save_product()
        new_stock = {
            'vending_machine': saved_vending_machine.id,
            'product': saved_product.id,
            'quantity': 'x'
        }
        response = self.client.post(self.path, data=new_stock, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_stock_should_pass(self):
        saved_stock = save_stock()
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['vending_machine'], saved_stock.vending_machine.id)
        self.assertEqual(response.data[0]['product'], saved_stock.product.id)
        self.assertEqual(response.data[0]['quantity'], saved_stock.quantity)

    def test_view_stock_should_pass(self):
        saved_stock = save_stock()
        response = self.client.get(f'{self.path}{saved_stock.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['vending_machine'], saved_stock.vending_machine.id)
        self.assertEqual(response.data['product'], saved_stock.product.id)
        self.assertEqual(response.data['quantity'], saved_stock.quantity)

    def test_view_stock_should_fail_when_id_is_not_found(self):
        response = self.client.get(f'{self.path}1/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_stock_should_pass(self):
        saved_stock = save_stock()
        new_stock = {
            'vending_machine': saved_stock.vending_machine.id,
            'product': saved_stock.product.id,
            'quantity': secrets.randbelow(100)
        }
        response = self.client.put(
            f'{self.path}{saved_stock.id}/',
            data=new_stock,
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['vending_machine'], new_stock['vending_machine'])
        self.assertEqual(response.data['product'], new_stock['product'])
        self.assertEqual(response.data['quantity'], new_stock['quantity'])

    def test_update_stock_should_fail_when_id_is_not_found(self):
        saved_vending_machine = save_vending_machine()
        saved_product = save_product()
        new_stock = {
            'vending_machine': saved_vending_machine.id,
            'product': saved_product.id,
            'quantity': secrets.randbelow(100)
        }
        response = self.client.put(f'{self.path}1/', data=new_stock, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_stock_should_pass(self):
        saved_stock = save_stock()
        response = self.client.delete(f'{self.path}{saved_stock.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_stock_should_fail_when_id_is_not_found(self):
        response = self.client.delete(f'{self.path}1/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
