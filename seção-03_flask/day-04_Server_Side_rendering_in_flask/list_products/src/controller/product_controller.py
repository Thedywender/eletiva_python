from flask import Blueprint, redirect, render_template, request
from model.product import Product

product_controller = Blueprint("product_controller", __name__)

products = []


@product_controller.route("/", methods=("GET"))
def product_view():
    return render_template("products.html", products=products)


@product_controller.route("/", methods=("POST"))
def add_product():
    id = len(products) + 1
    name = request.form["name"]
    price = request.form["price"]
    product = Product(id, name, price)
    return redirect("/")


@product_controller.route("/delete/<int:product_id>")
def delete_product(product_id):
    for product in products:
        if product.id == product_id:
            products.remove(product)
            break
        return redirect("/")
