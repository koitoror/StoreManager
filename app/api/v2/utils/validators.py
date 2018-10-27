import re

def validate_user_data(user):
    """ this funtion validates the user data """

    user['username'] = user['username'].lower()

    if user['username'] == '':
        return {'warning': 'username is a required field'}, 400

    # Check for empty email
    elif user['email'] == '':
        return {'warning': 'email is a required field'}, 400

    # Check for empty password
    elif user['password'] == '':
        return {'warning': 'password is a required field'}, 400

    elif user['password'] == 'password':
        return {'warning': "password cannot be 'password'"}, 400

    elif user['password'].strip(' ').isdigit():
        return {'warning': 'password should be alphanumeric'}, 400

    elif user['password'] != user['confirm']:
        return {'warning': 'password mismatch!'}, 400

    # Check for a valid user name
    if not re.match(r'^[a-zA-Z0-9_.+-]+$', user['username'].strip(' ')):
        return {'warning': 'Enter a valid username'}, 400

    if user['username'].strip(' ').isdigit():
        return {'warning': 'Enter a non digit username'}, 400

    # Check for a valid email
    if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
            user['email'].strip(' ')):
        return {'warning': 'Enter a valid email address'}, 400

    # check for a valid password
    if not user["password"].strip():
        return {"warning": "Enter a valid password"}, 400

    # Check for large/long inputs
    if len(user['username']) > 15:
        return {'warning': 'username is too long'}, 400

    elif len(user['email']) > 50:
        return {'warning': 'email is too long'}, 400

    elif len(user['password']) < 6:
        return {'warning': 'password requires atlest 6 characters'}, 400

def validate_product_data(product):
    """ this funtion validates the product data """

    # Check for empty product_name
    if product['product_name'] == '':
        return {'warning': 'product_name is a required field'}, 400

    # Check for empty product_category
    elif product['product_category'] == '':
        return {'warning': 'product_category is a required field'}, 400
    
    # check for a valid product_name
    if product['product_name'].strip(' ').isdigit():
        return {'warning': 'Enter a non digit product_name'}, 400

    if not product["product_name"].strip():
        return {"warning": "Enter a valid product_name"}, 400
    
    # check for valid product_category
    if product['product_category'].strip(' ').isdigit():
        return {'warning': 'Enter non digit product_category'}, 400

    if not product["product_category"].strip():
        return {"warning": "Enter valid product_category"}, 400

    # Check for large/long inputs
    if len(product['product_name']) > 50:
        return {'warning': 'product_name is too long'}, 400


def validate_update_product(product, data):
    """ this funtion validates the updated product data """

    # Check for empty product_name
    if data['product_name'] == '':
        data['product_name'] = product['product_name']

    # Check for empty product_category
    if data['product_category'] == '':
        data['product_category'] = product['product_category']
    
    # check for a valid product_name
    if data['product_name'].strip(' ').isdigit():
        return {'warning': 'Enter a non digit product_name'}, 400

    if not data["product_name"].strip():
        return {"warning": "Enter a valid product_name"}, 400
    
    # check for valid product_category
    if data['product_category'].strip(' ').isdigit():
        return {'warning': 'Enter non digit product_category'}, 400

    if not data["product_category"].strip():
        return {"warning": "Enter valid product_category"}, 400

    # Check for large/long inputs
    if len(data['product_name']) > 50:
        return {'warning': 'product_name is too long'}, 400
