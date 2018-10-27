# import json
# from app.tests.v2.base import BaseTestCase
# from app.tests.v2.helpers import register_user, login_user

# class TestValidatorsCase(BaseTestCase):
#     "Class for testing validators"

#     def test_username_is_required(self):
#         """test username is a required field."""
#         res = self.client.post(
#         'api/v2/auth/signup',
#         data=json.dumps(dict(
#             username='',
#             email='kamardaniel@gmail.com',
#             password='password123',
#             confirm='password123'
#         )),
#         content_type='application/json'
#         )
#         self.assertTrue(res.status_code, 400)
#         self.assertIn(b"username is a required field", res.data)

#     def test_username_length(self):
#         """test username requires at most 10 characters."""
#         res = self.client.post(
#         'api/v2/auth/signup',
#         data=json.dumps(dict(
#             username='kamardaniel1kamardaniel2',
#             email='kamardaniel@gmail.com',
#             password='password123',
#             confirm='password123'
#         )),
#         content_type='application/json'
#         )
#         self.assertTrue(res.status_code, 400)
#         self.assertIn(b"username is too long", res.data)

#     def test_email_length(self):
#         """test email is a required field."""
#         res = self.client.post(
#         'api/v2/auth/signup',
#         data=json.dumps(dict(
#             username='kamar',
#             email='kamardanielmoffatngiggelucaamugogokinyakinyanjui@gmail.com',
#             password='password123',
#             confirm='password123'
#         )),
#         content_type='application/json'
#         )
#         self.assertTrue(res.status_code, 400)
#         self.assertIn(b"email is too long", res.data)

#     def test_email_is_required(self):
#         """test email is a required field."""
#         res = self.client.post(
#         'api/v2/auth/signup',
#         data=json.dumps(dict(
#             username='kamar',
#             email='',
#             password='password123',
#             confirm='password123'
#         )),
#         content_type='application/json'
#         )
#         self.assertTrue(res.status_code, 400)
#         self.assertIn(b"email is a required field", res.data)

#     def test_password_is_required(self):
#         """test password is a required field."""
#         res = self.client.post(
#         'api/v2/auth/signup',
#         data=json.dumps(dict(
#             email='kamardaniel@gmail.com',
#             username='kamar',
#             password='',
#             confirm='password123'
#         )),
#         content_type='application/json'
#         )
#         self.assertTrue(res.status_code, 400)
#         self.assertIn(b"password is a required field", res.data)

#     def test_password_is_valid(self):
#         """test password is not whitespace."""
#         res = self.client.post(
#         'api/v2/auth/signup',
#         data=json.dumps(dict(
#             email='kamardaniel@gmail.com',
#             username='kamar',
#             password='      ',
#             confirm='      '
#         )),
#         content_type='application/json'
#         )
#         self.assertTrue(res.status_code, 400)
#         self.assertIn(b"Enter a valid password", res.data)

#     def test_password_requires_6_characters(self):
#         """test password requires atleast six characters."""
#         res = self.client.post(
#         'api/v2/auth/signup',
#         data=json.dumps(dict(
#             email='kamardaniel@gmail.com',
#             username='kamar',
#             password='pass',
#             confirm='pass'
#         )),
#         content_type='application/json'
#         )
#         self.assertTrue(res.status_code, 400)
#         self.assertIn(b"password requires atlest 6 characters", res.data)

#     def test_valid_email_format(self):
#         res = self.client.post(
#         'api/v2/auth/signup',
#         data=json.dumps(dict(
#             email='kamardanielgmail.com',
#             username='kamar',
#             password='password123',
#             confirm='password123'
#         )),
#         content_type='application/json'
#         )
#         self.assertTrue(res.status_code, 400)
#         self.assertIn(b"Enter a valid email address", res.data)

#     def test_password_must_match_to_register(self):
#         res = self.client.post(
#         'api/v2/auth/signup',
#         data=json.dumps(dict(
#             email='kamardaniel@gmail.com',
#             username='kamar',
#             password='passwor',
#             confirm='password123'
#         )),
#         content_type='application/json'
#         )
#         self.assertTrue(res.status_code, 400)
#         self.assertIn(b"password mismatch", res.data)

#     def test_non_digit_username(self):
#         """test non-digit username."""
#         res = self.client.post(
#         'api/v2/auth/signup',
#         data=json.dumps(dict(
#             email='kamardaniel@gmail.com',
#             username='12345',
#             password='password123',
#             confirm='password123'
#         )),
#         content_type='application/json'
#         )
#         self.assertTrue(res.status_code, 400)
#         self.assertIn(b"Enter a non digit username", res.data)

