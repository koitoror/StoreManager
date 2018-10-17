from flask_restplus import Namespace, fields, reqparse

class ProductsDto(object):
    api = Namespace("products", description="products related operations")
    products = api.model(
        "products", {
        "id": fields.Integer(),
        "creation_date": fields.String(),
        "modified_date": fields.String(),
        "name":fields.String(required=True, description="The product name"),
        "description":fields.String(required=True, description="The product description")
        }
    )
    post_products = api.model("post_products",{
        "name": fields.String("products name"),
        "description": fields.String("products description")
    })

product_parser = reqparse.RequestParser()
product_parser.add_argument('name', required=True, type=str, help='name should be a string')
product_parser.add_argument('description', required=True, type=str, help='description should be a string')
update_product_parser = reqparse.RequestParser()

update_product_parser.add_argument('name', type=str, help='name should be a string')
update_product_parser.add_argument('description', type=str, help='description should be a string')


class SalesDto(object):
    api = Namespace("sales", description="Sales related operations")
    sales = api.model(
        "sales", {
        "id": fields.Integer(),
        "creation_date": fields.String(),
        "modified_date": fields.String(),
        "name":fields.String(required=True, description="The sale name"),
        "description":fields.String(required=True, description="The sale description")
        }
    )
    post_sales = api.model("post_sales",{
        "name": fields.String("sales name"),
        "description": fields.String("sales description")
    })

sale_parser = reqparse.RequestParser()
sale_parser.add_argument('name', required=True, type=str, help='name should be a string')
sale_parser.add_argument('description', required=True, type=str, help='description should be a string')
update_sale_parser = reqparse.RequestParser()

update_sale_parser.add_argument('name', type=str, help='name should be a string')
update_sale_parser.add_argument('description', type=str, help='description should be a string')