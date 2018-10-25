from datetime import datetime
from ..utils.dto import ProductsDto

api = ProductsDto.api

class Product(object):
    """ CLASS FOR ADDING, EDITING AND DELETING STORE PRODUCTS."""

    def __init__(self):
        """constructor method"""

        self.no_of_products = []

    def create_product(self, data):
        """Method for creating an product"""

        data["id"] = int(len(self.no_of_products) + 1)
        data["creation_date"] = str(datetime.now().strftime('%b-%d-%Y : %H:%M:%S'))
        self.no_of_products.append(data)
        return data

    def get_one(self, product_id):
        """Method for fetching one product by its id"""
        product = [product for product in self.no_of_products if product["id"] == product_id]

        if not product:
            api.abort(404, "Product {} does not exist".format(product_id))
        return product

    def delete_product(self, product_id):
        "Method for deleting an product"

        product = self.get_one(product_id)
        self.no_of_products.remove(product[0])

    def update_product(self, product_id, data):
        """Method for updating an product"""

        product = self.get_one(product_id)
        data['modified_date'] = str(datetime.now().strftime('%b-%d-%Y : %H:%M:%S'))
        product[0].update(data)
        return product

    def get_all(self):
        """Method for returning all products."""
        products = [products for products in self.no_of_products]
        if not products:
            api.abort(404, "No Products Found.")
        return products
