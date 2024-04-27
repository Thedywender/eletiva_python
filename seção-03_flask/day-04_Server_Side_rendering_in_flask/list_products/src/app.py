from flask import Flask
from controller.product_controller import product_controller
from model.product import Product

app = Flask(__name__)

app.register_blueprint(product_controller, url_prefix="/")
app.register_blueprint(product_controller, url_prefix="/delete/<int:product_id>")


if __name__ == "__main__":
    app.run()
