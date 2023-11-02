import problems
from flask import Flask, request, render_template
app = Flask(__name__)

test = problems.Problem(0, 10)

@app.route("/")
def home():
    return test.test_prompt()

@app.route("/problems")
def display_problem():
    return render_template(
            "test.html",
            problem=test.test_prompt()
            )

@app.route("/problems", methods=["POST"])
def problem_post():
    text=request.form['problem']
    print(text)
    if text == test.bin_solution:
        return render_template(
                "result.html",
                correct=True
                )

    return render_template(
                "result.html",
                )
