import secrets
from typing import Any

from django.test import TestCase
from rest_framework import status

from api.models.product import Product
from api.models.stock import Stock
from api.models.vending_machine import VendingMachine
from api.tests.utils import get_values, save_product, save_stock, save_vending_machine


class TestStockView(TestCase):
    """Test stock view."""

    path: str = "/stock/"

    def test_create_stock_should_pass(self) -> None:
        """Test create stock with valid request."""
        saved_vending_machine: VendingMachine = save_vending_machine()
        saved_product: Product = save_product()
        new_stock: dict[str, Any] = {
            "vending_machine": saved_vending_machine.id,
            "product": saved_product.id,
            "quantity": secrets.randbelow(100),
        }
        response: Any = self.client.post(self.path, data=new_stock, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["vending_machine"], new_stock["vending_machine"])
        self.assertEqual(response.data["product"], new_stock["product"])
        self.assertEqual(response.data["quantity"], new_stock["quantity"])

    def test_create_stock_should_fail_when_vending_machine_is_null(self) -> None:
        """Test create stock with invalid request where vending machine is null."""
        saved_product: Product = save_product()
        new_stock: dict[str, Any] = {
            "product": saved_product.id,
            "quantity": secrets.randbelow(100),
        }
        response: Any = self.client.post(self.path, data=new_stock, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_stock_should_fail_when_vending_machine_id_is_not_found(
        self,
    ) -> None:
        """Test create stock with invalid request where vending machine id does not exist."""
        saved_product: Product = save_product()
        new_stock: dict[str, Any] = {
            "vending_machine": 99999,
            "product": saved_product.id,
            "quantity": secrets.randbelow(100),
        }
        response: Any = self.client.post(self.path, data=new_stock, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_stock_should_fail_when_product_is_null(self) -> None:
        """Test create stock with invalid request where product is null."""
        saved_vending_machine: VendingMachine = save_vending_machine()
        new_stock: dict[str, Any] = {
            "vending_machine": saved_vending_machine.id,
            "quantity": secrets.randbelow(100),
        }
        response: Any = self.client.post(self.path, data=new_stock, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_stock_should_fail_when_product_id_is_not_found(self) -> None:
        """Test create stock with invalid request where product id does not exist."""
        saved_vending_machine: VendingMachine = save_vending_machine()
        new_stock: dict[str, Any] = {
            "vending_machine": saved_vending_machine.id,
            "product": 99999,
            "quantity": secrets.randbelow(100),
        }
        response: Any = self.client.post(self.path, data=new_stock, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_stock_should_fail_when_quantity_is_null(self) -> None:
        """Test create stock with invalid request where quantity is null."""
        saved_vending_machine: VendingMachine = save_vending_machine()
        saved_product: Product = save_product()
        new_stock: dict[str, Any] = {
            "vending_machine": saved_vending_machine.id,
            "product": saved_product.id,
        }
        response: Any = self.client.post(self.path, data=new_stock, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_stock_should_fail_when_quantity_is_invalid(self) -> None:
        """Test create stock with invalid request where quantity is not a number."""
        saved_vending_machine: VendingMachine = save_vending_machine()
        saved_product: Product = save_product()
        new_stock: dict[str, Any] = {
            "vending_machine": saved_vending_machine.id,
            "product": saved_product.id,
            "quantity": "x",
        }
        response: Any = self.client.post(self.path, data=new_stock, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_stock_should_pass(self) -> None:
        """Test list stock with valid request."""
        saved_stock: Stock = save_stock()
        response: Any = self.client.get(self.path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(saved_stock.vending_machine.id, get_values(response, "vending_machine"))
        self.assertIn(saved_stock.product.id, get_values(response, "product"))
        self.assertIn(saved_stock.quantity, get_values(response, "quantity"))

    def test_retrieve_stock_should_pass(self) -> None:
        """Test retrieve stock with valid request."""
        saved_stock: Stock = save_stock()
        response: Any = self.client.get(f"{self.path}{saved_stock.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["vending_machine"], saved_stock.vending_machine.id)
        self.assertEqual(response.data["product"], saved_stock.product.id)
        self.assertEqual(response.data["quantity"], saved_stock.quantity)

    def test_retrieve_stock_should_fail_when_id_is_not_found(self) -> None:
        """Test retrieve stock with invalid request where stock id does not exist."""
        response: Any = self.client.get(f"{self.path}99999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_stock_should_pass(self) -> None:
        """Test update stock with valid request."""
        saved_stock: Stock = save_stock()
        new_stock: dict[str, Any] = {
            "vending_machine": saved_stock.vending_machine.id,
            "product": saved_stock.product.id,
            "quantity": secrets.randbelow(100),
        }
        response: Any = self.client.put(
            f"{self.path}{saved_stock.id}/",
            data=new_stock,
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["vending_machine"], new_stock["vending_machine"])
        self.assertEqual(response.data["product"], new_stock["product"])
        self.assertEqual(response.data["quantity"], new_stock["quantity"])

    def test_update_stock_should_fail_when_id_is_not_found(self) -> None:
        """Test update stock with invalid request where stock id does not exist."""
        saved_vending_machine: VendingMachine = save_vending_machine()
        saved_product: Product = save_product()
        new_stock: dict[str, Any] = {
            "vending_machine": saved_vending_machine.id,
            "product": saved_product.id,
            "quantity": secrets.randbelow(100),
        }
        response: Any = self.client.put(f"{self.path}99999/", data=new_stock, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_stock_should_pass(self) -> None:
        """Test delete stock with valid request."""
        saved_stock: Stock = save_stock()
        response: Any = self.client.delete(f"{self.path}{saved_stock.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_stock_should_fail_when_id_is_not_found(self) -> None:
        """Test delete stock with invalid request where stock id does not exist."""
        response: Any = self.client.delete(f"{self.path}99999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
