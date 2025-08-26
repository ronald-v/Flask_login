from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, username, password, fullname="") -> None:
        self.id = id
        self.username = username
        self.password = password
        self.fullname = fullname

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)
    
    @classmethod
    def generate_password(self, password):
        return generate_password_hash(password)
    
    # scrypt:32768:8:1$UDJFWeI7ELqFxayr$b0508f4b77f627d0df4bab8047af1bf1eb402ad99d8a8b59887152cc07a01d96c02b312e975206e8857e2b6361fcc7b186518e1b2e651fef339a9ea1721dcaeb