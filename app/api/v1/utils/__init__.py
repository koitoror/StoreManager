"""Main API Product Point"""

from flask_restplus import Api


api = Api(
    
    title='StoreManager API :: v1',
    doc='/documentation',
    version='1.0',
    description='StoreManager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store. A simple StoreManager API',
)