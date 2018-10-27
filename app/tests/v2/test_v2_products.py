import unittest
from app.tests.v2.base import BaseTestCase
from app.tests.v2.helpers import register_user, login_user


class ProductsTestCase(BaseTestCase):
    """Represents the products test case"""

    def test_product_creation(self):
        """Test API can create a product.""" 

        with self.client:
            res = register_user(self)
            self.assertTrue(res.status_code, 201)
            res = login_user(self)
            access_token = res.get_json()['token']

            # create product by making a POST request
            rv = self.client.post(
                'api/v2/products',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=self.product
                )
            self.assertEqual(rv.status_code, 201)
            self.assertIn(b'Product added successfully', rv.data)

    def test_api_can_get_all_products(self):
        """Test API can get all."""
        with self.client:
            register_user(self)
            res = login_user(self)
            access_token = res.get_json()['token']

            # create an product
            res = self.client.post(
                'api/v2/products',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=self.product
                )
            self.assertEqual(res.status_code, 201)

            # get all the products that belong to a specific user
            res = self.client.get(
                'api/v2/products',
                 headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
            )
            self.assertEqual(res.status_code, 200)
            self.assertIn(b'first test', res.data)

    def test_api_can_get_product_by_id(self):
        """Test API can get a single product by using it's id."""
        with self.client:
            register_user(self)
            res = login_user(self)
            access_token = res.get_json()['token']

            # create an product
            res = self.client.post(
                'api/v2/products',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=self.product
                )
            self.assertEqual(res.status_code, 201)

            # get all the products that belong to a specific user
            res = self.client.get(
                'api/v2/products/1',
                 headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
            )
            self.assertEqual(res.status_code, 200)
            self.assertIn(b'first test', res.data)

    def test_product_can_be_edited(self):
        """Test API can edit an existing product. (PUT request)"""
        with self.client:
            register_user(self)
            res = login_user(self)
            access_token = res.get_json()['token']

            # create an product
            res = self.client.post(
                'api/v2/products',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=self.product
                )
            self.assertEqual(res.status_code, 201)

            # modify an product
            rv = self.client.put(
                '/api/v2/products/1',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=self.update_product
                )
            self.assertEqual(rv.status_code, 200)

            res = self.client.get(
                'api/v2/products/1',
                 headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
            )
            self.assertIn(b'first edition', res.data)

    def test_product_deletion(self):
        """Test API can delete an existing product."""
        with self.client:
            register_user(self)
            res = login_user(self)
            access_token = res.get_json()['token']

            # create an product
            res = self.client.post(
                'api/v2/products',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=self.product
                )
            self.assertEqual(res.status_code, 201)
            
            # delete an product
            res = self.client.delete(
                '/api/v2/products/1',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                }
                )
            self.assertTrue(res.status_code, 200)
            self.assertIn(b"Product deleted successully", res.data)
            # test for product not found
            res = self.client.get(
                '/api/v2/products/1',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                }
                )
            self.assertEqual(res.status_code, 404)
            self.assertIn(b"Product 1 not found", res.data)

if __name__ == "__main__":
    unittest.main()