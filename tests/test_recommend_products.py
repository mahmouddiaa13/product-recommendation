from config import config, WORKING_ENV
from http import HTTPStatus
import pytest

body = {
    "fecha_dato": "2016-06-28",
    "ncodpers": 1061260,
    "ind_empleado": " N",
    "pais_residencia": "ES",
    "sexo": "H",
    "age": " 24",
    "fecha_alta": "2012-09-17",
    "ind_nuevo": " 0",
    "antiguedad": "     34",
    "indrel": " 1",
    "ult_fec_cli_1t": "",
    "indrel_1mes": "1",
    "tiprel_1mes": "I",
    "indresi": "S",
    "indext": "N",
    "conyuemp": "",
    "canal_entrada": "KHE",
    "indfall": "N",
    "tipodom": " 1",
    "cod_prov": "28",
    "nomprov": "MADRID",
    "ind_actividad_cliente": " 0",
    "renta": "396426.42",
    "segmento": "03 - UNIVERSITARIO",
    "ind_ahor_fin_ult1": 0,
    "ind_aval_fin_ult1": " 0",
    "ind_cco_fin_ult1": "     1",
    "ind_cder_fin_ult1": "0",
    "ind_cno_fin_ult1": 0,
    "ind_ctju_fin_ult1": "0",
    "ind_ctma_fin_ult1": "0",
    "ind_ctop_fin_ult1": "0",
    "ind_ctpp_fin_ult1": "0",
    "ind_deco_fin_ult1": "0",
    "ind_deme_fin_ult1": "0",
    "ind_dela_fin_ult1": "0",
    "ind_ecue_fin_ult1": "0",
    "ind_fond_fin_ult1": "0",
    "ind_hip_fin_ult1": "0",
    "ind_plan_fin_ult1": "0",
    "ind_pres_fin_ult1": "0",
    "ind_reca_fin_ult1": "0",
    "ind_tjcr_fin_ult1": "0",
    "ind_valo_fin_ult1": "0",
    "ind_viv_fin_ult1": "0",
    "ind_nomina_ult1": " 0",
    "ind_nom_pens_ult1": " 0",
    "ind_recibo_ult1": "0"
}


@pytest.mark.parametrize('ind_ahor_fin_ult1, ind_empleado, expected_status_code', [
    ("shgs", "N", HTTPStatus.BAD_REQUEST),
    ("0", "   N", HTTPStatus.OK),
    (1, "N", HTTPStatus.OK)
])
def test_create_task(client, ind_ahor_fin_ult1, ind_empleado, expected_status_code):
    body["ind_ahor_fin_ult1"] = ind_ahor_fin_ult1
    body["ind_empleado"] = ind_empleado
    api_version = config[WORKING_ENV].API_VERSION
    response = client.post(f'/api/{api_version}/product/recommend', json=body)
    assert response.status_code == expected_status_code

