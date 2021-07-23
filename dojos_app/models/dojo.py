from dojos_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.dojo_id = data['dojo_id']
        self.name= data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_schema').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def get_one_dojo(cls, dojo_id):
        query = "SELECT * FROM dojos WHERE dojo_id=%(dojo_id)s;"

        data = {
            "dojo_id" : dojo_id
        }
        results = connectToMySQL('dojos_schema').query_db(query, data)
        dojo = cls(results[0])
        return dojo

    @classmethod
    def save_dojos(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s;"
        return connectToMySQL('dojos_schema').query_db(query, data)
