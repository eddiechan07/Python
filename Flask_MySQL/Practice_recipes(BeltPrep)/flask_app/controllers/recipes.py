from flask_app import app
from flask import render_template, request, session, redirect, flash
from flask_app.models import user
from flask_app.models import recipe





@app.route('/recipes/new', methods=['GET'])
def recipes_dashbord():
    if 'user_id' not in session:
        flash("You must be logged in to access this page!")
        return redirect('/')

    return render_template('add_new_recipe.html')

@app.route('/recipes/new', methods=['POST'])
def add_new_recipe():

    if not recipe.Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')
    
    data = {
        'name' : request.form['name'],
        'description' : request.form['description'],
        'instructions' : request.form['instructions'],
        'date_cooked' : request.form['date_cooked'],
        'under_30_minutes' : request.form['under_30_minutes'],
        'user_id' : session['user_id']
    }
    
    recipe.Recipe.add_new_recipe(data)
    return redirect('/recipes')

@app.route('/recipes/delete/<int:recipe_id>')
def delete_recipe(recipe_id):
    if 'user_id' not in session:
        flash("You must be logged in to access this page!")
        return redirect('/')
    
    data = {'id' : recipe_id}
    recipe.Recipe.delete(data)
    return redirect('/recipes')

@app.route('/recipes/edit/<int:recipe_id>', methods=['GET'])
def edit_recipe_dashbord(recipe_id):
    if 'user_id' not in session:
        flash("You must be logged in to access this page!")
        return redirect('/')

    data = {'id': recipe_id}
    recipe_to_edit = recipe.Recipe.get_one_recipe(data)
    return render_template('/recipe_edit.html', recipe_to_edit = recipe_to_edit)

@app.route('/recipes/edit/<int:recipe_id>', methods=['POST'])
def edit_recipe(recipe_id):
    if 'user_id' not in session:
        flash("You must be logged in to access this page!")
        return redirect('/')
    
    if not recipe.Recipe.validate_recipe(request.form):
        return redirect(f'/recipe/edit/{recipe_id}')
    
    data = {
        'name' : request.form['name'],
        'description' : request.form['description'],
        'instructions' : request.form['instructions'],
        'date_cooked' : request.form['date_cooked'],
        'under_30_minutes' : request.form['under_30_minutes'],
        'user_id' : session['user_id']
    }
    recipe.Recipe.update(data)
    return redirect('/recipes')

@app.route('/recipes/<int:recipe_id>')
def show_recipe(recipe_id):
    
    user_data = {"id" : session['user_id']}
    recipe_data = {'id': recipe_id}
    user_in_db = user.User.get_by_id(user_data) 
    one_recipe = recipe.Recipe.get_one_recipe(recipe_data)
    return render_template('show_recipe.html', user_in_db = user_in_db, one_recipe = one_recipe)


@app.route('/recipes')
def dashboard():
    if 'user_id' not in session:
        flash("You must be logged in to access this page!")
        return redirect('/')
    
    data = {"id" : session['user_id']}
    user_in_db = user.User.get_by_id(data)   
    all_recipes = recipe.Recipe.get_all_recipes()
    
    return render_template('recipes.html', user_in_db = user_in_db, all_recipes = all_recipes)
