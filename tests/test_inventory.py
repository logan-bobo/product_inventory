import pytest

from product_inventory.inventory import Inventory
from .fixtures import (
    product,
    empty_inventory,
    single_item_inventory
)


class TestInventoryCreation:
    def test_inventory_can_be_instantiated(self):
        inventory = Inventory(
            name="test"
        )
        assert isinstance(inventory, Inventory)

    def test_inventory_can_be_instantiated_and_have_no_products(self):
        inventory = Inventory(
            name="test"
        )
        assert inventory.products == []


class TestInventoryName:
    def test_inventory_name_getter(self, empty_inventory):
        assert "test_inventory" == empty_inventory.name

    def test_inventory_name_setter(self, empty_inventory):
        empty_inventory.name = "test"
        assert "test" == empty_inventory.name

    def test_inventory_name_set_fails_with_int(self, empty_inventory):
        with pytest.raises(ValueError):
            empty_inventory.name = 1


class TestInventoryProducts:
    pass


class TestInventoryItems:
    pass


class TestInventorySum:
    pass
