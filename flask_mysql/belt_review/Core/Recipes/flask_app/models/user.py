from flask_app.config.mysqlconnection import connectToMySQL, DB
from flask_app import app
from flask_bcrypt import Bcrypt
from flask import flash
import re
bcrypt = Bcrypt(app)

class User:
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

    def __init__(self, data):
        self.id= data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Get user by ID
    @classmethod
    def get_by_id(cls , data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DB).query_db(query , data)

        if results:
            user = cls(results[0])
            return user
        return False

    # Get user by email
    @classmethod
    def get_by_email(cls , data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DB).query_db(query , data)

        if results:
            user = cls(results[0])
            return user
        return False

    # Register 
    @classmethod
    def register(cls , data):
        data = dict(data)
        data['password'] = bcrypt.generate_password_hash(data['password'])
        query = "INSERT INTO users (first_name , last_name , email , password) VALUES(%(first_name)s , %(last_name)s , %(email)s , %(password)s);"
        return connectToMySQL(DB).query_db(query , data)\
    
    # Register validation for validating register form
    @staticmethod
    def validate_registration(data):
        is_valid = True
        user = User.get_by_email(data)

        if not(User.EMAIL_REGEX.match(data['email'])) or user:
            flash("Invalid Email")
            is_valid = False
        if len(data['first_name']) < 2:
            flash("Invalid First Name")
            is_valid = False
        if len(data['last_name']) < 2:
            flash("Invalid Last Name")
            is_valid = False
        if data['password'] != data['confirm_password']:
            flash("Passwords don't match")
            is_valid = False

        return is_valid
    
    # login validation for validating login form
    @staticmethod
    def validate_login(data):
        is_valid = True
        user = User.get_by_email(data)

        if not(user):
            flash("User not found in database")
            is_valid = False
        elif not(bcrypt.check_password_hash(user.password , data['password'])):
            flash("Wrong password")
            is_valid = False
        return is_valid