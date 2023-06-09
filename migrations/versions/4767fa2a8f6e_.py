"""empty message

Revision ID: 4767fa2a8f6e
Revises: e2d5fda8b7c5
Create Date: 2023-05-13 01:45:14.244401

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4767fa2a8f6e'
down_revision = 'e2d5fda8b7c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('configue')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('year', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('weight', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('height', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('height')
        batch_op.drop_column('weight')
        batch_op.drop_column('year')

    op.create_table('configue',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('edad', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('peso', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('estatura', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='configue_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='configue_pkey')
    )
    # ### end Alembic commands ###
