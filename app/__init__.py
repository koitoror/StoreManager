from flask_restplus import Api
from flask import Blueprint, request

from .api.v1.views.products_views import api as products_ns
from .api.v1.views.sales_views import api as sales_ns
from functools import wraps


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
    doc='/',
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


api.add_namespace(products_ns, path='/api/v1')
api.add_namespace(sales_ns, path='/api/v1')