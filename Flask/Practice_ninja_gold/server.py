from flask import Flask, render_template, redirect, session, request
import random

app = Flask (__name__)
app.secret_key = 'secret'


@app.route('/')
def display():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activities' not in session:
        session['activities'] = []
    if 'move_count' not in session:
        session['move_count'] = 0
    
    if session['gold'] >= 500:
        session['status'] = 'win'
    elif session['move_count']>= 15:
        session['status'] = 'lose'
    else: session['status'] = 'playing'

    return render_template('index.html', gold = session['gold'], activities = session['activities'], move_count = session['move_count'], status = session['status'])

@app.route('/process_money', methods=['POST'])
def process_money():
    if session['status'] in ['win' or 'lose']:
        return redirect('/')

    place = request.form['place']
    if place == 'farm':
        gold_earned = random.randint(10,20)
    elif place == 'cave':
        gold_earned = random.randint(5,10)
    elif place == 'house':
        gold_earned = random.randint(2,5)
    elif place == 'casino':
        gold_earned = random.randint(-50,50)
    else:
        return redirect('/')

    session['gold'] += gold_earned
    session['move_count'] += 1
    status = 'positive' if gold_earned>=0 else 'negative'
    activity = {
        'message' : f'Earned {gold_earned} gold from the {place}.' if gold_earned>=0 else f'Lost {abs(gold_earned)} gold at the {place}.',
        'status' : status
        }
    session['activities'].insert(0,activity)

    if session['gold'] >= 500:
        session['status'] = 'win'
    elif session['move_count']>= 15:
        session['status'] = 'lose'

    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True, host = "127.0.0.1", port=8000)



