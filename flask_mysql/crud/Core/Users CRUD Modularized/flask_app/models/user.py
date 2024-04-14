from flask_app.config.mysqlconnection import connectToMySQL

db = "users"
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    @classmethod
    def save(cls, data):
        query = '''
        INSERT INTO users (first_name, last_name, email, created_at, updated_at) 
        VALUES (%(fname)s, %(lname)s, %(email)s, NOW(), NOW());'''
        return connectToMySQL(db).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        results = connectToMySQL(db).query_db(query)
        if results:  # Check if results is not False
            users = []
            for user in results:
                users.append(cls(user))
            return users
        else:
            print("Error retrieving users from the database.")
            return []  # Return an empty list or handle the error appropriately
    
    @classmethod
    def get_one(cls, data):
        query = '''
        SELECT * FROM users 
        WHERE id=%(id)s;'''
        result = connectToMySQL(db).query_db(query, data)
        return cls(result[0])
        

    @classmethod
    def update(cls, data):
        query = '''
        UPDATE users SET first_name=%(fname)s, last_name=%(lname)s, email=%(email)s
        WHERE id=%(id)s;'''
        return connectToMySQL(db).query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        query = '''
        DELETE FROM users 
        WHERE id=%(id)s;'''
        return connectToMySQL(db).query_db(query, data)
    