from flask import Flask, render_template, request
import sympy as sp

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error_message = None
    if request.method == "POST":
        try:
            # Get the expression from the user
            expression = request.form["expression"]
            # Parse the expression safely using sympy
            result = sp.sympify(expression)
        except Exception as e:
            error_message = "Error: Invalid input"

    return render_template("index.html", result=result, error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)
