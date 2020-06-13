import jwt

JWT_ALGORITHM = 'HS256' 

def create_token(data, secret):
    jwt_token = jwt.encode(data, secret, JWT_ALGORITHM)
    
    return jwt_token

def verify_signature(token):
    try:
        data = jwt.decode(token, 'acelera', JWT_ALGORITHM)
        return data
    except Exception as err:
        return {"error": 2}