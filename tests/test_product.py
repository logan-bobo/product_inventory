import pytest

from product_inventory.product import Product


@pytest.fixture
def product():
    test_product = Product(
        product_id=1,
        name="test_product",
        price=1.00,
        quantity=100
    )

    return test_product


class TestProductCreation:
    def test_product_can_be_instantiated(self):
        product = Product(
            product_id=1,
            name="test_product",
            price=1.00,
            quantity=100
        )
        assert isinstance(product, Product)

    def test_product_can_be_instantiated_without_quantity(self):
        product = Product(
            product_id=1,
            name="test_product",
            price=1.00,
        )
        assert 0 == product.quantity


class TestProductId:
    def test_product_id_property_is_int(self, product):
        assert isinstance(product.product_id, int)

    def test_product_id_getter(self, product):
        assert 1 == product.product_id

    def test_product_id_setter_with_correct_int(self, product):
        product.product_id = 2
        assert 2 == product.product_id

    def test_product_id_setter_exception_with_str(self, product):
        with pytest.raises(ValueError):
            product.product_id = '1'

    def test_product_id_setter_exception_with_id_larger_than_9999(self, product):
        with pytest.raises(ValueError):
            product.product_id = 10000


class TestProductName:
    def test_name_property_is_str(self, product):
        assert isinstance(product.name, str)

    def test_name_property_getter(self, product):
        assert "test_product" == product.name

    def test_name_setter_with_correct_str(self, product):
        product.name = "new_test_product"
        assert "new_test_product" == product.name

    def test_name_setter_exception_with_int(self, product):
        with pytest.raises(ValueError):
            product.name = 12

    def test_name_setter_exception_with_20_char_string(self, product):
        with pytest.raises(ValueError):
            product.name = "test-test-test-test-test-test"


class TestProductPrice:
    def test_price_property_is_float(self, product):
        assert isinstance(product.price, float)

    def test_price_property_getter(self, product):
        assert 1.00 == product.price

    def test_price_setter_with_correct_float(self, product):
        product.price = 1.20
        assert 1.20 == product.price

    def test_price_setter_exception_with_str(self, product):
        with pytest.raises(ValueError):
            product.price = "1.20"

    def test_price_setter_exception_with_incorrect_price(self, product):
        with pytest.raises(ValueError):
            product.price = 123.213


class TestProductQuantity:
    def test_quantity_property_is_int(self, product):
        assert isinstance(product.quantity, int)

    def test_quantity_property_getter(self, product):
        assert 100 == product.quantity

    def test_quantity_setter_with_correct_int(self, product):
        product.quantity = 120
        assert 120 == product.quantity

    def test_quantity_setter_exception_with_str(self, product):
        with pytest.raises(ValueError):
            product.quantity = "120"

    def test_quantity_setter_exception_with_over_1000_products(self, product):
        with pytest.raises(ValueError):
            product.quantity = 1200
