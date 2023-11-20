"""add file table

Revision ID: 9062e52dc642
Revises: 
Create Date: 2023-11-19 14:49:05.670946

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '9062e52dc642'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('file', sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('original_name', sa.String(255), nullable=False),
                    sa.Column('random_name', sa.String(255), nullable=False, unique=True),
                    sa.Column('inspectionform_id', sa.Integer, nullable=False, index=True),
                    sa.ForeignKeyConstraint(('inspectionform_id',), ['inspectionform.id']))


def downgrade() -> None:
    op.drop_table('file')
