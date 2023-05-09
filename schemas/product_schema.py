from pydantic import BaseModel
from typing import Optional


class DataIn(BaseModel):
    fecha_dato: str
    ncodpers: int
    ind_empleado: str
    pais_residencia: str
    fecha_dato: str
    sexo: str
    age: str
    fecha_alta: str
    ind_nuevo: str
    antiguedad: str
    indrel: str
    ult_fec_cli_1t: str
    indrel_1mes: str
    tiprel_1mes: str
    indresi: str
    indext: str
    conyuemp: str
    canal_entrada: str
    indfall: str
    tipodom: str
    cod_prov: str
    nomprov: str
    ind_actividad_cliente: str
    renta: str
    segmento: str
    ind_nuevo: str
    ind_ahor_fin_ult1: Optional[int] = 0
    ind_aval_fin_ult1: Optional[int] = 0
    ind_cco_fin_ult1: Optional[int] = 0
    ind_cder_fin_ult1: Optional[int] = 0
    ind_cno_fin_ult1: Optional[int] = 0
    ind_ctju_fin_ult1: Optional[int] = 0
    ind_ctma_fin_ult1: Optional[int] = 0
    ind_ctop_fin_ult1: Optional[int] = 0
    ind_ctpp_fin_ult1: Optional[int] = 0
    ind_deco_fin_ult1: Optional[int] = 0
    ind_deme_fin_ult1: Optional[int] = 0
    ind_dela_fin_ult1: Optional[int] = 0
    ind_ecue_fin_ult1: Optional[int] = 0
    ind_fond_fin_ult1: Optional[int] = 0
    ind_hip_fin_ult1: Optional[int] = 0
    ind_plan_fin_ult1: Optional[int] = 0
    ind_pres_fin_ult1: Optional[int] = 0
    ind_reca_fin_ult1: Optional[int] = 0
    ind_tjcr_fin_ult1: Optional[int] = 0
    ind_valo_fin_ult1: Optional[int] = 0
    ind_viv_fin_ult1: Optional[int] = 0
    ind_nomina_ult1: Optional[int] = 0
    ind_nom_pens_ult1: Optional[int] = 0
    ind_recibo_ult1: Optional[int] = 0

# class DataIn(BaseModel):
#     fecha_dato: str
#     ncodpers: str
#     ind_empleado: str
#     pais_residencia: str
#     fecha_dato: str
#     sexo: str
#     age: str
#     fecha_alta: str
#     ind_nuevo: str
#     antiguedad: str
#     indrel: str
#     ult_fec_cli_1t: str
#     indrel_1mes: str
#     tiprel_1mes: str
#     indresi: str
#     indext: str
#     conyuemp: str
#     canal_entrada: str
#     indfall: str
#     tipodom: str
#     cod_prov: str
#     nomprov: str
#     ind_actividad_cliente: str
#     renta: str
#     segmento: str
#     ind_nuevo: str
#     ind_nuevo: str
#     ind_nuevo: str
#     ind_nuevo: str
#     ind_nuevo: str
#     ind_ahor_fin_ult1: str
#     ind_aval_fin_ult1: str
#     ind_cco_fin_ult1: str
#     ind_cder_fin_ult1: str
#     ind_cno_fin_ult1: str
#     ind_ctju_fin_ult1: str
#     ind_ctma_fin_ult1: str
#     ind_ctop_fin_ult1: str
#     ind_ctpp_fin_ult1: str
#     ind_deco_fin_ult1: str
#     ind_deme_fin_ult1: str
#     ind_dela_fin_ult1: str
#     ind_ecue_fin_ult1: str
#     ind_fond_fin_ult1: str
#     ind_hip_fin_ult1: str
#     ind_plan_fin_ult1: str
#     ind_pres_fin_ult1: str
#     ind_reca_fin_ult1: str
#     ind_tjcr_fin_ult1: str
#     ind_valo_fin_ult1: str
#     ind_viv_fin_ult1: str
#     ind_nomina_ult1: str
#     ind_nom_pens_ult1: str
#     ind_recibo_ult1: str