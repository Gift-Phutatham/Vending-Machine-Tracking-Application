import secrets

from django.test import TestCase
from rest_framework import status

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


class TestVendingMachineViewSet(TestCase):
    path = '/vending-machine/'

    def test_create_vending_machine_should_pass(self):
        new_vending_machine = {
            'name': secrets.token_hex(16),
            'location': secrets.token_hex(16),
            'is_active': True
        }
        response = self.client.post(self.path, data=new_vending_machine, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], new_vending_machine['name'])
        self.assertEqual(response.data['location'], new_vending_machine['location'])
        self.assertEqual(response.data['is_active'], new_vending_machine['is_active'])

    def test_create_vending_machine_should_fail_when_name_is_null(self):
        new_vending_machine = {
            'location': secrets.token_hex(16)
        }
        response = self.client.post(self.path, data=new_vending_machine, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_vending_machine_should_fail_when_name_is_duplicate(self):
        saved_vending_machine = save_vending_machine()
        new_vending_machine = {
            'name': saved_vending_machine.name,
            'location': secrets.token_hex(16),
            'is_active': True
        }
        response = self.client.post(self.path, data=new_vending_machine, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_vending_machine_should_fail_when_location_is_null(self):
        new_vending_machine = {
            'name': secrets.token_hex(16)
        }
        response = self.client.post(self.path, data=new_vending_machine, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_vending_machine_should_fail_when_is_active_is_invalid(self):
        new_vending_machine = {
            'name': secrets.token_hex(16),
            'location': secrets.token_hex(16),
            'is_active': 'x'
        }
        response = self.client.post(self.path, data=new_vending_machine, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_vending_machine_should_pass(self):
        saved_vending_machine = save_vending_machine()
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], saved_vending_machine.name)
        self.assertEqual(response.data[0]['location'], saved_vending_machine.location)
        self.assertEqual(response.data[0]['is_active'], saved_vending_machine.is_active)

    def test_view_vending_machine_should_pass(self):
        saved_vending_machine = save_vending_machine()
        response = self.client.get(f'{self.path}{saved_vending_machine.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], saved_vending_machine.name)
        self.assertEqual(response.data['location'], saved_vending_machine.location)
        self.assertEqual(response.data['is_active'], saved_vending_machine.is_active)

    def test_view_vending_machine_should_fail_when_id_is_not_found(self):
        response = self.client.get(f'{self.path}1/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_vending_machine_should_pass(self):
        saved_vending_machine = save_vending_machine()
        new_vending_machine = {
            'name': secrets.token_hex(16),
            'location': secrets.token_hex(16),
            'is_active': False
        }
        response = self.client.put(
            f'{self.path}{saved_vending_machine.id}/',
            data=new_vending_machine,
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], new_vending_machine['name'])
        self.assertEqual(response.data['location'], new_vending_machine['location'])
        self.assertEqual(response.data['is_active'], new_vending_machine['is_active'])

    def test_update_vending_machine_should_fail_when_id_is_not_found(self):
        new_vending_machine = {
            'name': secrets.token_hex(16),
            'location': secrets.token_hex(16),
            'is_active': True
        }
        response = self.client.put(f'{self.path}1/', data=new_vending_machine, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_vending_machine_should_pass(self):
        saved_vending_machine = save_vending_machine()
        response = self.client.delete(f'{self.path}{saved_vending_machine.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_vending_machine_should_fail_when_id_is_not_found(self):
        response = self.client.delete(f'{self.path}1/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
