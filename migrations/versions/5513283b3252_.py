"""empty message

Revision ID: 5513283b3252
Revises: e06f37b1c7d6
Create Date: 2021-03-29 21:08:23.063202

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5513283b3252'
down_revision = 'e06f37b1c7d6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('company', sa.Column('year_later_price', sa.Integer(), nullable=True))
    op.add_column('company', sa.Column('year_later_return', sa.Float(), nullable=True))
    op.drop_column('company', 'bookvalue')
    op.drop_column('company', 'year_later')
    op.drop_column('company', 'bankers')
    op.drop_column('company', 'stocktype')
    op.drop_column('company', 'ipotype')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('company', sa.Column('ipotype', sa.VARCHAR(length=64), autoincrement=False, nullable=True))
    op.add_column('company', sa.Column('stocktype', sa.VARCHAR(length=64), autoincrement=False, nullable=True))
    op.add_column('company', sa.Column('bankers', sa.VARCHAR(length=64), autoincrement=False, nullable=True))
    op.add_column('company', sa.Column('year_later', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('company', sa.Column('bookvalue', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('company', 'year_later_return')
    op.drop_column('company', 'year_later_price')
    # ### end Alembic commands ###
