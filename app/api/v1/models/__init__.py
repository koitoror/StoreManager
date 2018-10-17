"""Main API Product Point"""

from flask_restplus import Api

# initializing the api
# api = Api(
#     version='1.0',
#     title='StoreManager',
#     description='StoreManager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store.',
#     doc='/api/documentation'
# )


api = Api(
    # api_v1, 
    title='StoreManager API :: v1',
    doc='/documentation',
    version='1.0',
    # authorizations=authorizations,
    description='StoreManager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store. A simple StoreManager API',
)