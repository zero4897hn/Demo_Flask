"""create_table_car

Revision ID: 2d452fa8b8fd
Revises: 
Create Date: 2024-03-01 14:23:49.234548

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2d452fa8b8fd'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'car',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('brand', sa.String(50), nullable=False),
        sa.Column('model', sa.String(50), nullable=False),
        sa.Column('year', sa.Integer, nullable=False)
    )
    pass


def downgrade() -> None:
    op.drop_table('car')
    pass
