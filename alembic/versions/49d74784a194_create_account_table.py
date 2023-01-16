"""create account table

Revision ID: 49d74784a194
Revises: 
Create Date: 2023-01-14 14:59:01.916238

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49d74784a194'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'car_plates',
        sa.Column('id_car_plates', sa.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False),
        sa.Column('plate', sa.String(10), nullable=False),
    )

def downgrade():
    op.drop_table('car_plates')
