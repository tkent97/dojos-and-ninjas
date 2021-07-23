from flask import render_template, request, redirect, session
from dojos_app import app
from dojos_app.models.ninja import Ninja
from dojos_app.models.dojo import Dojo

@app.route('/dojos')
def all_dojos():
    dojos = Dojo.get_dojos()
    return render_template('new_dojo.html', dojos=dojos)


@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    data = {
        'name': request.form['name']
    }
    Dojo.save_dojos(data)
    return redirect('/')


@app.route('/dojos/<int:dojo_id>')
def show_ninjas(dojo_id):
    get_selected = Dojo.get_one_dojo(dojo_id)
    ninjas = Ninja.get_all_ninjas(dojo_id)
    return render_template('dojo_show.html', ninjas=ninjas, selected_dojo=get_selected)