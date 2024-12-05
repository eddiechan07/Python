from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models import post
from flask_app.models import user


@app.route('/wall')
def wall():
    if 'user_id' not in session:
        flash("Please log in first", 'login')
        return redirect ('/')
    
    current_user_id = {'id': session['user_id']}
    current_user = user.User.get_by_id(current_user_id)

    
    posts = post.Post.get_all_posts()
    
    
    return render_template('wall.html', posts = posts, current_user = current_user)

@app.route('/wall/post', methods=['POST'])
def posts():
    if 'user_id' not in session:
        flash("Please log in first", 'login')
        return redirect('/')
    
    data ={
        'content' : request.form['content'],
        'user_id' : session['user_id']
    }
    post.Post.save_posts(data)
    return redirect ('/wall')

