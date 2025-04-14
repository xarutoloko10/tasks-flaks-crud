from flask import Flask

# variavel __name__ = "__main__"
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello Wolrd!"

@app.route("/about")
def about():
    return "Pagina Sobre"

if __name__ == "__main__":
    app.run(debug=True)