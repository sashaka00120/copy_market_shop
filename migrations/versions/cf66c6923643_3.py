"""3

Revision ID: cf66c6923643
Revises: 0d1b8bc5633c
Create Date: 2018-02-04 23:06:53.177273

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf66c6923643'
down_revision = '0d1b8bc5633c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('characteristic', sa.Column('blue', sa.String(length=30), nullable=True))
    op.add_column('characteristic', sa.Column('chastot', sa.String(length=30), nullable=True))
    op.add_column('characteristic', sa.Column('g4', sa.String(length=30), nullable=True))
    op.add_column('characteristic', sa.Column('hdd', sa.String(length=30), nullable=True))
    op.add_column('characteristic', sa.Column('monit', sa.String(length=30), nullable=True))
    op.add_column('characteristic', sa.Column('oper_m', sa.String(length=30), nullable=True))
    op.add_column('characteristic', sa.Column('optic', sa.String(length=30), nullable=True))
    op.add_column('characteristic', sa.Column('proc', sa.String(length=30), nullable=True))
    op.add_column('characteristic', sa.Column('video', sa.String(length=30), nullable=True))
    op.add_column('characteristic', sa.Column('weight', sa.String(length=30), nullable=True))
    op.add_column('characteristic', sa.Column('wifi', sa.String(length=30), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('characteristic', 'wifi')
    op.drop_column('characteristic', 'weight')
    op.drop_column('characteristic', 'video')
    op.drop_column('characteristic', 'proc')
    op.drop_column('characteristic', 'optic')
    op.drop_column('characteristic', 'oper_m')
    op.drop_column('characteristic', 'monit')
    op.drop_column('characteristic', 'hdd')
    op.drop_column('characteristic', 'g4')
    op.drop_column('characteristic', 'chastot')
    op.drop_column('characteristic', 'blue')
    # ### end Alembic commands ###