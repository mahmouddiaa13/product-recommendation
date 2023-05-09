from utils.lazy_viewer import LazyView
from config import config, WORKING_ENV


class ProductsApisRoutes:

    @staticmethod
    def task_apis(app):
        api_version = config[WORKING_ENV].API_VERSION

        app.add_url_rule(f"/api/{api_version}/product/recommend", methods=['POST'],
                         view_func=LazyView(f'api.{api_version}.product_apis.recommend_product'))

        return app
