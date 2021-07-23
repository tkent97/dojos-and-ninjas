from dojos_app import app
from dojos_app.controllers import ninja, dojo

if __name__ == '__main__':  
    app.run(debug=True)   

# python -m pipenv install flask pymysql flask-bcrypt