from datetime import datetime
from ..utils.dto import SalesDto

api = SalesDto.api

class Sale(object):
    """ CLASS FOR ADDING, EDITING AND DELETING STORE SALES."""

    def __init__(self):
        """constructor method"""

        self.no_of_sales = []

    def create_sale(self, data):
        """Method for creating an sale"""

        data["id"] = int(len(self.no_of_sales) + 1)
        data["creation_date"] = str(datetime.now().strftime('%b-%d-%Y : %H:%M:%S'))
        self.no_of_sales.append(data)
        return data

    def get_one(self, sale_id):
        """Method for fetching one sale by its id"""
        sale = [sale for sale in self.no_of_sales if sale["id"] == sale_id]

        if not sale:
            api.abort(404, "Sale {} does not exist".format(sale_id))
        return sale

    def delete_sale(self, sale_id):
        "Method for deleting an sale"

        sale = self.get_one(sale_id)
        self.no_of_sales.remove(sale[0])

    def update_sale(self, sale_id, data):
        """Method for updating an sale"""

        sale = self.get_one(sale_id)
        data['modified_date'] = str(datetime.now().strftime('%b-%d-%Y : %H:%M:%S'))
        sale[0].update(data)
        return sale

    def get_all(self):
        """Method for returning all sales."""
        sales = [sales for sales in self.no_of_sales]
        if not sales:
            api.abort(404, "No Sales Found.")
        return sales
