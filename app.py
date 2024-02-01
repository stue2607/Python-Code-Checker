# Import the built-in ast module
import ast
# Import the Flask module
from flask import Flask, request, render_template

# Create a Flask app object
app = Flask(__name__)

# Define a function to check user input python code for errors
def check_code(code):
    # Try to parse the code as an abstract syntax tree
    try:
        tree = ast.parse(code)
        # If no exception is raised, the code is syntactically valid
        return "The code is valid."
    # If an exception is raised, catch it and return the error message
    except SyntaxError as e:
        return f"The code is invalid.\n{e}"

# Define a route for the home page
@app.route("/")
def home():
    # Render a template that contains a form for the user to enter some python code
    return render_template("home.html")

# Define a route for the result page
@app.route("/result", methods=["POST"])
def result():
    # Get the user input code from the form
    code = request.form.get("code")

    # Call the check_code function with the user input code
    result = check_code(code)
    # Render a template that shows the result
    return render_template("result.html", result=result)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
