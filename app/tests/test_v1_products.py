import json

from app.tests.base import BaseTestCase



class TestProduct(BaseTestCase):
    """Test Products Endpoints."""

    def create(self):
        """Create product with required fields (title, description)."""
        return self.client.post(
            '/api/v1/products',
            data=json.dumps(self.data),
            content_type='application/json'
        )

    def create_no_title(self):
        """Create product with no title."""
        return self.client.post(
            '/api/v1/products',
            data=json.dumps(self.no_title),
            content_type='application/json'
        )

    def create_no_description(self):
        """Create product with no description."""
        return self.client.post(
            '/api/v1/products',
            data=json.dumps(self.no_description),
            content_type='application/json'
        )

    def create_no_json_data(self):
        """Create no json data"""
        return self.client.post(
            '/api/v1/products',
            data=json.dumps(self.data)
        )


    def test_create_product(self):
        """Test create product endpoint
        """
        with self.client:
            res = self.create()
            self.assertEqual(res.status_code, 201)
            self.assertIn(b"test1",res.data)


    def test_get_products(self):
        """Test get product endpoint
        """
        with self.client:
            res = self.create()
            self.assertEqual(res.status_code, 201)
            res = self.client.get(
                '/api/v1/products',
                content_type='application/json'
            )
            self.assertEqual(res.status_code, 200)
            self.assertIn(b"test",res.data )


    def test_get_one_product(self):
        """Test get_one product endpoint
        """
        with self.client:
            res = self.create()
            self.assertEqual(res.status_code, 201)
            result = self.client.get(
                '/api/v1/products/{}'.format(res.get_json()['id'])
            )
            self.assertEqual(result.status_code, 200)
            self.assertIn(b"test",result.data )

    def test_delete_product(self):
        """Test delete product endpoint
        """
        with self.client:
            res = self.create()
            self.assertEqual(res.status_code, 201)
            result = self.client.delete(
                '/api/v1/products/{}'.format(res.get_json()['id'])
            )
            self.assertEqual(result.status_code, 204)
            self.assertNotIn(b'test', result.data)
            res = self.client.get(
                '/api/v1/products/'
            )
            self.assertEqual(res.status_code, 404)

    def test_update_product(self):
        """Test update product endpoint
        """
        with self.client:
            res = self.create()
            self.assertEqual(res.status_code, 201)
            result = self.client.put(
                '/api/v1/products/{}'.format(res.get_json()['id']),
                data=json.dumps({"name":"soccer", "description":"france are the 2018 world champions"}),
                content_type='application/json'
            )
            self.assertEqual(result.status_code, 200)
            self.assertIn(b"soccer",result.data )

    def test_add_product_without_name(self):
        """Test add product without name."""
        with self.client:
            res = self.create_no_title()
            self.assertEqual(res.status_code, 400)
            name = res.get_json()['errors']['name']
            message = res.get_json()['message']
            self.assertIn("name should be a string Missing required parameter", name)
            self.assertIn("Input payload validation failed", message)

    def test_add_product_without_description(self):
        """Test add product without description."""
        with self.client:
            res = self.create_no_description()
            self.assertEqual(res.status_code, 400)
            description = res.get_json()['errors']['description']
            message = res.get_json()['message']
            self.assertIn("description should be a string Missing required parameter", description)
            self.assertIn("Input payload validation failed", message)

    def test_add_no_json_data(self):
        "Test cannot add no json data"
        with self.client:
            res = self.create_no_json_data()
            self.assertTrue(res.status_code, 400)
            message = res.get_json()['message']
            self.assertIn('Input payload validation failed', message)

