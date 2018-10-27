import json
from flask_testing import TestCase
from run import app
from app.database import Database

from app.api.v2.models.user import User
from app.api.v2.models.product import Product


class BaseTestCase(TestCase):
    """ Base Tests """

    @classmethod
    def create_app(cls):
        app.config.from_object('instance.config.TestingConfig')
        return app

    def setUp(self):
        self.db = Database(testing="testing")
        self.cursor = self.db.cursor
        self.dict_cursor = self.db.dict_cursor
        self.db.create_tables()
        
        self.user = User(
            user_id=1,
            username="kamardaniel",
            email='kamardaniel@gmail.com',
            password='password',
            confirm='password'
        )
        self.product_obj = Product(
            product_id=1,
            product_name="first product model test",
            product_category='testing is very essential',
            user_id="1"
        )
        self.product = json.dumps(
            {
                "product_name": "first test",
                "product_category": "tdd is awesome"
            }
        )
        self.product_no_product_name = json.dumps(
            {
                "product_name": "",
                "product_category": "tdd is awesome"
            }
        )
        self.product_no_product_category = json.dumps(
            {
                "product_name": "first test",
                "product_category": ""
            }
        )
        self.update_product = json.dumps(
            {
                "product_name": "first edition",
                "product_category": "tdd is very awesome"
            }
        )

    def tearDown(self):
        self.db.drop_all()