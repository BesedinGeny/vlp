from src.tables.models import WellData, VLP


def get_check_well_data_exists(session, well_data_hash):
    """
    Checks if the well_data table exists.
    
    :param session:
    :param well_data:
    :return:
    """
    well_id = session.query(WellData.id).filter(
        WellData.id == well_data_hash).scalar()

    return well_id


def get_check_vlp_exists(session, well_id):
    """
    Check if the well_id exists in the session
    :param well_id:
    :return:
    """
    vlp = session.query(VLP.vlp).filter(VLP.well_id == well_id).scalar()
    return vlp


def save_init_data(session, init_data, well_data_id):
    well_data = WellData(
        id=well_data_id,
        inclinometry=init_data["inclinometry"],
        d_cas=init_data["casing"]["d"],
        d_tub=init_data["tubing"]["d"],
        h_tub=init_data["tubing"]["h_mes"],
        wct=init_data["pvt"]["wct"],
        rp=init_data["pvt"]["rp"],
        gamma_oil=init_data["pvt"]["gamma_oil"],
        gamma_gas=init_data["pvt"]["gamma_gas"],
        gamma_wat=init_data["pvt"]["gamma_wat"],
        t_res=init_data["pvt"]["t_res"],
        p_wh=init_data["p_wh"],
        geo_grad=init_data["geo_grad"],
        h_res=init_data["h_res"]
    )
    session.add(well_data)
    session.commit()


def save_vlp_data(session, vlp, init_data_id):
    vlp = VLP(
        vlp=vlp,
        well_id=init_data_id
    )
    session.add(vlp)
    session.commit()


def cache_calculations_fetch(session, well_raw_data):
    well_data_flat_dict = dict_to_flat(well_raw_data)

    # kwargs = {f"WellData.{field}":value for field, value in well_data_flat_dict.items()}
    well_data = session.query(WellData).filter_by(**well_data_flat_dict).limit(1).first()

    if not well_data:
        return

    vlp = session.query(VLP).filter(VLP.well_id == well_data.id).limit(1).first()
    if not vlp:
        print("Have input but no output.")
        # unknown case
        return
    return vlp


def cache_calculation_store(session, well_data, vlp):
    flat_data = dict_to_flat(well_data)
    well_data_obj = WellData(**flat_data)
    session.add(well_data_obj)
    session.commit()
    vlp_obj = VLP(
        well_id=well_data_obj.id,
        q_liq=str(vlp["q_liq"]),
        p_wf=str(vlp["p_wf"])
    )
    session.add(vlp_obj)
    session.commit()

    return vlp_obj


def dict_to_flat(data: dict) -> dict:
    """Makes nesting dict flat"""
    result = {}
    for key, value in data.items():
        if isinstance(value, dict):
            result.update(**dict_to_flat(value))
        elif isinstance(value, list):
            result.update({key: str(value)})
        else:
            result.update({key: value})
    return result

