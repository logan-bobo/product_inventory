from .product import Product


class Inventory:
    """
    A class to represent our inventory for a store
    """
    def __init__(self, name: str, products=None):
        if products is None:
            products = []
        self._name: str = name
        self._products: list[Product] = products
        self._total_items: int = len(self._products)
        self._inventory_sum: float = sum([(p.price * p.quantity) for p in self._products])

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str):
        self._name = new_name

    @property
    def products(self) -> list[Product]:
        return self._products

    @products.setter
    def products(self, new_products: list[Product]):
        self._products = new_products

    def add_product(self, new_product: Product) -> None:
        self._products.append(new_product)
        return None

    def add_products(self, new_products: list[Product]) -> None:
        for new_product in new_products:
            self._products.append(new_product)
        return None

    def remove_product(self, product_to_remove: Product) -> None:
        try:
            self._products.remove(product_to_remove)
        except ValueError as error:
            raise f"Product {product_to_remove.name} not in inventory {error}"
        return None

    def remove_products(self, products_to_remove: list[Product]) -> None:
        for product_to_remove in products_to_remove:
            try:
                self._products.remove(product_to_remove)
            except ValueError as error:
                raise f"Product {product_to_remove.name} not in inventory {error}"
        return None
