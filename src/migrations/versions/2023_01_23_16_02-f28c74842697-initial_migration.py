"""initial_migration

Revision ID: f28c74842697
Revises: 
Create Date: 2023-01-23 16:02:30.399371

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f28c74842697'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vlp',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('q_liq', sa.String(), nullable=True),
    sa.Column('p_wf', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('well_data',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('MD', sa.String(), nullable=True),
    sa.Column('TVD', sa.String(), nullable=True),
    sa.Column('d', sa.Float(), nullable=True),
    sa.Column('h_mes', sa.Float(), nullable=True),
    sa.Column('wct', sa.Float(), nullable=True),
    sa.Column('rp', sa.Float(), nullable=True),
    sa.Column('gamma_oil', sa.Float(), nullable=True),
    sa.Column('gamma_gas', sa.Float(), nullable=True),
    sa.Column('gamma_wat', sa.Float(), nullable=True),
    sa.Column('t_res', sa.Float(), nullable=True),
    sa.Column('p_wh', sa.Float(), nullable=True),
    sa.Column('geo_grad', sa.Float(), nullable=True),
    sa.Column('h_res', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('well_data')
    op.drop_table('vlp')
    # ### end Alembic commands ###
