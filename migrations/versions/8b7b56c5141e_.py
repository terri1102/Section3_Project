"""empty message

Revision ID: 8b7b56c5141e
Revises: 5513283b3252
Create Date: 2021-03-30 10:18:23.752444

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8b7b56c5141e'
down_revision = '5513283b3252'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stock')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stock',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('companyname', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('stockcode', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('ipodate', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('ipotype', sa.VARCHAR(length=40), autoincrement=False, nullable=True),
    sa.Column('stocktype', sa.VARCHAR(length=40), autoincrement=False, nullable=True),
    sa.Column('bankers', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('bookvalue', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('total', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('stock_amount', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='stock_pkey')
    )
    # ### end Alembic commands ###
