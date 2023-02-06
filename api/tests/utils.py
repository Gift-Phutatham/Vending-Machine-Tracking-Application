import secrets
from typing import Any

from api.models.product import Product
from api.models.stock import Stock
from api.models.vending_machine import VendingMachine


def save_vending_machine() -> VendingMachine:
    """
    Save vending machine.

    Returns:
        VendingMachine: Saved vending machine.
    """
    vending_machine: VendingMachine = VendingMachine(
        id=1, name=secrets.token_hex(16), location=secrets.token_hex(16), is_active=True
    )
    vending_machine.save()
    return vending_machine


def save_product() -> Product:
    """
    Save product.

    Returns:
        Product: Saved product.
    """
    product: Product = Product(id=1, name=secrets.token_hex(16), cost="{:.2f}".format(secrets.randbelow(1000)))
    product.save()
    return product


def save_stock() -> Stock:
    """
    Save stock.

    Returns:
        Stock: Saved stock.
    """
    vending_machine: VendingMachine = save_vending_machine()
    product: Product = save_product()
    stock: Stock = Stock(
        id=1,
        vending_machine=vending_machine,
        product=product,
        quantity=secrets.randbelow(100),
    )
    stock.save()
    return stock


def get_values(response: Any, key: str) -> list[str]:
    """
    Get values from the given response and key.

    Params:
        response (Any): Response to be retrieved the value from
        key (str): Key of the response body
    Returns:
        list[str]: List of the values.
    """
    return list(map(lambda data: data[key], response.data))
