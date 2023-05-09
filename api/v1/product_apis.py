from controllers.product_controllers import ProductController
from schemas.product_schema import DataIn
from flask_pydantic import validate
from http import HTTPStatus
import json
from flask import request, Response


@validate(body=DataIn)
def recommend_product():
    body = request.get_json()
    body_pydantic = DataIn(**body)
    ncodpers = body_pydantic.ncodpers
    product_controller = ProductController()
    products = product_controller.recommend_product(body_pydantic)
    return Response(response=json.dumps({ncodpers: products}),
                    status=HTTPStatus.OK,
                    mimetype='application/json')