#     def test_valid_username(self):
#         """test valid username format."""
#         res = self.client.post(
#         'api/v2/auth/signup',
#         data=json.dumps(dict(
#             email='kamardaniel@gmail.com',
#             username='      ',
#             password='password123',
#             confirm='password123'
#         )),
#         content_type='application/json'
#         )
#         self.assertTrue(res.status_code, 400)
#         self.assertIn(b"Enter a valid username", res.data)

#     def test_product_name_is_required(self):
#         "Test product_name is a required property"
#         with self.client:
#             res = register_user(self)
#             self.assertTrue(res.status_code, 201)
#             res = login_user(self)
#             access_token = res.get_json()['token']

#             # create product by making a POST request
#             rv = self.client.post(
#                 'api/v2/products',
#                 headers={
#                     "x-access-token": access_token,
#                     "content-type": "application/json"
#                 },
#                 data=self.product_no_product_name
#                 )
#             self.assertEqual(rv.status_code, 400)
#             self.assertIn(b"product_name is a required field", rv.data)

#     def test_product_category_is_required(self):
#         "Test product_category is a required property"
#         with self.client:
#             res = register_user(self)
#             self.assertTrue(res.status_code, 201)
#             res = login_user(self)
#             access_token = res.get_json()['token']

#             # create product by making a POST request
#             rv = self.client.post(
#                 'api/v2/products',
#                 headers={
#                     "x-access-token": access_token,
#                     "content-type": "application/json"
#                 },
#                 data=self.product_no_product_category
#                 )
#             self.assertEqual(rv.status_code, 400)
#             self.assertIn(b"product_category is a required field", rv.data)

#     def test_non_digit_product_category(self):
#         "test for non-digig product_category."
#         with self.client:
#             res = register_user(self)
#             self.assertTrue(res.status_code, 201)
#             res = login_user(self)
#             access_token = res.get_json()['token']

#             # create product by making a POST request
#             rv = self.client.post(
#                 'api/v2/products',
#                 headers={
#                     "x-access-token": access_token,
#                     "content-type": "application/json"
#                 },
#                 data=json.dumps(
#                     {"product_name": "first test",
#                     "product_category": "11111111"
#                     })
#                 )
#             self.assertEqual(rv.status_code, 400)
#             self.assertIn(b"Enter non digit product_category", rv.data)

#     def test_valid_product_category(self):
#         "test product_category entered in valid format"
#         with self.client:
#             res = register_user(self)
#             self.assertTrue(res.status_code, 201)
#             res = login_user(self)
#             access_token = res.get_json()['token']

#             # create product by making a POST request
#             rv = self.client.post(
#                 'api/v2/products',
#                 headers={
#                     "x-access-token": access_token,
#                     "content-type": "application/json"
#                 },
#                 data=json.dumps(
#                     {"product_name": "first test",
#                     "product_category": "    "
#                     })
#                 )
#             self.assertEqual(rv.status_code, 400)
#             self.assertIn(b"Enter valid product_category", rv.data)

#     def test_valid_product_name(self):
#         "test product_name entered in valid format"
#         with self.client:
#             res = register_user(self)
#             self.assertTrue(res.status_code, 201)
#             res = login_user(self)
#             access_token = res.get_json()['token']

#             # create product by making a POST request
#             rv = self.client.post(
#                 'api/v2/products',
#                 headers={
#                     "x-access-token": access_token,
#                     "content-type": "application/json"
#                 },
#                 data=json.dumps(
#                     {"product_name": "    ",
#                     "product_category": "this is very awsome"
#                     })
#                 )
#             self.assertEqual(rv.status_code, 400)
#             self.assertIn(b"Enter a valid product_name", rv.data)

#     def test_product_name_length(self):
#         "test product_name is less than 50 characters"
#         with self.client:
#             res = register_user(self)
#             self.assertTrue(res.status_code, 201)
#             res = login_user(self)
#             access_token = res.get_json()['token']

#             # create product by making a POST request
#             rv = self.client.post(
#                 'api/v2/products',
#                 headers={
#                     "x-access-token": access_token,
#                     "content-type": "application/json"
#                 },
#                 data=json.dumps(
#                     {"product_name": "thisisthelongestproduct_nameeveranitshouldbemorethanfiftycharacterslong",
#                     "product_category": "this is very awsome"
#                     })
#                 )
#             self.assertEqual(rv.status_code, 400)
#             self.assertIn(b"product_name is too long", rv.data)
