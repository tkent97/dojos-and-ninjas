from dojos_app import app
from flask import render_template, request, redirect, session
from dojos_app.models.ninja import Ninja
from dojos_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')


@app.route('/ninjas')
def new_ninja():
    dojos = Dojo.get_dojos()
    return render_template('new_ninja.html', dojos=dojos)

@app.route('/create', methods=['POST'])
def create_ninja():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo_id']
    }
    Ninja.save_ninja(data)
    return redirect('/')


