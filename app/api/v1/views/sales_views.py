# third-party imports
from flask_restplus import Resource
from flask import request
from functools import wraps

# local imports
from ..models.sales import Sale as SaleClass
from ..utils.dto import SalesDto, sale_parser, update_sale_parser
from ..utils.decorators import token_required

api = SalesDto.api
sales = SalesDto.sales
post_sales = SalesDto.post_sales

sale = SaleClass()


@api.route("/sales")
class SaleList(Resource):
    """Displays a list of all sales and lets you POST to add new sales."""

    @api.expect(post_sales)
    @api.doc('creates an sale')
    @api.response(201, "Created")
    def post(self):
        """Creates a new Sale."""
        args = sale_parser.parse_args()
        return sale.create_sale(args),201

    @api.doc("list_sales", security='apikey')
    @api.response(404, "Sales Not Found")
    @api.marshal_list_with(sales, envelope="sales")
    @token_required
    def get(self):
        """List all Sales"""
        return sale.get_all()

@api.route("/sales/<int:saleId>")
@api.param("saleId", "sale identifier")
@api.response(404, 'Sale not found')
class Sale(Resource):
    """Displays a single sale item and lets you delete them."""

    @api.marshal_with(sales)
    @api.doc('get one sale')
    def get(self, saleId):
        """Displays a single Sale."""
        return sale.get_one(saleId)

    @api.marshal_with(sales)
    @api.doc('updates an sale')
    @api.expect(post_sales)
    def put(self, saleId):
        """Updates a single Sale."""
        args = update_sale_parser.parse_args()
        return sale.update_sale(saleId, args)

    @api.marshal_with(sales)
    @api.doc('deletes an sale')
    @api.response(204, 'Sale Deleted')
    def delete(self, saleId):
        """Deletes a single Sale."""
        sale.delete_sale(saleId)
        return '',204