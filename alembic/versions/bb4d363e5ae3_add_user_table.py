"""add user table

Revision ID: bb4d363e5ae3
Revises: d27fd7deda50
Create Date: 2025-03-07 18:56:13.206402

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bb4d363e5ae3'
down_revision: Union[str, None] = 'd27fd7deda50'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',    
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'))




            
    
    """Upgrade schema."""
    pass


def downgrade() -> None:    
    op.drop_table('users')
    """Downgrade schema."""
    pass
