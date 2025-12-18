from flask import Flask, render_template, request

app = Flask (__name__, template_folder='templates')

@app.route("/", methods=["GET", "POST"]) 
def index():
    result = ''
    if request.method == "POST":
        try:
            expression = request.form["display"]
            result = eval(expression)
        except Exception as e:
            result = "Error"
    return render_template("index.html", result=result)

@app.route("/how_to_use")
def how_to_use():
    return render_template('how_to_use.html')

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)