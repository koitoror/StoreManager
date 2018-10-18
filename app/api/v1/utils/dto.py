from flask_restplus import Namespace, fields, reqparse

class ProductsDto(object):
    api = Namespace("products", description="products related operations")
    products = api.model(
        "products", {
        "id": fields.Integer(),
        "creation_date": fields.String(),
        "modified_date": fields.String(),
        "name":fields.String(required=True, description="The product name"),
        "price":fields.Integer(required=True, description="The product price"),
        "quantity":fields.Integer(required=True, description="The product quantity")

        }
    )
    post_products = api.model("post_products",{
        "name": fields.String("products name"),
        "price": fields.Integer("products price"),
        "quantity": fields.Integer("products quantity")

    })

product_parser = reqparse.RequestParser()
product_parser.add_argument('name', required=True, type=str, help='name should be a string')
product_parser.add_argument('price', required=True, type=int, help='price should be a integer')
product_parser.add_argument('quantity', required=True, type=int, help='quantity should be a integer')

update_product_parser = reqparse.RequestParser()

update_product_parser.add_argument('name', type=str, help='name should be a string')
update_product_parser.add_argument('price', type=int, help='price should be a integer')
update_product_parser.add_argument('quantity', type=int, help='quantity should be a integer')


class SalesDto(object):
    api = Namespace("sales", description="Sales related operations")
    sales = api.model(
        "sales", {
        "id": fields.Integer(),
        "creation_date": fields.String(),
        "modified_date": fields.String(),
        "name":fields.String(required=True, description="The sale name"),
        "price":fields.Integer(required=True, description="The sale price"),
        "quantity":fields.Integer(required=True, description="The sale quantity")

        }
    )
    post_sales = api.model("post_sales",{
        "name": fields.String("sales name"),
        "price": fields.Integer("sales price"),
        "quantity": fields.Integer("sales quantity")

    })

sale_parser = reqparse.RequestParser()
sale_parser.add_argument('name', required=True, type=str, help='name should be a string')
sale_parser.add_argument('price', required=True, type=int, help='price should be a integer')
sale_parser.add_argument('quantity', required=True, type=int, help='quantity should be a integer')

update_sale_parser = reqparse.RequestParser()

update_sale_parser.add_argument('name', type=str, help='name should be a string')
update_sale_parser.add_argument('price', type=int, help='price should be a integer')
update_sale_parser.add_argument('quantity', type=int, help='quantity should be a integer')