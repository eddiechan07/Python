from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)

app.secret_key = 'your_secret_key'
@app.route('/')
def visit_count():
    if "visit_count" in session:
        session["visit_count"] += 1
    else:
         session["visit_count"] = 1
    visit_count = session["visit_count"]
    session["actual_visits"] = session.get("actual_visits", 0) + 1

    return render_template('index.html', visit_count = visit_count, actual_visit = session["actual_visits"])

@app.route('/counter_by_two')
def visit_count_by_two():
    if "visit_count" in session:
        session["visit_count"] += 2
    else:
         session["visit_count"] = 2
    visit_count = session["visit_count"]
    session["actual_visits"] = session.get("actual_visits", 0) + 1
    
    return render_template('index.html', visit_count = visit_count, actual_visit = session["actual_visits"])  

@app.route('/counter_by_you', methods =['POST'])
def visit_count_by_you():
    increment_value = request.form["value"]
    increment_value = int(increment_value)
    session["visit_count"] = session.get("visit_count") + increment_value -1

    return redirect('/')  

@app.route('/reset')
def reset():
    session.clear() 
    return redirect('/')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, host = '127.0.0.1', port =8000)