from dojos_app.config.mysqlconnection import connectToMySQL
from dojos_app.models.dojo import Dojo


class Ninja:
    def __init__(self, data):
        self.ninja_id = data['ninja_id']
        self.first_name= data['first_name']
        self.last_name= data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_ninjas(cls, dojo_id):
        query = "SELECT * FROM ninjas WHERE dojo_id=%(dojo_id)s;"
        data = {
            "dojo_id" : dojo_id
        }
        results = connectToMySQL("dojos_schema").query_db(query, data)
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas

    @classmethod
    def save_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        return connectToMySQL('dojos_schema').query_db(query,data)