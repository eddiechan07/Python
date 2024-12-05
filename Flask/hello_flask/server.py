from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo"

@app.route('/say/<name>')
def say_name(name):
    return f"Hi {name.capitalize()}!"

@app.route('/repeat/<int:num>/<string>')
def repeat(num, string):
    return (f"{(string + '\n') * num}").replace('\n', '<br>')

@app.route('/users/<name>/<num>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(name, num):
    print(name)
    print(num)
    return f"username: {name}, id: {num}"

@app.errorhandler(404)
def page_not_found(e):
    return f"Sorry! No response. Try again."


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8000)
