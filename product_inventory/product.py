class Product:
    """
    Class to represent a product and its quantity held
    """

    def __init__(self, product_id: int, name: str, price: float, quantity: int = 0):
        self._product_id: int = product_id
        self._name: str = name
        self._price: float = price
        self._quantity: int = quantity

    @property
    def product_id(self) -> int:
        return self._product_id

    @product_id.setter
    def product_id(self, new_id):
        # TODO: Move all logic where type() != type -> isinstance()
        if type(new_id) != int:
            raise ValueError("New product id must be an int")
        if len(str(new_id)) > 4:
            raise ValueError("Products can not have an ID longer than 4")
        self._product_id = new_id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name):
        if type(new_name) != str:
            raise ValueError("New name must be a str")
        if len(new_name) > 20:
            raise ValueError("Products can not have a name larger than 20 characters")
        self._name = new_name

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, new_price):
        if type(new_price) != float:
            raise ValueError("New price must be a float")
        list_price = str(new_price).split('.')
        if len(list_price[1]) > 2:
            raise ValueError("Products must be in the correct currency format 00.00")
        self._price = new_price

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, new_quantity: int):
        if type(new_quantity) != int:
            raise ValueError("New quantity must be an int")
        if new_quantity > 1000:
            raise ValueError("We can not store more that 1000 of each product")
        self._quantity = new_quantity
