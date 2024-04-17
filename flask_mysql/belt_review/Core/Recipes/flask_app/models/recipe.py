from flask_app.config.mysqlconnection import connectToMySQL, DB
from flask_app.models.user import User
from flask import flash

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.made_on = data['made_on']
        self.under_30 = data['under_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None

    #get by id 
    @classmethod
    def get_by_id(cls , data):
        query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id WHERE recipes.id = %(id)s;"
        results = connectToMySQL(DB).query_db(query , data)

        if results:
            recipe = cls(results[0])
            user_data = {
                'id': results[0]['users.id'],
                'first_name': results[0]['first_name'],
                'last_name': results[0]['last_name'],
                'email': results[0]['email'],
                'password': results[0]['password'],
                'created_at': results[0]['users.created_at'],
                'updated_at': results[0]['users.updated_at']
            }
            recipe.user = User(user_data)
            return recipe
        return False

    # get all recipes
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id;"
        results = connectToMySQL(DB).query_db(query)
        recipes=[]
        if results:
            for row in results:
                recipe=cls(row)
                user_data ={ 
                    'id': row['users.id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'email': row['email'],
                    'password': row['password'],
                    'created_at': row['users.created_at'],
                    'updated_at': row['users.updated_at']
                }
                recipe.user= User(user_data)
                recipes.append(recipe)
        return recipes

    # add recipe
    @classmethod
    def create(cls, data):
        query = "INSERT INTO recipes (name , description , instructions , made_on , under_30 , user_id) VALUES (%(name)s , %(description)s , %(instructions)s , %(made_on)s , %(under_30)s , %(user_id)s);"
        return connectToMySQL(DB).query_db(query , data)
    #delete recipe
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query, data)
    #update recipe
    @classmethod
    def edit(cls, data):
        query=" UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, made_on = %(made_on)s, under_30 = %(under_30)s WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query, data)
    
    @staticmethod
    def validate_recipe(data):
        is_valid = True
        recipe = Recipe.get_by_id(data)
        if len(data['name']) < 3:
            flash("name must be at leat 3 characters")
            is_valid = False
        if len(data['description']) < 3:
            flash("Description must be at leat 3 characters")
            is_valid = False
        if len(data['instructions']) < 3:
            flash("Instructions must be at leat 3 characters")
            is_valid = False

        return is_valid