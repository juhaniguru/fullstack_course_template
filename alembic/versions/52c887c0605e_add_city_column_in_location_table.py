"""add city column in location table

Revision ID: 52c887c0605e
Revises: 
Create Date: 2023-11-08 19:19:03.339073

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '52c887c0605e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('location', sa.Column('city', sa.String(45)))


def downgrade() -> None:
    op.drop_column('location', 'city')
