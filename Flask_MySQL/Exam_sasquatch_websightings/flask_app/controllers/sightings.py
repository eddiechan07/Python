from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models import sighting
from flask_app.models import user
from datetime import datetime, date


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash("You must be logged in to access to this page")
        return redirect('/')
    
    current_user_data = {'id' : session['user_id']}
    user_in_db = user.User.get_user_by_id(current_user_data)
    all_sightings = sighting.Sighting.get_all_sightings()
    return render_template('dashboard.html', all_sightings = all_sightings, user_in_db = user_in_db)

@app.route('/sightings/new')
def new_sighting():
    data = {'id' : session['user_id']}
    user_in_db = user.User.get_user_by_id(data)
    today_date = date.today().strftime('%Y-%m-%d')
    return render_template('new_sightings.html',user_in_db = user_in_db, today_date = today_date)

@app.route('/sightings/new', methods=['POST'])
def report_new_sighting():
    if 'user_id' not in session:
        flash("You must be logged in to access to this page")
        return redirect('/')
    
    today_date = date.today()
    date_of_sighting = datetime.strptime(request.form['date_of_sighting'], '%Y-%m-%d').date()
    if date_of_sighting > today_date:
        flash("The sighting date cannot be in the future.")
        return redirect('/sightings/new')
    
    data = {
        'location': request.form['location'], 
        'date_of_sighting': date_of_sighting, 
        'number_of_sasquatch': request.form['number_of_sasquatch'], 
        'what_happened': request.form['what_happened'],
        'user_id': session['user_id']
    }
    
    sighting.Sighting.save_new_sighting(data)
    return redirect('/dashboard')

@app.route('/sightings/delete/<int:sighting_id>')
def delete_sighting(sighting_id):
    data={'id' : sighting_id}
    sighting.Sighting.delete(data)
    return redirect('/dashboard')

@app.route('/sightings/view/<int:sighting_id>')
def view_sighting(sighting_id):
    user_data = {'id' : session['user_id']}
    user_in_db = user.User.get_user_by_id(user_data)
    sighting_data={'id':sighting_id}
    sightings = sighting.Sighting.view(sighting_data)
    return render_template('/view.html', sightings = sightings, user_in_db = user_in_db)

@app.route('/sightings/edit/<int:sighting_id>')
def edit_sighting(sighting_id):
    if 'user_id' not in session:
        flash("You must be logged in to access to this page")
        return redirect('/')
    
    user_data = {'id' : session['user_id']}
    user_in_db = user.User.get_user_by_id(user_data)
    return render_template('/edit.html',user_in_db=user_in_db, sighting_id = sighting_id)

@app.route('/sightings/edit/<int:sighting_id>/process', methods=['POST'])
def update(sighting_id):
    if 'user_id' not in session:
        flash("You must be logged in to access to this page")
        return redirect('/')
    
    data = {
        'location': request.form['location'], 
        'date_of_sighting': request.form['date_of_sighting'], 
        'number_of_sasquatch': request.form['number_of_sasquatch'], 
        'what_happened': request.form['what_happened'],
        'user_id': session['user_id'],
        'id' : sighting_id
        
    }
    sighting.Sighting.edit(data)
    return redirect('/dashboard')