from flask import Blueprint, render_template
from model.book_model import Book

book_controller = Blueprint("book_controller", __name__)


@book_controller.route("/", methods=["GET"])
def book_view():
    book = Book("Dom Casmurro", "Machado de Assis", 1899)
    return render_template("index.html", book=book)
