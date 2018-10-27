# third-party imports
from flask_restplus import Resource

# local imports
from ..utils.sdto import api, sales, post_sales, product_parser, update_product_parser
from ..utils.decorators import token_required
from ..utils.validators import validate_product_data, validate_update_product
from ..models.sale import Sale
from app.database import Database


conn = Database()
cursor = conn.cursor
dict_cursor = conn.dict_cursor

@api.route("/sales")
class SaleList(Resource):
    """Displays a list of all products and lets you POST to add new products."""

    @api.expect(post_sales)
    @api.doc('adds a product')
    @api.response(201, "Created")
    @token_required
    @api.doc(security='apikey')
    @api.header('x-access-token', type=str, description='access token')
    def post(self, user_id):
        """Creates a new Product."""
        args = product_parser.parse_args()

        # validate the product payload
        invalid_data = validate_product_data(args)
        if invalid_data:
            return invalid_data

        product_name = args["product_name"]
        product_category = args["product_category"]
        Sale.add_product(cursor, product_name, product_category, user_id)
        return {"message": "Product added successfully"}, 201

    @api.doc("list_sales")
    @api.response(404, "Products Not Found")
    @api.marshal_list_with(sales, envelope="products")
    @token_required
    @api.doc(security='apikey')
    @api.header('x-access-token', type=str, description='access token')
    def get(self, user_id):
        """List all Products"""
        products = Sale.get_all(dict_cursor, user_id)
        if not products:
            api.abort(404, "No products for user {}".format(user_id))
        return products

@api.route("/sales/<int:saleId>")
@api.param("saleId", "sale identifier")
@api.response(404, 'Sale not found')
class SaleClass(Resource):
    """Displays a single product item and lets you delete them."""

    @api.marshal_with(sales)
    @api.doc('get one product')
    @token_required
    @api.doc(security='apikey')
    @api.header('x-access-token', type=str, description='access token')
    def get(self, user_id, productId):
        """Displays a single Product."""
        product = Sale.get_product_by_id(dict_cursor, productId)
        if product["user_id"] != str(user_id):
            api.abort(401, "Unauthorized to view this product")
        return product


    @api.doc('updates a sale')
    @api.expect(post_sales)
    @token_required
    @api.doc(security='apikey')
    @api.header('x-access-token', type=str, description='access token')
    def put(self, user_id, productId):
        """Updates a single Product."""
        args = update_product_parser.parse_args()
        product_name = args["product_name"]
        product_category = args["product_category"]
        product = {"product_name": product_name, "product_category":product_category}
        product = Sale.get_product_by_id(dict_cursor, productId)

        invalid_data = validate_update_product(product, args)

        if invalid_data:
            return invalid_data
        
        Sale.modify_product(dict_cursor, cursor, args["product_name"], args["product_category"], productId, user_id)
        return {"message": "Updated successfully", "product":product}

    @api.doc('deletes a sale')
    @api.response(204, 'Product Deleted')
    @token_required
    @api.doc(security='apikey')
    @api.header('x-access-token', type=str, description='access token')
    def delete(self, user_id, productId):
        """Deletes a single Product."""

        Sale.delete_product(dict_cursor, cursor, productId, user_id)
        return {"message": "Product deleted successully"}, 200