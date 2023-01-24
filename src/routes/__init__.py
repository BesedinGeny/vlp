import json

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.models.models import VlpCalcRequest, VlpCalcResponse
from src.routes.queries import cache_calculation_store, cache_calculations_fetch
from src.db import get_session

main_router = APIRouter(prefix="/vlp", tags=["VLP"])


@main_router.post("/calc", response_model=VlpCalcResponse)
def calc_vlp(
        vlp_in: VlpCalcRequest,
        db: Session = Depends(get_session)
):
    """Расчёт VLP по исходным данным и сохранение в Базу"""
    from src.calculations.vlp import calc_vlp as vlp_calculation  # noqa
    vlp = cache_calculations_fetch(db, vlp_in.dict())
    if vlp:
        print("Cache worked")
        vlp.q_liq = json.loads(vlp.q_liq)
        vlp.p_wf = json.loads(vlp.p_wf)
        return vlp

    vlp_result = vlp_calculation(**vlp_in.dict())
    # test
    from src.tables.models import WellData, VLP
    wd = db.query(WellData).all()
    vlps = db.query(VLP).all()

    vlp = cache_calculation_store(db, vlp_in.dict(), vlp_result)
    vlp.q_liq = json.loads(vlp.q_liq)
    vlp.p_wf = json.loads(vlp.p_wf)
    return vlp

