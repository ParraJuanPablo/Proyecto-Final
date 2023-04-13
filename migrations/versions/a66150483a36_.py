"""empty message

Revision ID: a66150483a36
Revises: d812adc71946
Create Date: 2023-04-13 14:51:23.522483

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a66150483a36'
down_revision = 'd812adc71946'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('valores',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('calorias_ingeridas', sa.Integer(), nullable=False),
    sa.Column('calorias_gastadas', sa.Integer(), nullable=False),
    sa.Column('horas_ejercicio', sa.Integer(), nullable=False),
    sa.Column('horas_sueño', sa.Integer(), nullable=False),
    sa.Column('scoop_proteina', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('valores')
    # ### end Alembic commands ###
