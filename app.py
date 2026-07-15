from flask import Flask, render_template

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"]

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/hello")
def hello():
    return "Hello Flask!"



if __name__ == "__main__":
    app.run(debug=True)


