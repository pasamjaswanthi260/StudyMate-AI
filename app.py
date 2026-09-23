from flask import Flask, render_template, request
from gemini_service import generate_study_response

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    response = ""

    if request.method == "POST":

        feature = request.form.get("feature")
        question = request.form.get("question")

        # Check whether the user entered anything
        if not question or not question.strip():

            response = "Please enter some study content before generating a response."

        # Check whether the input is too long
        elif len(question) > 10000:

            response = "Your input is too long. Please keep it under 10,000 characters."

        else:

            response = generate_study_response(feature, question)

    return render_template("index.html", response=response)


if __name__ == "__main__":
    app.run(debug=True)