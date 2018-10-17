from flask_testing import TestCase
from app.api.v1.models.products import Product
from app.api.v1.models.sales import Sale
from run import app


class BaseTestCase(TestCase):
    """ Base Tests """

    @classmethod
    def create_app(cls):
        app.config.from_object('instance.config.TestingConfig')
        return app

    def setUp(self):
        self.product = Product()
        self.data = self.product.create_product({"name":"test1", "description":"description1"})
        self.no_name = self.product.create_product({"description": "no name"})
        self.no_description = self.product.create_product({"name": "no description"})

        self.sale = Sale()
        self.data = self.sale.create_sale({"name":"test1", "description":"description1"})
        self.no_title = self.sale.create_sale({"description": "no title"})
        self.no_description = self.sale.create_sale({"name": "no description"})

    def tearDown(self):
        self.product.no_of_products.clear()
        self.product.no_of_products.clear()