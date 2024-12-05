from flask import Flask, render_template
app = Flask(__name__)

# @app.route('/')
# def default():
#     return f"Hello, Assignment!"

@app.route('/play')
def play():
    return render_template('play.html', times =3, color = 'blue')

@app.route('/play/<int:times>')
def num_of_boxes(times):
    return render_template('play.html', times =times)

@app.route('/play/<int:times>/<color>')
def boxes(times, color):
    return render_template('play.html', times =times, color = color)


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8000)  


