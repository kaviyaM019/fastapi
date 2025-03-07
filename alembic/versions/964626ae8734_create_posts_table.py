"""create posts table

Revision ID: 964626ae8734
Revises: 
Create Date: 2025-03-07 18:20:36.445640

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '964626ae8734'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('title', sa.String(), nullable=False)
    )
    """Upgrade schema."""

    pass


def downgrade() -> None:
    op.drop_table('posts')
    
    """Downgrade schema."""
    pass
