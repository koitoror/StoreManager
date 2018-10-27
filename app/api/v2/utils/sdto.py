from flask_restplus import Namespace, fields, reqparse

api = Namespace("sales", description="Sales related operations")

sales = api.model("sales", {
    "id": fields.Integer(readonly=True),
    "product_name":fields.String(required=True, description="The product product_name"),
    "product_category":fields.String(required=True, description="The product product_category"),
    "user_id":fields.String(required=True, description="The product user_id"),
    "created_at":fields.String(required=True, description="The product creation date")
    })

post_sales = api.model("post_sales", {
        "product_name": fields.String(required=True,description="sales product_name", example='This is my first product.'),
        "product_category": fields.String(required=True,description="sales product_category", example='This is my first category.')
    }
)

product_parser = reqparse.RequestParser()
product_parser.add_argument('product_name', required=True, type=str, help='product_name should be a string')
product_parser.add_argument('product_category', required=True, type=str, help='product_category should be a string')

update_product_parser = reqparse.RequestParser()
update_product_parser.add_argument('product_name', required=True, type=str, help='product_name should be a string')
update_product_parser.add_argument('product_category', required=True, type=str, help='product_category should be a string')