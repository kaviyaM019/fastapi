"""add foreign-key to posts table

Revision ID: d12f86275c14
Revises: bb4d363e5ae3
Create Date: 2025-03-07 19:07:36.023788

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd12f86275c14'
down_revision: Union[str, None] = 'bb4d363e5ae3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users",local_cols= ['owner_id'],remote_cols=['id'], ondelete="CASCADE")

    """Upgrade schema."""

    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")    
    
    """Downgrade schema."""
    pass
