from flask import Flask
from routes.product_apis_routes import ProductsApisRoutes
from config import config, WORKING_ENV


def create_app():
    _app = Flask(__name__)
    _app.config.from_object(config[WORKING_ENV])
    _app = ProductsApisRoutes.task_apis(_app)
    return _app


if __name__ == '__main__':
    app = create_app()
    app.run(port=5000)
