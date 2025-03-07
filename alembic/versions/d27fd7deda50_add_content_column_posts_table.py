"""add content column  posts table

Revision ID: d27fd7deda50
Revises: 964626ae8734
Create Date: 2025-03-07 18:44:58.100351

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd27fd7deda50'
down_revision: Union[str, None] = '964626ae8734'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    """Upgrade schema."""
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    
    """Downgrade schema."""
    pass
