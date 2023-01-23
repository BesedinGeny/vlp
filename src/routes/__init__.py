from fastapi import APIRouter
from src.models.models import VlpCalcRequest, VlpCalcResponse
from src.routes.queries import save_init_data, save_vlp_data, get_check_well_data_exists, get_check_vlp_exists

main_router = APIRouter(prefix="/vlp", tags=["VLP"])


@main_router.post("/calc", response_model=VlpCalcResponse)
def calc_vlp(vlp_in: VlpCalcRequest):
    """Расчёт VLP по исходным данным и сохранение в Базу"""
    from src.calculations.vlp import calc_vlp as vlp_calculation  # noqa
    data = dict(
        inclinometry=vlp_in.inclinometry.dict(),
        casing=vlp_in.casing.dict(),
        tubing=vlp_in.tubing.dict(),
        pvt=vlp_in.pvt.dict(),
        p_wh=vlp_in.p_wh,
        geo_grad=vlp_in.geo_grad,
        h_res=vlp_in.h_res
    )
    return vlp_calculation(**data)

