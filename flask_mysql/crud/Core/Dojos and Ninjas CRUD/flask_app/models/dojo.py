from flask_app.config.mysqlconnection import connectToMySQL,DB
# from flask_app.models.ninja import ninja
class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query ="SELECT * FROM dojos;"
        results=connectToMySQL(DB).query_db(query)
        dojos =[]
        for row in results:
            dojos.append(cls(row))
        return dojos
    

    @classmethod
    def save(cls,data):
        query= '''
        INSERT INTO dojos (name ,created_at, updated_at) 
        VALUES (%(name)s , NOW(), NOW());'''
        return connectToMySQL(DB).query_db(query,data)
    
    
    @classmethod
    def dojo_with_members(cls,data ):
        query = """
        SELECT * FROM dojos
        LEFT JOIN ninjas on dojos.id = ninjas.dojo_id
        WHERE dojos.id = %(id)s;"""
        results = connectToMySQL(DB).query_db(query,data)
        dojo = cls(results[0])
        for row in results:
            ninja = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(ninja))
        return dojo 