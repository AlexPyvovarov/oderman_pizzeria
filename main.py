from flask import Flask
from flask import render_template


app = Flask(__name__)

title_site = "Oderman"


@app.route("/")
def index():
    return render_template(
        template_name_or_list="index.html",
        title=title_site,
    )


@app.errorhandler(404)
def page_not_found(error):
    return "this page doesn't exist", 404


@app.route("/menu")
def menu():
    pizzas = [
        {"name": "ggig", "toppings": "gsrg", "price": "190"},
        {"name": "fabaifub", "toppings": "gsrg", "price": "230"},
        {"name": "gashbfaiu", "toppings": "fvshbf", "price": "100"}
    ]
    return render_template(template_name_or_list="index.html", pizzas=pizzas)


if __name__ == "__main__":
    app.run(debug=True)
