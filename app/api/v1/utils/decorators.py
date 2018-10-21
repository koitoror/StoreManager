from functools import wraps

def token_required(f):
    """Ensures user is logged in before action
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # user_id = ""
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            
            return {'message' : 'Token is missing.'}, 401

        if token != 'mytoken':
            return {'message' : 'Your token is wrong, wrong, wrong!!!'}, 401

        return f(*args, **kwargs)

    return decorated