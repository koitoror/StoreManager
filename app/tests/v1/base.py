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
        self.data = self.product.create_product({"name":"test1", "price":100, "quantity":10})
        self.no_name = self.product.create_product({"price":50, "quantity":100})
        self.no_price = self.product.create_product({"name":"no price", "quantity":30})
        self.no_quantity = self.product.create_product({"name": "no quantity"})


        self.sale = Sale()
        self.data = self.sale.create_sale({"name":"test1", "price":100, "quantity":10})
        self.no_name = self.sale.create_sale({"price":50, "quantity":100})
        self.no_price = self.sale.create_sale({"name":"no price", "quantity":30})
        self.no_quantity = self.sale.create_sale({"name": "no quantity"})

    def tearDown(self):
        self.product.no_of_products.clear()
        self.sale.no_of_sales.clear()