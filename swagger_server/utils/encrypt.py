from datetime import datetime, timedelta
import bcrypt
import jwt
from swagger_server.config.access import access

config = access()

def encrypt_password(password: str):
    bytes = password.encode('utf-8')
    salt = config.get('SALT').encode('utf-8')
    return bcrypt.hashpw(bytes, salt).decode()


def generate_token(user_id: int):
    exp = datetime.now() + timedelta(minutes=1440)
    return jwt.encode({'user_id': user_id, 'exp': exp}, config.get('SALT').encode('utf-8'), algorithm="HS256")
