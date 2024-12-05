from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key= 'Your secret!'

@app.route('/')
def survey():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form.get('name')
    session['dojo_location'] = request.form.get('dojo_location')
    session['favorite_language'] = request.form.get('favorite_language')
    session['comment'] = request.form.get('comment')
    return redirect('/result')

@app.route('/result')
def show_info():
    name = session.get('name')
    dojo_location = session['dojo_location']
    favorite_language = session['favorite_language']
    comment = session['comment'] 
    return render_template("show.html", name=name, dojo_location=dojo_location, favorite_language=favorite_language, comment=comment)



if __name__ == "__main__":
    app.run(debug=True, host = '127.0.0.1', port=8000)
