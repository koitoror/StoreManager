from flask_restplus import Api
from flask import Blueprint, request

from .api.v1.views.products_views import api as products_ns
from .api.v1.views.sales_views import api as sales_ns
from functools import wraps

# blueprint = Blueprint('api', __name__)

# api = Api(
#     blueprint,
#     title='StoreManager',
#     doc='/api/documentation',
#     version='1.0',
#     description='StoreManager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store.'
# )

# api_v1 = Blueprint('api', __name__, url_prefix=/api/v1')

api_v1 = Blueprint('api', __name__)


authorizations = {
    'apikey' : {
        'type' : 'apiKey',
        'in' : 'header',
        'name' : 'x-access-token'
    }
}

api = Api(
    api_v1, 
    title='StoreManager API :: v1',
    doc='/api/documentation',
    version='1.0',
    authorizations=authorizations,
    description='StoreManager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store. A simple StoreManager API',
)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return {'message' : 'Token is missing.'}, 401

        if token != 'mytoken':
            return {'message' : 'Your token is wrong, wrong, wrong!!!'}, 401

        print('TOKEN: {}'.format(token))
        return f(*args, **kwargs)

    return decorated

# ns = api.namespace('users', description='USERS operations')
# ns0 = api.namespace('products', description='PRODUCTS operations')
# ns1 = api.namespace('sales', description='SALES operations')

# api.add_namespace(products_ns path=/api/v1')
# api.add_namespace(sales_ns path=/api/v1')

api.add_namespace(products_ns, path='/api/v1')
api.add_namespace(sales_ns, path='/api/v1')