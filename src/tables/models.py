import sqlalchemy as sa

from db import Base


class WellData(Base):
    """Входные парамтеры"""
    __tablename__ = "well_data"
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    MD = sa.Column(sa.String)
    TVD = sa.Column(sa.String)
    d = sa.Column(sa.Float)
    h_mes = sa.Column(sa.Float)
    wct = sa.Column(sa.Float)
    rp = sa.Column(sa.Float)
    gamma_oil = sa.Column(sa.Float)
    gamma_gas = sa.Column(sa.Float)
    gamma_wat = sa.Column(sa.Float)
    t_res = sa.Column(sa.Float)
    p_wh = sa.Column(sa.Float)
    geo_grad = sa.Column(sa.Float)
    h_res = sa.Column(sa.Float)


class VLP(Base):
    """Результат входных параметров"""
    __tablename__ = "vlp"
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    q_liq = sa.Column(sa.String)
    p_wf = sa.Column(sa.String)
