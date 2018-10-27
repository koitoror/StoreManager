from ..utils.sdto import api

class Sale(object):
    """Defines the Product model"""
    def __init__(self, product_id, product_name, product_category, user_id):
        self.product_id = product_id
        self.product_name = product_name
        self.product_category = product_category
        self.created_by = user_id
    
    @staticmethod
    def add_product(cursor, product_name, product_category, user_id):
        query = "INSERT INTO products (product_name, product_category, user_id) VALUES (%s, %s, %s)"
        cursor.execute(query, (product_name, product_category, user_id))

    @staticmethod
    def get_product_by_id(dict_cursor, productId):
        query_string="SELECT * FROM products WHERE id=%s"
        dict_cursor.execute(query_string, [productId])
        data = dict_cursor.fetchone()
        if not data:
            api.abort(404, "Product {} not found".format(productId))
        product = {key:str(value) for key, value in data.items() if value is not str}
        return product
     

    @staticmethod   
    def modify_product(dict_cursor, cursor, product_name, product_category, productId, user_id):
        data = Product.get_product_by_id(dict_cursor, productId)
        if data["user_id"] != str(user_id):
            api.abort(401, "Unauthorized")
        query = "UPDATE products SET product_name=%s, product_category=%s WHERE (id=%s)"
        cursor.execute(query, (product_name, product_category, productId))

    @staticmethod   
    def delete_product(dict_cursor, cursor, productId, user_id):
        data = Product.get_product_by_id(dict_cursor, productId)
        if data["user_id"] != str(user_id):
            api.abort(401, "Unauthorized")
        query = "DELETE FROM products WHERE id=%s"
        dict_cursor.execute(query, [productId])

    @staticmethod   
    def get_all(dict_cursor, user_id):
        query_string="SELECT * FROM products WHERE user_id = %s"
        dict_cursor.execute(query_string, [user_id])
        products = dict_cursor.fetchall()
        results = []
        for product in products:
            obj = {
                "id":product["id"],
                "product_name":product["product_name"],
                "product_category":product["product_category"],
                "user_id":product["user_id"],
                "created_at":product["created_at"].strftime('%d-%b-%Y : %H:%M:%S'),
            }
            results.append(obj)
        return results

        