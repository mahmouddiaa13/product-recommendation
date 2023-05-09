from data_processor.data_processor import processData
import data_processor.data_processor as prod_recomm
from schemas.product_schema import DataIn

from flask import current_app
import xgboost as xgb
import numpy as np


class ProductController:

    def recommend_product(self, req_body: DataIn):
        model = xgb.Booster()
        model.load_model(current_app.config["MODEL_FILE_PATH"])
        x_vars_list, cust_dict = processData(req_body.dict(), {})
        if not x_vars_list:
            return []
        test_X = np.array(x_vars_list)
        xgtest = xgb.DMatrix(test_X)
        del x_vars_list
        preds = model.predict(xgtest)
        del test_X, xgtest
        target_cols = np.array(prod_recomm.target_cols)
        preds = np.argsort(preds, axis=1)
        preds = np.fliplr(preds)[:, :7]
        final_preds = [" ".join(list(target_cols[pred])) for pred in preds]
        return final_preds
