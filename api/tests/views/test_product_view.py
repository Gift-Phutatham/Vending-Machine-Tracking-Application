import secrets
from typing import Any

from django.test import TestCase
from rest_framework import status

from api.models.product import Product
from api.tests.utils import get_values, save_product


class TestProductView(TestCase):
    """Test product view."""

    path: str = "/product/"
    content_type: str = "application/json"

    def test_create_product_should_pass(self) -> None:
        """Test create product with valid request."""
        new_product: dict[str, Any] = {
            "name": secrets.token_hex(16),
            "cost": "{:.2f}".format(secrets.randbelow(1000)),
        }
        response: Any = self.client.post(self.path, data=new_product, content_type=self.content_type)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], new_product["name"])
        self.assertEqual(response.data["cost"], new_product["cost"])

    def test_create_product_should_fail_when_name_is_null(self) -> None:
        """Test create product with invalid request where name is null."""
        new_product: dict[str, Any] = {"cost": "{:.2f}".format(secrets.randbelow(1000))}
        response: Any = self.client.post(self.path, data=new_product, content_type=self.content_type)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_product_should_fail_when_name_is_duplicate(self) -> None:
        """Test create product with invalid request where name already existed."""
        saved_product: Product = save_product()
        new_product: dict[str, Any] = {
            "name": saved_product.name,
            "cost": "{:.2f}".format(secrets.randbelow(1000)),
        }
        response: Any = self.client.post(self.path, data=new_product, content_type=self.content_type)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_product_should_fail_when_cost_is_null(self) -> None:
        """Test create product with invalid request where cost is null."""
        new_product: dict[str, Any] = {"name": secrets.token_hex(16)}
        response: Any = self.client.post(self.path, data=new_product, content_type=self.content_type)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_product_should_pass(self) -> None:
        """Test list product with valid request."""
        saved_product: Product = save_product()
        response: Any = self.client.get(self.path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(saved_product.name, get_values(response, "name"))
        self.assertIn(saved_product.cost, get_values(response, "cost"))

    def test_retrieve_product_should_pass(self) -> None:
        """Test retrieve product with valid request."""
        saved_product: Product = save_product()
        response: Any = self.client.get(f"{self.path}{saved_product.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], saved_product.name)
        self.assertEqual(response.data["cost"], saved_product.cost)

    def test_retrieve_product_should_fail_when_id_is_not_found(self) -> None:
        """Test retrieve product with invalid request where product id does not exist."""
        response: Any = self.client.get(f"{self.path}99999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_product_should_pass(self) -> None:
        """Test update product with valid request."""
        saved_product: Product = save_product()
        new_product: dict[str, Any] = {
            "name": secrets.token_hex(16),
            "cost": "{:.2f}".format(secrets.randbelow(1000)),
        }
        response: Any = self.client.put(
            f"{self.path}{saved_product.id}/",
            data=new_product,
            content_type=self.content_type,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], new_product["name"])
        self.assertEqual(response.data["cost"], new_product["cost"])

    def test_update_product_should_fail_when_id_is_not_found(self) -> None:
        """Test update product with invalid request where product id does not exist."""
        new_product: dict[str, Any] = {
            "name": secrets.token_hex(16),
            "cost": "{:.2f}".format(secrets.randbelow(1000)),
        }
        response: Any = self.client.put(f"{self.path}99999/", data=new_product, content_type=self.content_type)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_product_should_pass(self) -> None:
        """Test delete product with valid request."""
        saved_product: Product = save_product()
        response: Any = self.client.delete(f"{self.path}{saved_product.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_product_should_fail_when_id_is_not_found(self) -> None:
        """Test delete product with invalid request where product id does not exist."""
        response: Any = self.client.delete(f"{self.path}99999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
