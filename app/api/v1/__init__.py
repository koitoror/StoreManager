from flask_restplus import Api
from flask import Blueprint

from .views.products_views import api as products_ns
from .views.sales_views import api as sales_ns



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




api.add_namespace(products_ns, path='/api/v1')
api.add_namespace(sales_ns, path='/api/v1')