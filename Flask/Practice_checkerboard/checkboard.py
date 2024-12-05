from flask import Flask, render_template
app = Flask (__name__)

# @app.route('/')
# def test():
#     return "Test successed"

@app.route('/')
def default():
    row = 8
    column = 8
    color1 = "black"
    color2 = "red"
    return render_template('checkboard.html', row = row, column = column, color1 = color1, color2 = color2)

@app.route('/<int:column>')
def custom_columns(column):
    row = 8
    color1 = "green"
    color2 = "orange"
    return render_template('checkboard.html', row = row, column = column, color1 = color1, color2 = color2)

@app.route('/<int:row>/<int:column>')
def custom_row_and_columns(row, column):
    color1 = "purple"
    color2 = "gray"
    return render_template('checkboard.html', row = row, column = column, color1 = color1, color2 = color2)

@app.route('/<int:row>/<int:column>/<color1>/<color2>')
def custom_row_and_columns_and_colors(row, column, color1, color2):
    return render_template('checkboard.html', row = row, column = column, color1 = color1, color2 = color2)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port = 8000)