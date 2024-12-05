from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/dojos')
def dojos():
    all_dojos = Dojo.get_all_dojos()
    return render_template("dojos.html",  dojos=all_dojos)

@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    Dojo.create_dojo(request.form)
    return redirect('/dojos')
    

@app.route('/ninjas')
def ninjas():
    all_dojos = Dojo.get_all_dojos()
    return render_template("ninjas.html", dojos=all_dojos)

@app.route('/create_ninja', methods=['POST'])
def create_ninja():
    dojo_id = request.form['dojo']
    data={
        'dojos_id' : dojo_id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age']
    }
    Ninja.create_ninja(data)
    return redirect(f'/dojos/{dojo_id}')

@app.route('/dojos/<int:dojo_id>')
def show_ninjas_in_dojo(dojo_id):
    print(f"Received dojo_id: {dojo_id}")
    dojo = Dojo.get_by_id(dojo_id)
    ninjas = Ninja.get_all_by_dojo(dojo_id)

    print(f"Dojo: {dojo}")
    print(f"Ninjas: {ninjas}")

    return render_template("show_ninjas_in_dojo.html", dojo = dojo, ninjas = ninjas)







