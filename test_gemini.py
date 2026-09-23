from flask import Flask, render_template, request
from gemini_service import generate_study_response

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    response = ""

    if request.method == "POST":

        feature = request.form.get("feature")
        question = request.form.get("question")

        response = generate_study_response(feature, question)

    return render_template("index.html", response=response)


if __name__ == "__main__":
    app.run(debug=True)