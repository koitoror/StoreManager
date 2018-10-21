import json

from app.tests.base import BaseTestCase



class TestSale(BaseTestCase):
    """Test sales Endpoints."""

    def create(self):
        """Create sale with required fields (name, price, quantity)."""
        return self.client.post(
            '/api/v1/sales',
            data=json.dumps(self.data),
            content_type='application/json'
        )

    def create_no_name(self):
        """Create sale with no name."""
        return self.client.post(
            '/api/v1/sales',
            data=json.dumps(self.no_name),
            content_type='application/json'
        )

    def create_no_price(self):
        """Create sale with no price."""
        return self.client.post(
            '/api/v1/sales',
            data=json.dumps(self.no_price),
            content_type='application/json'
        )

    def create_no_json_data(self):
        """Create no json data"""
        return self.client.post(
            '/api/v1/sales',
            data=json.dumps(self.data)
        )


    def test_create_sale(self):
        """Test create sale endpoint
        """
        with self.client:
            res = self.create()
            self.assertEqual(res.status_code, 201)
            self.assertIn(b"test1",res.data)


    def test_get_sales(self):
        """Test get sale endpoint
        """
        with self.client:
            res = self.create()
            self.assertEqual(res.status_code, 201)
            access_token = 'mytoken'
            headers = {'Authorizations': 'Bearer {}'.format(access_token)}       
            return self.client.post(
            '/api/v1/sales',
            data=json.dumps(self.data),
            content_type='application/json',
            headers=headers
            )
            self.assertEqual(res.status_code, 200)
            self.assertIn(b"test",res.data )


    def test_get_one_sale(self):
        """Test get_one sale endpoint
        """
        with self.client:
            res = self.create()
            self.assertEqual(res.status_code, 201)
            result = self.client.get(
                '/api/v1/sales/{}'.format(res.get_json()['id'])
            )
            self.assertEqual(result.status_code, 200)
            self.assertIn(b"test",result.data )

    def test_delete_sale(self):
        """Test delete sale endpoint
        """
        with self.client:
            res = self.create()
            self.assertEqual(res.status_code, 201)
            result = self.client.delete(
                '/api/v1/sales/{}'.format(res.get_json()['id'])
            )
            self.assertEqual(result.status_code, 204)
            self.assertNotIn(b'test', result.data)
            res = self.client.get(
                '/api/v1/sales/'
            )
            self.assertEqual(res.status_code, 404)

    def test_update_sale(self):
        """Test update sale endpoint
        """
        with self.client:
            res = self.create()
            self.assertEqual(res.status_code, 201)
            result = self.client.put(
                '/api/v1/sales/{}'.format(res.get_json()['id']),
                data=json.dumps({"name":"gum-balls", "price":30, "quantity":50}),
                content_type='application/json'
            )
            self.assertEqual(result.status_code, 200)
            self.assertIn(b"gum-balls",result.data )

    def test_add_sale_without_name(self):
        """Test add sale without name."""
        with self.client:
            res = self.create_no_name()
            self.assertEqual(res.status_code, 400)
            name = res.get_json()['errors']['name']
            message = res.get_json()['message']
            self.assertIn("name should be a string Missing required parameter", name)
            self.assertIn("Input payload validation failed", message)

    def test_add_sale_without_price(self):
        """Test add sale without price."""
        with self.client:
            res = self.create_no_price()
            self.assertEqual(res.status_code, 400)
            price = res.get_json()['errors']['price']
            message = res.get_json()['message']
            self.assertIn("price should be a integer Missing required parameter", price)
            self.assertIn("Input payload validation failed", message)

    def test_add_no_json_data(self):
        "Test cannot add no json data"
        with self.client:
            res = self.create_no_json_data()
            self.assertTrue(res.status_code, 400)
            message = res.get_json()['message']
            self.assertIn('Input payload validation failed', message)

