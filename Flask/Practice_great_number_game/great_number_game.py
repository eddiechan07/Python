from flask import Flask, render_template, request, redirect, session
import random


app = Flask(__name__)
app.secret_key = "you_secret_key"

@app.route('/')
def random_number():
    if 'number' not in session:
        session['number'] = random.randint(1,100)
        session['attempts'] = 0
    return render_template('index.html')

@app.route('/guess', methods = ['POST'])
def guess():
    guess = int(request.form['value'])
    number = session['number']
    session['attempts'] += 1
    attempts = session['attempts'] 

    if guess < number:
        status = "Too Low!"
    elif guess > number:
        status = "Too High!"   
    else:
        status = f"Congrats! The number is {number}, you have tried {attempts} times" 
        session.pop('number')
        session.pop('attempts')
    return render_template('index.html', status = status, attempts = attempts)


    
if __name__ == "__main__":
    app.run(debug=True, host ='127.0.0.1', port = 8000)


