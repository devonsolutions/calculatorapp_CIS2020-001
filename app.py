from flask import Flask, render_template, request

app = Flask (__name__, template_folder='templates')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/matrix_addition")
def matrix_addition():
    return render_template('matrix_addition.html')

@app.route("/matrix_subtraction")
def matrix_subtraction():
    return render_template('matrix_subtraction.html')

if __name__ == "__main__":
    app.run()