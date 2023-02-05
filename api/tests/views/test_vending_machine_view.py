import secrets
from typing import Any

from django.test import TestCase
from rest_framework import status

from api.models.vending_machine import VendingMachine
from api.tests.utils import get_values, save_vending_machine


class TestVendingMachineView(TestCase):
    """Test vending machine view."""

    path: str = "/vending-machine/"

    def test_create_vending_machine_should_pass(self) -> None:
        """Test create vending machine with valid request."""
        new_vending_machine: dict[str, Any] = {
            "name": secrets.token_hex(16),
            "location": secrets.token_hex(16),
            "is_active": True,
        }
        response: Any = self.client.post(self.path, data=new_vending_machine, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], new_vending_machine["name"])
        self.assertEqual(response.data["location"], new_vending_machine["location"])
        self.assertEqual(response.data["is_active"], new_vending_machine["is_active"])

    def test_create_vending_machine_should_fail_when_name_is_null(self) -> None:
        """Test create vending machine with invalid request where name is null."""
        new_vending_machine: dict[str, Any] = {"location": secrets.token_hex(16)}
        response: Any = self.client.post(self.path, data=new_vending_machine, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_vending_machine_should_fail_when_name_is_duplicate(self) -> None:
        """Test create vending machine with invalid request where name already existed."""
        saved_vending_machine: VendingMachine = save_vending_machine()
        new_vending_machine: dict[str, Any] = {
            "name": saved_vending_machine.name,
            "location": secrets.token_hex(16),
            "is_active": True,
        }
        response: Any = self.client.post(self.path, data=new_vending_machine, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_vending_machine_should_fail_when_location_is_null(self) -> None:
        """Test create vending machine with invalid request where location is null."""
        new_vending_machine: dict[str, Any] = {"name": secrets.token_hex(16)}
        response: Any = self.client.post(self.path, data=new_vending_machine, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_vending_machine_should_fail_when_is_active_is_invalid(self) -> None:
        """Test create vending machine with invalid request where is_active is not a boolean."""
        new_vending_machine: dict[str, Any] = {
            "name": secrets.token_hex(16),
            "location": secrets.token_hex(16),
            "is_active": "x",
        }
        response: Any = self.client.post(self.path, data=new_vending_machine, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_vending_machine_should_pass(self) -> None:
        """Test list vending machine with valid request."""
        saved_vending_machine: VendingMachine = save_vending_machine()
        response: Any = self.client.get(self.path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(saved_vending_machine.name, get_values(response, "name"))
        self.assertIn(saved_vending_machine.location, get_values(response, "location"))
        self.assertIn(saved_vending_machine.is_active, get_values(response, "is_active"))

    def test_retrieve_vending_machine_should_pass(self) -> None:
        """Test retrieve vending machine with valid request."""
        saved_vending_machine: VendingMachine = save_vending_machine()
        response: Any = self.client.get(f"{self.path}{saved_vending_machine.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], saved_vending_machine.name)
        self.assertEqual(response.data["location"], saved_vending_machine.location)
        self.assertEqual(response.data["is_active"], saved_vending_machine.is_active)

    def test_retrieve_vending_machine_should_fail_when_id_is_not_found(self) -> None:
        """Test retrieve vending machine with invalid request where vending machine id does not exist."""
        response: Any = self.client.get(f"{self.path}99999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_vending_machine_should_pass(self) -> None:
        """Test update vending machine with valid request."""
        saved_vending_machine: VendingMachine = save_vending_machine()
        new_vending_machine: dict[str, Any] = {
            "name": secrets.token_hex(16),
            "location": secrets.token_hex(16),
            "is_active": False,
        }
        response: Any = self.client.put(
            f"{self.path}{saved_vending_machine.id}/",
            data=new_vending_machine,
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], new_vending_machine["name"])
        self.assertEqual(response.data["location"], new_vending_machine["location"])
        self.assertEqual(response.data["is_active"], new_vending_machine["is_active"])

    def test_update_vending_machine_should_fail_when_id_is_not_found(self) -> None:
        """Test update vending machine with invalid request where vending machine id does not exist."""
        new_vending_machine: dict[str, Any] = {
            "name": secrets.token_hex(16),
            "location": secrets.token_hex(16),
            "is_active": True,
        }
        response: Any = self.client.put(f"{self.path}99999/", data=new_vending_machine, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_vending_machine_should_pass(self) -> None:
        """Test delete vending machine with valid request."""
        saved_vending_machine: VendingMachine = save_vending_machine()
        response: Any = self.client.delete(f"{self.path}{saved_vending_machine.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_vending_machine_should_fail_when_id_is_not_found(self) -> None:
        """Test delete vending machine with invalid request where vending machine id does not exist."""
        response: Any = self.client.delete(f"{self.path}99999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
