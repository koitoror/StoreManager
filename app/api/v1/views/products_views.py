# third-party imports
from flask_restplus import Resource
from flask import request
from functools import wraps

# local imports
from ..models.products import Product as ProductClass
from ..utils.dto import ProductsDto, product_parser, update_product_parser
from ..utils.decorators import token_required

api = ProductsDto.api
products = ProductsDto.products
post_products = ProductsDto.post_products

product = ProductClass()


@api.route("/products")
class ProductList(Resource):
    """Displays a list of all products and lets you POST to add new products."""

    @api.expect(post_products)
    @api.doc('creates an product', security='apikey')
    @api.response(201, "Created")
    @token_required
    def post(self):
        """Creates a new Product."""
        args = product_parser.parse_args()
        return product.create_product(args),201

    @api.doc("list_products", security='apikey')
    @api.response(404, "Products Not Found")
    @api.marshal_list_with(products, envelope="products")
    @token_required
    def get(self):
        """List all Products"""
        return product.get_all()

@api.route("/products/<int:productId>")
@api.param("productId", "product identifier")
@api.response(404, 'Product not found')
class Product(Resource):
    """Displays a single product item and lets you delete them."""

    @api.marshal_with(products)
    @api.doc('get one product', security='apikey')
    @token_required
    def get(self, productId):
        """Displays a single Product."""
        return product.get_one(productId)

    @api.marshal_with(products)
    @api.doc('updates an product', security='apikey')
    @api.expect(post_products)
    @token_required
    def put(self, productId):
        """Updates a single Product."""
        args = update_product_parser.parse_args()
        return product.update_product(productId, args)

    @api.marshal_with(products)
    @api.doc('deletes an product', security='apikey')
    @api.response(204, 'Product Deleted')
    @token_required
    def delete(self, productId):
        """Deletes a single Product."""
        product.delete_product(productId)
        return '',204