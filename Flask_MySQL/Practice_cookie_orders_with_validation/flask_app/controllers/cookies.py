from flask_app import app 
from flask import render_template, redirect, request, flash
from flask_app.models.cookie import Cookie

@app.route('/cookies')
def cookie_orders():
    cookies = Cookie.show_cookie_orders()
    return render_template('cookies.html', cookies = cookies)

@app.route('/cookies/new')
def log_cookie():
    return render_template('new_cookies.html')

@app.route('/cookies/log', methods=['POST'])
def add_new_cookie():
    
    data={
        'customer_name' : request.form['customer_name'],
        'cookie_type' : request.form['cookie_type'],
        'num_of_boxes' : request.form['num_of_boxes']
    }


    if not Cookie.validate_data(data):
        return redirect('/cookies/new')
    Cookie.add_new_cookie(data)
    return redirect('/cookies')

@app.route('/cookies/edit/<int:id>', methods=['POST', 'GET'])
def edit_cookie(id):
    if request.method == 'POST':
        data = {
            'id': id,
            'customer_name': request.form['customer_name'],
            'cookie_type': request.form['cookie_type'],
            'num_of_boxes': request.form['num_of_boxes']
        }
        if not Cookie.validate_data(data):
            return redirect(f'/cookies/edit/{id}')
        Cookie.edit_cookie(data)
        flash("Cookie order updated successfully!", 'success')
        return redirect('/cookies')


    cookie = Cookie.get_cookie_by_id(id)
    return render_template('cookie_editor.html', cookie=cookie)



