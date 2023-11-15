"""add test table

Revision ID: 98bfea4e6544
Revises: 52c887c0605e
Create Date: 2023-11-08 19:31:37.037984

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '98bfea4e6544'
down_revision: Union[str, None] = '52c887c0605e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('testtable1', sa.Column('id', sa.Integer, primary_key=True), sa.Column('test', sa.Text))



def downgrade() -> None:
    op.drop_table('testtable1')
